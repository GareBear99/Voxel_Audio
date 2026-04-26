# Vault Repeat Export Audio Fix v1.8.12

## Problem
After one Browser Record export was saved in the Session Export Vault, later exports could produce video with no audio.

## Root Cause
The previous recorder cleanup stopped every track in the mixed MediaRecorder stream:

```js
mixed.getTracks().forEach(t => t.stop())
```

That mixed stream included the real audio capture track from `<audio>.captureStream()` or the WebAudio `MediaStreamDestination`. Stopping that source track can poison the reusable audio pipeline for the next export/re-export.

## Fix
- The recorder now clones audio tracks before MediaRecorder receives them.
- Cleanup only stops recorder-owned cloned audio tracks and canvas video tracks.
- The original audio capture stream is never stopped by export cleanup.
- WebAudio export destinations are created fresh per export and old destinations are disconnected.
- Export waits for audio metadata/canplay before creating the recorder stream.
- The normal `audio.onended` handler is restored after export/cancel/failure.
- Added `Chain Test`, which performs three short repeat exports back-to-back to catch repeat-export silence without waiting for a full-song render.

## Validation
Static validation:

```bash
node scripts/extract-app-js.js
node --check app.extracted.js
```

Manual validation path:
1. Load folder.
2. Select song.
3. Bind image.
4. Enter Artist.
5. Press `Chain Test`.
6. Play the 2nd and 3rd exported files from downloads/Vault.
7. Only after those have audio, run `Record Full`.
