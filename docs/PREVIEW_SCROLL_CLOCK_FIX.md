# Preview Scroll Clock Fix — v1.8.6

This release fixes the small side metadata line in **Live Export Preview**.

## Root cause

The side metadata scroll function depends on a stable `startedAt` timestamp.

The preview loop was incorrectly passing `performance.now()` every frame:

`renderExportVideoFrame(..., performance.now())`

That reset the scroll timer continuously, so the text always looked stuck at the beginning instead of moving.

## Fixed

- Added a persistent `previewStartWall` clock for Live Export Preview.
- The clock starts when preview opens.
- The clock resets only if the preview track changes.
- The small metadata line now visibly:
  - pauses,
  - scrolls right-to-left,
  - pauses at the end,
  - restarts.

## Explicitly unchanged

- The large main title is untouched.
- Only the small `VOXEL AUDIO EXPORT • song • artist/feat` line behavior was corrected.
