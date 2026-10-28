# Native Flow preset voice gate

Read before the first video submission and whenever the requested voice/model changes.

## Verified native workflow

Google's [Create videos in Flow](https://support.google.com/flow/answer/16353334?hl=en) documents voice references for **Omni Flash → Video → Ingredients**. Add a single-speaker reference from **Add ingredients → Voices**. The [model feature guide](https://support.google.com/flow/answer/16352836?hl=en) describes native preset/custom-voice support. Availability, names, pricing and controls can vary by region/account and change over time; the actual UI is authoritative.

Observed on 2026-10-28: **Omni 1.1 Flash**, Ingredients, vertical 9:16, 720p, 8 seconds, one output, with the same **Achernar** preset plus approved presenter images, produced speaking presenter clips. Achernar's catalog description was “Female, soft, high pitch.” The voice chip showed an error when no presenter image was attached, then became enabled with an image reference. This is an observed compatibility requirement, not a promise of absolute identity across independent renders.

## Required checks

- Select the native preset in the real Voices UI **before any video generation**. Record its observed name/ID, description and evidence. Use the user's choice, or choose a suitable default when delegated.
- Preview the preset if playback is available. Do not claim an audition or direct listening when only text, waveforms or automatic transcription are available. A label such as “youthful” or “soft” does not prove an exact age.
- Attach the actual same preset to **each speaking generation**, together with the correct presenter image/character references. Confirm model/mode support and an enabled voice ingredient, then record attachment evidence before submit. No prompt-only “same voice” substitute.
- Keep native timbre/accent stable; specify only the desired delivery, pace, warmth and pauses. Record any native performance settings. Customizing and saving a variant is an optional user-selected direction, not required to use a default preset.
- Generate exact approved lines once. Avoid filling spare seconds with repeated words. Verify the downloaded speech. Correct harmless orthographic transcription errors; never caption over an actual spoken mistake.
- Review two reusable clips consecutively for timbre, pitch, accent, pace, identity, gaze, mouth synchronization and natural performance. Obtain the human checkpoint before the remainder. If the user changes the voice, use the new preset and redo the affected checkpoint; retain all unaffected accepted work.

A native edit of an existing speaking clip is not equivalent to a saved preset. A tested source-video edit mixed old and replacement dialogue. Keep such failures out of the accepted set, and do not repeatedly spend credits trying an unsupported voice-preservation route.

## Private manifest fields

Record `voice.preset_name`, `voice.preset_id` when exposed, `voice.catalog_description`, `voice.model`, `voice.mode`, `voice.performance_settings`, `voice.selection_evidence`, per-scene `voice_attachment_evidence`, the two-clip approval and subsequent human feedback. Keep exact job prompts/settings, quote/debit evidence and original media separately. Do not publish account IDs or private project URLs with a reusable skill.
