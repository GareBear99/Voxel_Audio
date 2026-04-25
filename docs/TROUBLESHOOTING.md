# Troubleshooting

## Laggy render / weak hardware

Try:

1. Switch `Quality` to `Eco`.
2. Hide the Browser Hub with `Hub`.
3. Use Voxel Icon view instead of Web Node view.
4. Clear Search or focus a smaller folder.
5. Keep browser zoom near 100%.
6. Close extra browser tabs using canvas/audio.
7. Use Build MP4 Kit instead of full Browser Record for final output.

## Audio and visuals feel out of sync

Try:

1. Pause and play once to resume the Web Audio context cleanly.
2. Switch to Eco so the renderer stops starving audio analysis.
3. Avoid High mode on weak hardware.
4. Use FFmpeg Kit for final output because it renders deterministically outside the live browser render loop.

## Blank scene

Try:

1. Clear Search.
2. Click Recenter.
3. Switch Quality to Eco or Auto.
4. Confirm Browser Hub shows visible tracks.
5. Click Reset if you want a full startup-state rebuild.

## Preview Export does not open

Preview requires:

- selected playable audio track
- bound image
- Artist name

## Browser Record fails

Browser Record depends on MediaRecorder and canvas capture support.

Try:

- Record: WebM
- another current browser
- Download Run Log
- use Build MP4 Kit instead

## MP4 kit script fails

Check:

- all kit files are in one folder
- FFmpeg is installed
- filenames in manifest match downloaded filenames
- run script from a terminal for full FFmpeg output

## Album render fails

Check:

- all audio and cover files are in one folder
- fallback cover exists if some tracks have no image
- concat list is generated
- FFmpeg is installed

## Admin unlock does not persist

The local admin unlock uses browser `localStorage`. It can be cleared by private browsing, site-data cleanup, different browser profiles, or different local origins.
