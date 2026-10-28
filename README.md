# Codex Video Generation

A Codex skill for making reviewed, consistent presenter Reels in **Google Flow**: script and storyboard, native preset voice selection, reference-based scene generation, synchronized word-highlighted captions, local assembly, and visible Gemini-logo removal.

The installable skill is [`gflow-batch-video`](gflow-batch-video/SKILL.md), displayed as **Google Flow Reels Studio**. This is an independent workflow, not an official Google or OpenAI product, and it does not promise perfect identity, voice matching or generation quality.

## Demo

A finished 40-second vertical reel made with this skill: five presenter scenes, the Achernar preset voice, synchronized word-highlighted captions, and local visible-logo removal. Turn on sound to hear the presenter.

<video src="https://github.com/TangledDaunT/Codex-Video-Generation/raw/refs/heads/main/demo/gflow-reels-studio-40s.mp4" controls playsinline poster="demo/poster.jpg" width="360"></video>

[Watch or download the full 40-second demo](https://github.com/TangledDaunT/Codex-Video-Generation/raw/refs/heads/main/demo/gflow-reels-studio-40s.mp4).

## What the skill does

- Starts with a complete script and scene-by-scene storyboard for review.
- **Selects a native Flow preset voice before any video generation.** Every speaking scene receives the same actual voice ingredient plus the approved presenter image/character.
- Checks two reusable speaking clips before generating the remaining approved scenes.
- Keeps the speaking presenter visible and checks dialogue, gaze, mouth motion, anatomy, room layout and camera continuity.
- Derives caption timing from actual downloaded speech using a local aligner, then adds readable active-word highlighting.
- Assembles and verifies the final reel locally, with the visible Gemini logo repaired before delivery.
- Preserves originals, scene files, editable captions, exact prompts/settings and a private production/credit ledger.

## Install

Clone this repository and copy its skill folder into your Codex skills directory:

```bash
git clone https://github.com/TangledDaunT/Codex-Video-Generation.git
mkdir -p ~/.codex/skills
cp -R Codex-Video-Generation/gflow-batch-video ~/.codex/skills/
```

If `~/.codex/skills/gflow-batch-video` already exists, back it up and merge deliberately instead of blindly overwriting it. Reload/restart your Codex session if needed for skill discovery.

Invoke it with `$gflow-batch-video` or “Use Google Flow Reels Studio.”

## Prerequisites

1. **Google Flow access** with the required video/voice features and available credits. Availability depends on the live account, region and product controls.
2. **An authorized browser MCP.** Use the configured `google_flow` Chrome server, or the supported ChatGPT in-app browser MCP when the user chooses that route. They are distinct sessions. The skill does not bundle a browser server, credentials or cookies.
3. **Local FFmpeg** for assembly, media verification and repair. Captions need a build with libass and an appropriate font.
4. **A local speech aligner**, such as Whisper/faster-whisper, for timestamps from actual speech.
5. **Python dependencies for the optional repair helper:** `numpy`, `opencv-python-headless`, and `av`.

Use an isolated environment for local Python dependencies:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install numpy opencv-python-headless av
```

No provider API key is required by this skill's browser-based Flow workflow or local repair helper. Normal Flow account access and the user's Codex/ChatGPT account are still required.

## Example brief

```text
Use $gflow-batch-video.
Create a 40-second vertical 9:16 presenter explainer for editors.
Topic: how to use this skill with Codex.
Use my attached character references and plain English.
Choose a sweet young adult female preset voice in Google Flow.
The presenter must speak on screen throughout.
Add synchronized, word-highlighted captions.
Give me the script and storyboard first; wait for approval before generation.
```

A complete brief can include audience, outcome, duration, aspect ratio, language, character/product references, style, audio route and exclusions. The default export target is 1080 × 1920; the skill separately discloses native source resolution and any upscaling.

## Native voice consistency

The tested native workflow is **Omni Flash → Video → Ingredients → Add ingredients → Voices → preset**, with a presenter image/character attached. In a verified production, the UI called the model **Omni 1.1 Flash** and the selected default voice **Achernar — Female, soft, high pitch**. Other presets can be selected for other briefs.

A voice-only ingredient can appear disabled until an image reference is attached. The agent must inspect compatibility and enabled chips before spending credits. A voice name in a prompt is not a substitute for a real voice ingredient. The first two clips are reviewed for performance and perceptual consistency; using one preset does not guarantee every render will match perfectly.

See [preset voice instructions](gflow-batch-video/references/preset-voices.md) and Google's [current voice-reference workflow](https://support.google.com/flow/answer/16353334?hl=en).

## Local visible-logo removal

This workflow removes the visible Gemini mark from the final assembled video locally unless the user asks to retain it. It preserves the original export, audio, captions, framing and duration. A moving or duplicated mark needs its own inspected mask/time interval.

Use a small tested FFmpeg `delogo` repair on simple backgrounds, or the included explicit-mask OpenCV helper where a rectangular repair smears an edge:

```bash
.venv/bin/python gflow-batch-video/scripts/remove_visible_logo.py \
  original.mp4 final-no-logo.mp4 --config logo-regions.json \
  --ffmpeg /path/to/ffmpeg
```

You must inspect the actual footage and provide correct ROI-sized grayscale PNG masks and time ranges. The helper does not automatically detect logos. It refuses to overwrite originals/existing outputs, requires normalized zero-start audio/video, checks constant frame rate and full decoding, stream-copies audio, and verifies original/output compressed audio packet hashes. Review every repaired shot for residual marks, halos, smoothing and moving-edge artifacts.

See [configuration and QA guidance](gflow-batch-video/references/local-logo-removal.md). This edits visible pixels only; it does not remove invisible provenance or establish non-AI origin. Use it for media you are authorized to edit.

## Credits and local computation

| Operation | Accounting |
| --- | --- |
| Flow image/video generation, retries, voice previews or paid upscales | Record the live quote and actual debit/refund evidence per job. Prices vary; this repository contains no universal credit-price table. |
| Local FFmpeg/OpenCV logo repair | **Zero external API calls/credits** from the helper itself; uses local computation. |
| Local captioning and assembly | No Flow generation/API call is required; local compute/dependency costs may apply. |
| Codex/ChatGPT planning, coding and inspection | Consumes the applicable account allowance or tokens. Report per-task charges only when measurable; do not convert account-wide usage percentages into a fabricated project credit total. |

Include discarded takes and corrections in production totals. Distinguish estimates, displayed quotes and confirmed charges. Keep billing histories, token logs, project IDs, profile directories and account identifiers private.

## Files

- [`gflow-batch-video/SKILL.md`](gflow-batch-video/SKILL.md): workflow and approval boundaries.
- [`references/preset-voices.md`](gflow-batch-video/references/preset-voices.md): native preset selection and attachment gate.
- [`references/browser-production.md`](gflow-batch-video/references/browser-production.md): selected-browser operation, uploads and verified downloads.
- [`references/google-flow-mcp.md`](gflow-batch-video/references/google-flow-mcp.md): configured Chrome MCP cautions.
- [`references/storytelling-motion.md`](gflow-batch-video/references/storytelling-motion.md): useful hooks, shot planning and motion QA.
- [`references/local-logo-removal.md`](gflow-batch-video/references/local-logo-removal.md): local finishing procedure.
- [`scripts/remove_visible_logo.py`](gflow-batch-video/scripts/remove_visible_logo.py): explicit-mask local repair helper.

## Limitations and privacy

Live UI controls are authoritative. Tool names do not establish a native batch API, saved-voice endpoint, automatic stitcher or supported setting. Stop on login, quota or policy blocks; inspect ambiguous submissions before retrying. Transcripts and still samples do not prove a perceptual voice/lip-sync match: when the agent cannot listen directly, obtain human playback review and disclose the limit.

This repository contains reusable instructions and code, plus the approved public demo linked above. It excludes personal profiles, account emails, private project URLs, usage logs and other production media. Keep local account configuration outside this public repository. Human checkpoints remain script/storyboard review, reference/two-clip voice review, and final-cut review.

Licensed under [MIT](LICENSE).
