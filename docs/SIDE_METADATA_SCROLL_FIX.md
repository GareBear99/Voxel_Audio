# Side Metadata Scroll Fix — v1.8.5

This release fixes only the small side metadata text line in the export renderer.

## Fixed

- The `VOXEL AUDIO EXPORT • song • artist/feat` line is now clipped into a safe scrolling lane.
- Long artist/feat text can no longer run into the reactive circle.
- The metadata lane pauses, scrolls to the end, pauses, then restarts.
- No duplicate ghost copy is drawn.
- No title rendering behavior is changed.

## Explicitly untouched

- The main large Song title remains the restored v1.8.4/v1.8.1 behavior.
- No title marquee was added.
- No title safe-box shrink was added.
- No title fade mask was added.
