# Browser Record Playable Blob Gate — v1.8.16

This pass blocks Browser Record exports unless the app can prove the finished video blob actually plays in the current browser.

## Export gates

1. **Recorder-input audio gate** — samples the exact mixed `MediaStream` sent to `MediaRecorder`. If the recorder stream has no live audio energy, the export is blocked.
2. **Finished-blob playback gate** — loads the final recorded blob into a muted temporary `<video>`, verifies duration, seeks into the file, and confirms playback advances. If this fails, the app does not download the file and does not save it to the Vault.

## Why this exists

A non-empty MP4/WebM blob is not enough proof. Some browser recorder outputs can contain streams but still fail playback in the user's environment. This gate catches that failure before wasting a full-song render cycle.

## Chain Test

Chain Test remains diagnostic-only. It should not require artist, image, or folder input. It must pass both gates on all three runs before reporting success.

## Final output doctrine

Browser Record is still a convenience preview/export path. For release-grade uploads where compatibility matters, use **Build MP4 Kit** and render through FFmpeg.
