# Vault Audio Re-export Stability Fix

This pass fixes the silent-audio failure that could happen after the first Browser Record export was saved in the Session Export Vault.

## Fixed
- Recorder audio tracks are cloned before being passed to `MediaRecorder`.
- Recorder cleanup now stops only the recorder-owned cloned tracks and export canvas video tracks.
- The original `<audio>` capture stream and WebAudio graph are not stopped during export cleanup.
- WebAudio fallback export destinations are created fresh per export and disconnected after use.
- Export waits for media metadata/canplay before building the recorder stream.
- Normal playback `audio.onended` handler is restored after export/cancel/failure.
- Vault re-export keeps the correct 10s/full duration instead of relying on unsafe operator precedence.
- Feat metadata is capped to 36 characters, matching Artist cap behavior.

## Validation
- `node scripts/extract-app-js.js`
- `node --check app.extracted.js`

