# Production Hardening Pass — v1.8.16

## Goal

Make Voxel Audio smoother on weak hardware without destroying the visual identity or the local-first production workflow.

## Runtime changes

- Added `Quality: Lite`.
- Added adaptive quality order: `Lite → Eco → Auto → High`.
- Added a performance governor that measures scene draw cost and automatically lowers quality when the frame budget is repeatedly missed.
- Added static background caching so the radial gradient and grid are not rebuilt every frame.
- Added hidden-tab drawing skip.
- Added debounced resize handling.
- Added Web Node link/node draw caps tied to the active quality mode.
- Added label suppression in lower modes.
- Added throttled floating artwork transforms in Lite/Eco.
- Lowered analyser and waveform density in Lite.
- Kept audio timing anchored to the HTML audio element.

## Why this is production-grade for the local build

The app now has a clear runtime ladder:

| Layer | Purpose |
|---|---|
| Lite | Maximum survival mode for old Macs and screen recording on weak machines. |
| Eco | Low-cost editing/default weak-hardware mode. |
| Auto | Balanced normal mode. |
| High | Visual inspection mode for stronger machines. |
| FFmpeg Kit | Deterministic final-output route independent of browser capture speed. |

## Remaining non-local production work

The following are intentionally not solved inside a single HTML file:

- Google OAuth account login.
- Stripe billing.
- Server-side quota enforcement.
- Secure no-watermark entitlement validation.
- Server FFmpeg render workers.
- Hosted storage/download links.
- Abuse and rate-limit protection.
- Terms/privacy/commercial deployment pages.

## Validation performed

- Extracted the application script from `index.html`.
- Ran `node --check app.extracted.js`.
- Result: pass.
