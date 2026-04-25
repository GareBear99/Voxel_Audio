# Local Reliability Patch

This patch adds a fixed Quick Dock and startup self-test.

## Why

A no-server single-page app must keep critical actions visible even if the browser window is narrow, zoomed, or the topbar overflows.

## Quick Dock

The Quick Dock stays visible and provides:

- Open folder
- Bind image
- Open info docs
- Preview export
- Browser record
- Build MP4 kit
- Album route builder

## Startup diagnostic

On load, Voxel Audio checks for:

- file inputs
- info overlay
- preview/export buttons
- File API
- Web Audio
- Canvas

If something is missing, it reports it onscreen instead of failing silently.
