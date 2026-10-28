#!/usr/bin/env python3
"""Repair explicitly masked video regions locally; preserve audio and originals."""
from __future__ import annotations
import argparse
import hashlib
import json
import math
from pathlib import Path
import shutil
import subprocess
import sys

# Probe in a separate process so PyAV/OpenCV's bundled device libraries do not
# collide when both packages use differently versioned FFmpeg distributions.
PROBE = r'''
import av, hashlib, json, sys
p=sys.argv[1]; c=av.open(p); v=c.streams.video[0]
r={'width':v.width,'height':v.height,'fps_num':v.average_rate.numerator,'fps_den':v.average_rate.denominator,'container_seconds':c.duration/av.time_base if c.duration else None,'has_audio':bool(c.streams.audio)}
h=hashlib.sha256(); packets=0
if r['has_audio']:
 for x in c.demux(audio=0):
  if x.size: h.update(bytes(x)); packets+=1
r['audio_sha256']=h.hexdigest() if r['has_audio'] else None; r['audio_packets']=packets
r['audio_start_seconds']=float(c.streams.audio[0].start_time*c.streams.audio[0].time_base) if r['has_audio'] and c.streams.audio[0].start_time is not None else None
c.close()
c=av.open(p); count=0; previous=None; errors=[]; expected=r['fps_den']/r['fps_num']
for f in c.decode(video=0):
 t=float(f.time) if f.time is not None else None
 if t is None: errors.append('missing timestamp')
 elif previous is not None and abs((t-previous)-expected)>max(.0001,expected*.02): errors.append('non-constant frame interval')
 if count==0: r['first_video_seconds']=t
 previous=t; count+=1
c.close(); r['frames']=count; r['cfr']=not errors; r['decode']='pass'; print(json.dumps(r))
'''

def probe(path: Path) -> dict:
    result = subprocess.run([sys.executable, '-c', PROBE, str(path)], capture_output=True, text=True, check=True)
    return json.loads(result.stdout)

def load_regions(config: Path, width: int, height: int):
    import cv2
    import numpy as np
    data = json.loads(config.read_text())
    method = data.get('method', 'ns')
    if method not in ('ns', 'telea'):
        raise ValueError('method must be ns or telea')
    radius = float(data.get('radius', 5))
    if not math.isfinite(radius) or radius <= 0:
        raise ValueError('radius must be finite and positive')
    result = []
    for entry in data['regions']:
        roi = entry['roi']
        if len(roi) != 4 or any(not isinstance(x, int) or isinstance(x, bool) for x in roi):
            raise ValueError('roi must contain four integers')
        x, y, w, h = roi
        if min(x, y) < 0 or min(w, h) <= 0 or x+w > width or y+h > height:
            raise ValueError('roi is outside the actual video dimensions')
        start, end = float(entry['start']), float(entry['end'])
        if not (math.isfinite(start) and math.isfinite(end) and 0 <= start < end):
            raise ValueError('region time interval must satisfy 0 <= start < end')
        mask_path = Path(entry['mask'])
        if not mask_path.is_absolute():
            mask_path = config.parent / mask_path
        mask = cv2.imread(str(mask_path), cv2.IMREAD_GRAYSCALE)
        if mask is None or mask.shape != (h, w) or not np.any(mask):
            raise ValueError('mask must be a nonempty grayscale image matching its roi size')
        mask = np.uint8(mask > 0) * 255
        # A real surrounding border is required to inpaint the masked shape.
        pad = max(12, math.ceil(radius * 4))
        xa, ya = max(0, x-pad), max(0, y-pad)
        xb, yb = min(width, x+w+pad), min(height, y+h+pad)
        local_mask = np.zeros((yb-ya, xb-xa), np.uint8)
        local_mask[y-ya:y-ya+h, x-xa:x-xa+w] = mask
        if np.all(local_mask):
            raise ValueError('mask needs unmasked surrounding pixels')
        result.append({'roi': roi, 'start': start, 'end': end, 'mask_path': str(mask_path),
                       'pixels': int(np.count_nonzero(mask)), 'bounds': (xa, ya, xb, yb), 'mask': local_mask})
    if not result:
        raise ValueError('at least one configured region is required')
    return result, method, radius

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', type=Path)
    parser.add_argument('output', type=Path)
    parser.add_argument('--config', required=True, type=Path)
    parser.add_argument('--ffmpeg', default=shutil.which('ffmpeg'))
    args = parser.parse_args()
    source, target = args.input.resolve(), args.output.resolve()
    if source == target or target.exists():
        parser.error('output must be a new path; originals are never overwritten')
    if not source.is_file() or not args.config.is_file():
        parser.error('input and config must exist')
    if not args.ffmpeg:
        parser.error('FFmpeg is required; provide --ffmpeg')
    metadata = probe(source)
    if not metadata['cfr'] or not metadata['frames']:
        parser.error('source must have verified constant frame rate and decodable frames')
    if metadata.get('first_video_seconds') is None or abs(metadata['first_video_seconds']) > .0001:
        parser.error('source video must start at timestamp zero; normalize the input timeline first')
    if metadata['has_audio'] and (metadata['audio_start_seconds'] is None or abs(metadata['audio_start_seconds']) > .001):
        parser.error('source audio must have a verified zero-start timeline; normalize input timing first')
    import cv2
    import numpy as np
    regions, method, radius = load_regions(args.config.resolve(), metadata['width'], metadata['height'])
    flag = cv2.INPAINT_NS if method == 'ns' else cv2.INPAINT_TELEA
    width, height = metadata['width'], metadata['height']
    fps = f"{metadata['fps_num']}/{metadata['fps_den']}"
    target.parent.mkdir(parents=True, exist_ok=True)
    temporary = target.with_name(target.stem + '.partial' + target.suffix)
    if temporary.exists():
        parser.error('temporary output already exists; inspect it before retrying')
    decoder = subprocess.Popen([args.ffmpeg, '-v', 'error', '-i', str(source), '-an', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], stdout=subprocess.PIPE)
    command = [args.ffmpeg, '-v', 'error', '-n', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{width}x{height}', '-r', fps, '-i', 'pipe:0', '-i', str(source), '-map', '0:v:0']
    if metadata['has_audio']:
        command += ['-map', '1:a:0', '-c:a', 'copy']
    command += ['-c:v', 'libx264', '-preset', 'fast', '-crf', '18', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', str(temporary)]
    encoder = subprocess.Popen(command, stdin=subprocess.PIPE)
    frame_size = width*height*3
    count = 0
    try:
        while True:
            raw = decoder.stdout.read(frame_size)
            if not raw:
                break
            if len(raw) != frame_size:
                raise RuntimeError('incomplete decoded frame')
            frame = np.frombuffer(raw, np.uint8).reshape(height, width, 3).copy()
            time = count * metadata['fps_den'] / metadata['fps_num']
            for region in regions:
                if region['start'] <= time < region['end']:
                    xa, ya, xb, yb = region['bounds']
                    frame[ya:yb, xa:xb] = cv2.inpaint(frame[ya:yb, xa:xb], region['mask'], radius, flag)
            encoder.stdin.write(frame.tobytes())
            count += 1
        encoder.stdin.close()
        decoder.stdout.close()
        if decoder.wait() or encoder.wait():
            raise RuntimeError('FFmpeg decode/encode failed')
    except BaseException:
        decoder.kill(); encoder.kill()
        decoder.wait(); encoder.wait()
        raise
    after = probe(temporary)
    if count != metadata['frames'] or after['frames'] != count or not after['cfr']:
        raise RuntimeError('frame count/frame rate validation failed; inspect partial output')
    if after['container_seconds'] is None or metadata['container_seconds'] is None or abs(after['container_seconds']-metadata['container_seconds']) > metadata['fps_den']/metadata['fps_num'] + .001:
        raise RuntimeError('container duration changed; inspect partial output')
    if (after['width'], after['height']) != (width, height):
        raise RuntimeError('framing dimensions changed')
    if (after['audio_sha256'], after['audio_packets']) != (metadata['audio_sha256'], metadata['audio_packets']):
        raise RuntimeError('audio packets changed; inspect partial output')
    target_report = target.with_suffix(target.suffix + '.repair.json')
    if target_report.exists():
        raise RuntimeError('report path already exists; inspect before retrying')
    temporary.rename(target)
    report = {'source': str(source), 'output': str(target), 'source_metadata': metadata, 'output_metadata': after,
              'method': method, 'radius': radius, 'audio_stream_copy_verified': True,
              'regions': [{k:v for k,v in r.items() if k not in ('mask', 'bounds')} for r in regions],
              'external_api_calls': 0, 'external_api_credits': 0, 'human_visual_review_required': True,
              'note': 'Local repair may smooth texture. Review all moving repaired regions. Visible-pixel editing makes no claim about invisible provenance.'}
    target_report.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({'output': str(target), 'report': str(target_report), 'frames': count, 'audio_identical': True}))

if __name__ == '__main__':
    main()
