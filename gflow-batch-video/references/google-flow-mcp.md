# Configured Chrome route: google_flow MCP

Use this reference only when the authorized route is the installed `google_flow` Chrome browser server. If the user selects the ChatGPT in-app browser, use [browser-production.md](browser-production.md) instead. These browser sessions are distinct.

## Setup and boundary

The tested upstream is [TMSSS05/google-flow-browser-mcp](https://github.com/TMSSS05/google-flow-browser-mcp). Discover actual available server tools before use. A configured server may need a new session or application reload before its tools appear. Installation or an SDK handshake does not prove the current chat has active tools.

Keep account email, checkout location and the authorized persistent Chrome profile in **private local configuration**, not in a public skill. Use only the user's authorized profile, keep Chrome visible, and verify the intended email from visible Flow account UI. Never clone cookies, create substitute profiles or attach an unrelated debugging port. Missing/ambiguous account identity is unverified; let the user complete sign-in/2FA.

The local compatibility patch inspected in October 2026 fixed Linux/profile assumptions, cookie copying, arbitrary debugger attachment, stdout logging that corrupts MCP, and false-positive account verification. It added bounded observed-UI tools. These are local changes, not claimed upstream capabilities; review the installed checkout before relying on them.

## Capability cautions

| Tool family | Tested interpretation |
| --- | --- |
| `flow_connect`, `flow_account_check`, `flow_status` | Inspect both connection state and explicit visible-account verification. “Connected” alone is insufficient. |
| `flow_browser_state` | Preferred current-state inspection without navigation; returns control descriptors, visible text and a local screenshot. View the screenshot when needed. |
| `flow_browser_action` | Preferred bounded UI actions: navigate, click, fill, press, upload and save a browser download. Use unique, observed controls only; serialize the shared composer. |
| `flow_generate_image` | Legacy convenience helper has stale assumptions and may use private media redirect downloading. Prefer observed controls and actual reference attachment. |
| `flow_generate_video` | Tested as setup only; does not click final Generate. Parameters/reference handling can be stale. Never interpret an internal “completed” queue item as a rendered video. |
| `flow_download_latest` | May only initiate a click; does not establish a confirmed nonempty local file. Prefer a saved-download action with returned path/bytes. |
| Character/scene/grid helpers | Tool names do not prove these routes or capabilities exist in the live UI. Inspect the current app rather than assuming a saved-voice or native batch API. |
| `flow_queue_status` | Internal bookkeeping, not Flow render/concurrency evidence. |

Native preset voices are available through supported Flow UI/model modes; see [preset-voices.md](preset-voices.md). Their existence does not establish a dedicated MCP voice-lock or lip-sync endpoint. Track scenes locally and assemble with FFmpeg.

## Observed-UI action contract

Discover the installed schema; the tested local action tool accepted:

```json
{"action":"click","selector":"one uniquely observed locator","submit":true,"approved":true}
```

Use `submit:true, approved:true` only for a credit-consuming submission already authorized by the user. These flags record authorization, not create it. A clicked or `submitted_unverified` response does not prove rendering succeeded.

For `fill`, supply the complete approved prompt and inspect the composer. For `upload`, use actual existing reference files through an observed input and verify thumbnails/chips. For `download`, select the exact native-size action and confirm returned path/bytes. A menu opening or upscale request is not a completed download. Re-read menus after changes to avoid stale control indices.

Capture the actual model, Ingredients mode, selected native voice, reference attachments, aspect, supported duration, resolution, output count and credit quote before generation. Stop on login, quota, policy or rate-limit errors; inspect ambiguous submissions before retrying and preserve successes.
