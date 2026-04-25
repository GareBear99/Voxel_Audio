# MP4 Direct Audio Restore — v1.8.10

This release restores Browser Record MP4 as an option and changes the audio capture order.

## Problem

Uploaded Browser Record MP4 files were confirmed with `ffprobe` to contain:

- H.264 video
- no audio stream

That means the browser accepted MP4 recording but silently dropped the audio during muxing.

## Why this patch

The previous audio path preferred WebAudio `MediaStreamDestination`. Some browser MP4 MediaRecorder implementations are unstable with that route.

This version prefers direct `<audio>.captureStream()` first, then falls back to WebAudio only if direct capture is unavailable.

## Changed

- Browser Record MP4 is restored.
- `getReliableExportAudioStream()` now tries direct audio element capture first.
- Mixed recorder stream is checked before recording starts.
- Export run log now records video/audio track counts and capture source.
- If there are zero audio tracks before recording starts, export aborts instead of silently creating a broken file.

## Important

If your browser still outputs MP4 with no audio stream even though the mixed stream has audio tracks, that is a browser MediaRecorder MP4 muxing bug. In that case:

- use WebM for local Browser Record, or
- use Build MP4 Kit for final MP4 with audio.

## Untouched

- Main title rendering
- Side metadata scroll
- Visual layout
