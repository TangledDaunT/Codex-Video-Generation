# Local visible Gemini-logo removal

Remove the visible Gemini mark from the **final assembled export** before delivery in this workflow, unless the user requests retention. Preserve the original export and all accepted source clips. This edits visible pixels only, not invisible provenance or media origin.

## Inspect and choose a local method

Inspect every scene's opening/middle/ending and moving regions at full size. A native fixed-corner mark and a second moving mark inherited from a generated reference can coexist. Record their coordinates and time ranges; coordinates from another project are not defaults.

- A small FFmpeg `delogo` rectangle can work on a simple background. Test it before accepting the whole video. Reject conspicuous rectangular smoothing, edge smears, remaining sparkle outlines and damaged captions.
- For difficult boundaries, use a tight grayscale mask and local OpenCV inpainting. White mask pixels identify the logo; black pixels preserve source content. Expand the mask enough to cover antialiased edges/halos, but keep it clear of faces, captions and important product geometry. Use separate per-interval masks for duplicate/moving marks and inspect their entire paths.
- The bundled `scripts/remove_visible_logo.py` implements an explicit-mask local repair with FFmpeg decode/encode, OpenCV and a machine-readable QA report. It **does not find logos or design masks automatically**. Inspect/adapt the masks first. Inpainting can soften texture and cannot guarantee reconstruction of occluded detail.

Local removal makes no Flow generation request and no external model/API call. FFmpeg/OpenCV processing uses local computation, not API credits. Assistant work around the operation may still consume the user's ChatGPT/Codex allowance or tokens; do not invent per-action credit equivalents.

## Helper configuration

Install Python dependencies in an isolated environment: `numpy`, `opencv-python-headless`, and `av`. Supply an installed FFmpeg executable through `--ffmpeg` if it is not on PATH.

The JSON configuration has `regions`, an array of objects with:

- `roi`: `[x, y, width, height]` measured against this video's actual frame dimensions.
- `mask`: path to a grayscale PNG of exactly the ROI's size, relative to the configuration file or absolute.
- `start`, `end`: seconds, with start inclusive and end exclusive.

Optional top-level fields: `method` (`ns` or `telea`) and `radius` (positive local inpainting radius). Different scene intervals may use different ROIs/masks. If marks move, a tightly inspected mask covering their full path can work; otherwise prepare per-interval masks. Never mask a broad area merely to conceal an inspection failure.

```bash
python scripts/remove_visible_logo.py original.mp4 final-no-logo.mp4 \
  --config logo-regions.json --ffmpeg /path/to/ffmpeg
```

The helper refuses to overwrite the input or an existing output. It requires a verified zero-start, constant-frame-rate source video/audio timeline, checks frame timestamps, copies the original audio stream, and writes a JSON report beside the output. Test on a short representative portion before processing long media.

## Required final QA

Decode the full output and verify actual duration, dimensions, frame rate and all frames. Compare original/output compressed audio packet hashes when stream-copy is used. Review repaired areas through motion, scene boundaries and the most difficult skin/desk/floor/product edges. Confirm captions, framing and speaker mouth remain intact and no recognizable Gemini mark remains in reviewed regions. Record any residual texture smoothing honestly; refine only failed regions. Deliver the repaired playable file with the original retained. Do not claim perfect background reconstruction, invisible-provenance removal or non-AI origin.
