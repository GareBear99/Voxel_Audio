# Operator Manual

## Basic session

1. Open `index.html` or serve with `python3 -m http.server 8080`.
2. Click `Open Audio Folder`.
3. Click a voxel or row to play a track.
4. Bind artwork with `Bind Image To Selected` or drag an image onto a voxel.
5. Enter Artist name before export.
6. Use `Preview Export` to verify layout.
7. Use `10s Record` for a quick browser sample.
8. Use `Build MP4 Kit` for final production output.

## Controls

| Control | Meaning |
|---|---|
| Open Audio Folder | Loads playable audio files from a folder tree. |
| Search | Filters visible voxels and Browser Hub rows. |
| Bind Image To Selected | Attaches cover art to the selected/current track. |
| Play | Plays or pauses the current track. |
| Back | Backs out of panels/focus/search/selection/zoom without deleting loaded audio. |
| Reset | Clears the active session and returns to startup/demo state. |
| Recenter | Fits the visible voxel scene back into view. |
| Quality | Cycles Lite / Eco / Auto / High. Lite is the weakest-hardware mode. |
| Hub | Shows or hides the Browser Hub. |
| Preview Export | Opens final-layout preview. |
| 10s Record | Records a quick browser preview. |
| Record Full | Records the selected full song in browser. |
| Build MP4 Kit | Downloads deterministic FFmpeg render assets/scripts. |
| Album Route | Builds a multi-track album route kit. |
| Vault | Shows completed Browser Record outputs from the current session. |

## Required before export

Single-track Preview, Record, and MP4 Kit require:

- selected playable audio
- bound image/artwork
- Artist name, max 36 characters

## Best weak-hardware operating mode

- `Quality: Lite` for worst hardware, or `Quality: Eco` for better visuals
- `Hub: Hidden`
- Voxel Icon view
- short Preview checks only
- FFmpeg Kit for final output

## Best release workflow

Browser Record is useful for previews. FFmpeg Kit is the cleaner final-release path because it avoids browser codec and real-time capture problems.


## v1.8.0 weak-hardware rule

Use `Quality: Lite` when the render stutters, the folder is huge, or you are screen recording on an old Mac. The app may also downgrade quality automatically when the performance governor detects repeated frame-budget misses. This does not change exports, metadata, vault items, selected track, or image bindings.
