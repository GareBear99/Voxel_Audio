# Troubleshooting

## Blank scene

Try:

1. Clear Search.
2. Click Recenter.
3. Switch Quality to Eco or Auto.
4. Confirm Browser Hub shows visible tracks.

## Preview Export does not open

Preview requires:

- selected audio track
- bound image

## Browser Record fails

Browser Record depends on MediaRecorder and canvas capture support.

Try:

- Record: WebM
- another browser
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
