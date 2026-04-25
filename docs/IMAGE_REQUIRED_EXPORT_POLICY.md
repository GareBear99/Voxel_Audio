# Image Required Export Policy

Voxel Audio blocks export actions unless the selected track has bound artwork.

## Required before export

For single-track workflows:

1. Select or play a song.
2. Bind an image with **Bind Image To Selected** or drop an image onto the song voxel.
3. Confirm the floating image appears for that selected song.
4. Then use:
   - Preview Export
   - 10s Record
   - Record Full
   - Build MP4 Kit

## Why

The current release workflow is artwork-first. A valid visual export must include the image/cover floating with the selected single.

## Browser Record

Browser Record requires bound artwork.

If artwork is missing, the action is blocked and the app shows an `IMAGE_REQUIRED` message.

## MP4 Kit

MP4 Kit requires the original image file so the generated FFmpeg kit can download the cover source.

If only metadata exists from an imported binding map, rebind the image file first.

## Album Route

Album export requires either:

- every routed track has bound artwork, or
- a fallback album cover is set from the current selected track.

Without artwork coverage, album export is blocked.
