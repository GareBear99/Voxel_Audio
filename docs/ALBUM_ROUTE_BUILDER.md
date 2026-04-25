# Album Route Builder

Album Route Builder creates a full album visualizer export kit.

## Add sources

- Add Selected
- Add Visible/Search
- Add Current Folder
- Add All Loaded

Tracks may come from any folder route inside the loaded audio tree.

## Color controls

Each routed track has a color picker.

The album can use:

- source voxel RGB color
- per-track custom color
- one album-wide color

## Covers

Each track can use its own bound cover image.

If some tracks do not have covers, choose a current track with a bound image and click **Use Current Image As Fallback**.

## Output kit

The album kit downloads:

- every audio source
- every cover source
- `album_manifest.json`
- `render_album_ffmpeg.sh`
- `render_album_ffmpeg.bat`
- run log

The script renders per-track segments, then concatenates the album MP4.
