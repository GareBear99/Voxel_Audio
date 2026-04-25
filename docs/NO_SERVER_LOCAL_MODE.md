# No-Server Local Mode

Voxel Audio is designed to run as a local single-file app.

## Run without a server

Double-click:

```text
index.html
```

or use your browser's File → Open menu.

## Why this matters

The app does not need:

- a backend
- a database
- cloud upload
- account login
- npm install
- build step

## Local features

The following work locally:

- folder picker
- drag/drop folder loading
- audio playback
- Web Audio analysis
- voxel visualization
- image binding
- live export preview
- browser record export
- FFmpeg kit generation
- album route kit generation

## Browser limitations

Browsers may treat `file://` pages differently.

If drag/drop folder behavior is inconsistent, use **Open Audio Folder**.

If Browser Record fails, use **Download Run Log** and then use **Build MP4 Kit** for final output.
