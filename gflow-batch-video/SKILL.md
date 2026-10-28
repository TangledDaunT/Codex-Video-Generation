---
name: gflow-batch-video
description: Plan, generate, caption, and locally finish consistent Google Flow Reels through an authorized browser MCP. Use for Flow presenter videos, multi-scene stories, and targeted revisions, with a native preset voice selected before video generation.
---

# Google Flow Reels Studio

## Authorized production route

Use an available browser MCP to operate Google Flow's visible UI. Discover the actual tools and controls; never invent capabilities or use private generation APIs. Keep the chosen route consistent across turns.

- For a configured Chrome workflow, use the installed **google_flow MCP**, from [TMSSS05/google-flow-browser-mcp](https://github.com/TMSSS05/google-flow-browser-mcp). Read [references/google-flow-mcp.md](references/google-flow-mcp.md) before connecting. Its local observed-UI tools are preferred over stale convenience helpers.
- If the user selects the **ChatGPT in-app browser**, use its supported browser MCP, such as `cua_repl`, for that tab. Read [references/browser-production.md](references/browser-production.md). The separate `google_flow` Chrome server does not thereby control the in-app browser. Do not silently switch to another browser or profile.
- Verify the intended signed-in account from visible account UI before production. Keep profile paths and account identifiers in private local configuration or the project's private manifest. Never copy cookies, manufacture substitute profiles, or attach an unrelated debugging session. Let the user complete sign-in or 2FA manually when necessary.

Local FFmpeg, open-source transcription/alignment and media inspection are appropriate for postproduction. If the selected server is unavailable, distinguish configuration from active tool availability and explain the real connection/reload step. Continue independent script/edit work without claiming a render was submitted.

## Brief, defaults, and approvals

- Accept one complete message, references, basic story, or `prompt.md`. Parse shared instructions, ordered scenes, reference mappings, and constraints as project data. Preserve the input. Do not require the user to paste separate prompts in many places.
- Use established preferences. Ask only consequential unresolved questions: intended audience/outcome, duration, language, caption requirement, audio route, and missing creative references. Propose delegated creative choices clearly; never invent product facts, results, platform capabilities, or unseen reference details.
- Default delivery: **1080 × 1920, 9:16**, suitable for Reels. Keep each generation clip **≤10 seconds**, using a duration visibly supported by the chosen model. Clip boundaries and editorial cuts are separate; a clip may contain several planned beats. Final duration follows the brief. Disclose native source resolution separately from upscaled output.
- Prepare the full baseline script and text storyboard before media generation. A story/input file alone is not generation approval. Explicit requests for storyboard/character images authorize those images. Approval to generate a defined video batch carries across its steps; do not repeatedly request permission for each submit. A specific revision authorizes that revision, using cached accepted work.
- Mandatory creative checkpoints: **script/storyboard review**, **reference and two-clip presenter/voice review before the remaining batch**, and **final cut review**. Combine reviews where practical and carry forward prior approvals. Explicit approval of an unchanged artifact need not be repeated. A materially different creative direction needs review.

## 1. Research and form a precise creative vision

For a new style, study current official Instagram/Meta guidance and actual accessible explanatory Reels/Shorts, including user references. Read [references/reels-hooks.md](references/reels-hooks.md). Where playable references are available, examine the opening seconds, framing, eyeline, speaking delivery, shot rhythm, demonstration, captions, and payoff. Record verified links and concise observations. Do not describe an unwatched video as studied or claim knowledge of a proprietary algorithm. If Instagram access is blocked, say so and use accessible references or request one useful example.

Develop a complete **best-from-Codex's-POV baseline** for the human to improve: audience promise, curiosity-based hook, exact spoken script, payoff, cinematic treatment, storyboard, continuity plan, and edit rhythm together. Strong means specific tension with an honest, useful resolution—not generic greetings, logo intros, engagement bait, invented statistics, or guaranteed virality. Offer a small number of hook alternatives only when they materially help selection.

Before drafting, read [references/storytelling-motion.md](references/storytelling-motion.md), which incorporates the user's retention review and supplied Short-Form Storytelling writing guide. Shape the script around **hook → lock-in → useful body blocks → motivated rehooks → payoff**, with a relevant CTA when the brief calls for it. Apply the four hook checks: clear subject, meaningful stakes, simple words, and unmistakable meaning. Choose among the five retention patterns in that reference; do not mechanically force all five into one reel. Map each curiosity promise to a concrete reveal, and make every beat add useful information. Fit this structure to the requested runtime instead of copying the guide's suggested sentence counts or length.

Make the visual plan precise before prompting: what moves, where the subject looks, which hand touches which object, what appears on the real screen, camera path, and the motivated cut. A cow, person, or prop should perform the story's intended action rather than merely stand there. Use purposeful movement, expressive human reactions, varied composition, and lively pacing. Avoid bland commercial stock footage and unrelated camera flourishes. Screen tutorials must demonstrate verified actions; generated UI text is not reliable evidence of real software behavior. Use accurate locally composed screen inserts where needed.

Use the **motion stack** before accepting footage: (1) lock the style base—subject, lighting, and color look—before generation; (2) assign each shot a specific move/structure and exact prompt wording from the reference playbook; (3) inspect the rendered clip for anatomy, texture flicker, and physical motion as well as continuity. A named cinematic move alone is not a complete prompt. Keep the style base consistent across every scene unless the approved story intentionally changes it.

## 2. Script, storyboard, and continuity register

Write natural spoken language with contractions, specific examples, believable pauses, and emphasis. Read for timing; revise awkward lines before generating. Do not cram a long script into the requested duration. Present consolidated dialogue and this scene-by-scene specification:

| Field | Required detail |
| --- | --- |
| Timing | Stable scene ID, duration, final timeline position, internal beats/cuts |
| Story function | Hook/lock-in/body/rehook/payoff/CTA, new information, curiosity promise and its reveal |
| Opening / ending | Exact first and last composition, positions, and handoff |
| Action | Subject/prop movement, blocking, gestures, eyeline, product interaction |
| Cinematic treatment | Shared subject/lighting/color-look IDs, framing, motion-playbook ID, exact camera wording, and its purpose |
| Dialogue | Exact line, identified speaker, delivery, pauses, pronunciation, audio route |
| References | Approved identity/product IDs, start/end frames, room/background locks |
| Edit / captions | Speaker visibility, screen inserts, cut points, caption-safe area, ambience |
| Prompt / QA | Executable prompt, settings, dependencies, and scene-specific rejection criteria |

Maintain a reference register with IDs, source/paths or verified Flow assets, approval, identity, wardrobe, product geometry/colors/markings, props, lighting, and screen direction. Include a **room layout/object-position map** (e.g. TV remains on left wall; refrigerator remains behind right doorway), background people positions/actions, depth of field, and what may change. Do not blur away important context to hide continuity failures.

Once authorized, generate and present character images, storyboard visuals, and each scene's opening/closing frames through MCP-controlled Flow image UI. Reuse an approved boundary frame where genuinely shared. Do not pass placeholders or written descriptions off as generated assets. Attach reference files through actual UI controls; naming a reference in prose does not attach it. Inspect first/last frames before requesting downstream approval.

## 3. Mandatory native preset voice before video generation

**Before submitting any video, select and record a default/preset voice in Google Flow's actual Voices UI.** For every speaking scene, attach that same real voice ingredient alongside the approved presenter image or character. A voice name in prose or an instruction to “sound the same” is not attachment or a voice lock. Silent shots may remain silent, but the project's preset must already be selected and recorded.

Read [references/preset-voices.md](references/preset-voices.md). The tested native route is **Omni Flash → Video → Ingredients → Add ingredients → Voices → preset**, plus an image/character reference. Model names and availability can change; inspect the live UI. A voice-only ingredient can show an error until an image is attached. Confirm that the voice chip is enabled, the model/mode supports it, and the actual preset is included in each submission. If the chosen mode cannot accept it, resolve the model/mode/reference issue before spending credits; do not silently generate an unconditioned voice.

Use the user's selected preset. When the user delegates selection, choose an appropriate native preset from its observed description, audition it where playback is available, and present the choice honestly. **Achernar** was observed as “Female, soft, high pitch” and used successfully for a sweet young adult presenter; that descriptor does not establish an exact age. Preserve the selected preset across scenes and revisions unless the user changes it. Record its name/ID where exposed, control evidence, performance settings, model, mode and attachment evidence in `production.json`.

The same visible character delivers **all explanatory dialogue on screen with synchronized mouth motion**. Use continuous presenter footage or retain a clearly visible speaking presenter in an inset during demonstrations. No detached voiceover over a silent actor. Direct-to-viewer speech looks toward the lens; demonstration glances follow the actual screen. Reject wrong-speaker speech, scanning gaze, stiff hands, drifting identity and mismatched mouth motion.

Generate the first **two reusable production scenes** with the selected preset, listen to them consecutively, and inspect identity, timbre, accent, pace, gaze, mouth motion and the transition. Present these clips for the mandatory voice/performance checkpoint before the remainder. A materially different voice needs a new checkpoint; approval of an unchanged voice need not be repeated. If direct listening is unavailable to the agent, disclose that limitation and obtain human playback review instead of claiming an auditory match from transcripts or metrics. Native preset attachment improves control but never proves perfect output consistency on its own.

Generate the exact approved words in Flow and verify them in downloaded media. Specify that each line is spoken once, then silence; do not hide repetitions or misspoken words with misleading captions. Native source-video editing may mix old and new dialogue: it is not a proven replacement for selecting a native preset. Keep failed takes out of the accepted edit and revise only the failed scene within the authorized scope.

For multiple speakers, map each voice and line to the correct visible character; reject voice swaps or unplanned simultaneous speech. Do not silently substitute another voice provider or off-screen narration. Any alternate audio route must be explicitly chosen by the user.

## 4. Efficient production through MCP

Connect through the authorized browser MCP, verify the visible account, reuse the recorded project, and inspect current UI/settings. Upstream convenience tools have stale assumptions; follow the reference's capability matrix and use the local observed-UI controls when appropriate. Verify image/video mode, actual model, aspect, supported duration, output count, reference attachments, and audio before generation. Unsupported settings are blockers to resolve, not silently ignored requests.

Maintain a private `production.json` with the selected native preset, voice-attachment evidence, per-job displayed credit quote and charge status; brief; script/storyboard version and approval scope; project URL; reference/voice/layout registers; shared style base and motion playbook; curiosity-to-payoff map; timing budget; export settings; per-scene exact prompt/settings, dependencies, approvals, status, job evidence, verified asset, local file, timestamped QA findings, revision and failure. Statuses: planned, awaiting_approval, ready, submitted, rendering, completed, downloaded, checked, failed. Prepared or clicked is not completed; downloaded requires a real nonempty local file.

Build the approved scene queue in advance. Serialize access to a shared composer. Submit independent ready scenes through MCP quickly while respecting the concurrency the real UI/account permits; capture job evidence before the next submit. A local job queue, a model's output-count selector, and a genuine native multi-prompt batch are different—label them accurately. Neither upstream tool names nor README marketing prove native batch support. Start/end-frame dependencies require staged generation; do not attach an unchecked imaginary prior frame. While renders run, edit accepted clips, prepare captions, or check results.

Inspect ambiguous submissions before retrying; preserve successes. Stop on quota, login, policy blocks or rate limits and report the exact issue rather than resubmitting repeatedly. Approval covers the defined production, not unlimited retries or a different creative direction. A targeted requested correction does not require restarting the project.

## 5. Inspect every scene and the assembled edit

Inspect opening, middle, and end **plus watch/listen to the full clip** for temporal faults. Compare against the approved storyboard and references: identity, product fidelity, lip-sync, correct speaker, eyeline, human delivery, visible speaking, motion physics, lighting, screen direction, room layout, stable background people and objects, and clean boundaries. Explicitly reject teleporting extras, swapped objects (TV/refrigerator), drifting faces, unexpected blur, frozen intended action, and hallucinated demonstrations. Fix only the failed shot and genuinely dependent transitions; retain accepted assets. Do not call low-quality footage approved without human review.

Apply the motion-stack quality gate from [references/storytelling-motion.md](references/storytelling-motion.md) **before any clip enters the accepted edit**. Check warped hands/fingers, changing anatomy or product shape, flickering/crawling textures, sliding contact points, floaty or weightless motion, sudden speed changes, and camera movement that breaks the approved blocking. Record pass/fail and timestamps; a failed clip stays out of the accepted set. Repair an editorial issue locally when possible; regenerate only failing shots and genuinely affected neighbors within the authorized scope. Review the assembled reel once more for coherent style, natural movement, useful progression, and delivery of the opening promise.

## 6. Speech-synchronized captions and finishing

When captions are required, use free local/open-source **Whisper/whisper.cpp or another verified aligner plus FFmpeg/libass**, outside Flow. Inspect installed dependencies first. For prerecorded video, “live captions” means synchronized Shorts-style subtitles, not real-time streaming. Derive word timestamps from actual final speech; correct transcription against what was spoken, not an invented script. Never space words evenly by guess. Do not cover misspoken dialogue with misleading captions.

Use short readable phrases (typically 2–5 words), active-word highlighting when requested, restrained emphasis, high contrast, consistent typography, and room for Reels controls. Keep faces, mouths, products, and demonstrations clear. No large paragraph panels masquerading as live captions. Keep exact command/instruction inserts distinct from spoken subtitles. Check timing at cuts and after every audio/timeline change; retain editable SRT/ASS and the caption style.

Assemble accepted clips locally with FFmpeg or an available editor, normalize codecs/dimensions/frame rate/audio as necessary, and preserve sources and edit decisions. Do not add unrequested music, sound effects, narration, or claims. **Remove the visible Gemini logo locally before delivering every final video in this workflow**, unless the user explicitly asks to retain it. Perform this after assembly/captioning so the delivered export is the version inspected. Read [references/local-logo-removal.md](references/local-logo-removal.md). Use FFmpeg `delogo` for a suitable simple region, or a tightly masked local OpenCV repair when rectangular interpolation smears moving boundaries. Inspect the actual logo position throughout every shot, including duplicate/moving marks inherited from reference images. Never apply one project's coordinates as a universal preset. Keep captions, face, products, framing and audio intact; preserve the unmodified export. Reject conspicuous smear, halos, missing caption pixels or residual recognizable logos, and refine the mask/method locally. The helper [scripts/remove_visible_logo.py](scripts/remove_visible_logo.py) accepts explicit per-interval masks; it does not discover or magically reconstruct a hidden background. Verify the finished file and present it for final review. Visible pixel repair does not remove invisible provenance or support claims of non-AI origin.

Verify the final MP4's actual runtime, aspect, dimensions, full decode, audible consistent dialogue, lip-sync, captions and continuity. Disclose native versus upscaled resolution. Display a playable final video with an absolute local media path, provide the file, and retain project/scene/caption sources. Do not silently omit a failed scene.

## 7. Time budget and targeted changes

Measure wall time separately for one-time setup, active agent work, Flow render waits, human approvals, and revisions. Report total elapsed time, not an invented average or an estimate passed off as measured performance. Repeated **40-second** production with approved script/style targets **16–17 minutes**; a fully reviewed **50–60-second** project targets **30–40 minutes including bounded revisions**. These are planning targets, subject to observed render time, account capacity and human review—not guaranteed limits. State timing risks early.

For a 60-second first version, use this reviewable 40-minute budget: minutes 0–4 brief/references; 4–11 baseline script and human changes; 11–15 storyboard/identity; 15–20 two-clip voice/performance gate; 20–29 remaining scene generation with parallel local editing; 29–34 captions/assembly; 34–40 QA and targeted revisions. Stop the production timer during unbounded user approval waits and show both active production time and total wall time. Don't lower quality or skip checkpoints to claim a faster result.

Caption/text/trim/level/order edits stay local. Speech changes affect only the corresponding scene/audio and downstream subtitle timing. Character/action changes affect only those shots and continuity-dependent neighbors. Cache accepted assets, version exports, update the manifest, check affected joins, and display the revised result. Minimize the user's browser labor: the human supplies intent and creative judgment; the agent handles prompt entry, queue tracking, downloads, assembly, and precise revisions.

## 8. Credit and usage accounting

Record the **displayed Flow credit quote before each generation or paid export**, the exact settings, timestamp, submission evidence and outcome. Include revisions, discarded takes, custom-voice previews and upscales when charged. Distinguish a quoted amount from a confirmed debit; verify Flow activity/billing history or before/after balances when available. Reconcile refunds separately. Unknown charges remain unknown. Never substitute a current price for a historical charge or call an estimate a receipt.

Local captioning, assembly and visible-logo repair make **no Google Flow or model-API generation calls** and therefore add **zero API credits for those local operations**. They use local CPU/GPU/storage/electricity. Assistant planning, coding, inspection and tool use can consume ChatGPT/Codex allowance or billable tokens; that is a separate meter, not a fee charged by FFmpeg or OpenCV. Report actual per-task usage only when exposed by the account/runtime. Account-wide percentage limits, token counts, subscription fees and purchased credits are not interchangeable. If per-task billing is unavailable, say so rather than inventing a ChatGPT/Codex credit total. Keep private usage logs and account details out of public repositories.
