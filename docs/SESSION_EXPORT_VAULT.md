# Session Export Vault

Voxel Audio keeps the last 9 browser Record exports in memory during the current page session.

## Why

Some browsers can hide, miss, or interrupt the first download prompt at the end of a MediaRecorder stream. The Session Export Vault prevents a successful export from disappearing immediately.

## Behavior

- Stores the last 9 browser Record exports.
- Provides a Download button for each export.
- Stores exports in memory only.
- Clears when the page is closed or reloaded.
- Does not upload files anywhere.

## Applies to

- 10s Record.
- Record Full.

## Does not apply to

- FFmpeg Kit files.
- Album Kit source files.

Those are still downloaded as individual generated files.
