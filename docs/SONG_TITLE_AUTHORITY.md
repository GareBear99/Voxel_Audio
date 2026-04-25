# Song Title Authority — v1.8.1

Voxel Audio now treats **Song name** as the public/export title and treats the source filename only as a fallback.

## Title priority

1. Manual Song name typed in the export panel.
2. Imported/bound per-track title metadata.
3. Embedded audio metadata where available:
   - MP3 ID3v2 `TIT2` title frames.
   - WAV/RIFF `INAM` title chunks.
4. Cleaned filename fallback, with extension removed and `_` / `-` converted to spaces.

## Where the canonical song title is used

- Preview canvas title.
- Browser Record video title.
- Browser Record download filename.
- Session Export Vault display name.
- FFmpeg MP4 Kit manifest.
- FFmpeg title drawtext.
- Browser Hub list labels.
- Hover cards.
- Now Playing label.
- Binding map export/import metadata.

## What still keeps the original filename

The original filename remains preserved for traceability, source-file downloads, and kit asset names when needed. It should not appear as the main public song title unless no better title exists.

## Notes

Browser File APIs do not expose OS music-library title fields directly. Voxel Audio therefore reads common embedded tags from the audio file itself where feasible, then falls back safely. Manual Song name is always the final authority.
