# Voxel Audio

## Current release status — v1.8.0

This package has been audited and aligned as a **low-weight local creator tool**:

- Local-first folder audio visualizer.
- Playable voxel directory for detected audio files.
- Image binding per track.
- Artist-required export metadata with 36-character cap.
- Live export preview.
- Browser Record for quick previews.
- Session Export Vault with edit/re-export.
- Deterministic FFmpeg MP4 Kit for production output.
- Album Route Builder for multi-track render kits.
- Lite / Eco / Auto / High performance ladder for older hardware.
- Reset/Back button bindings corrected in v1.7.1 after audit.
- Production hardening in v1.8.0: Lite mode, cached background render, hidden-tab pause, web-node draw caps, throttled artwork transforms, debounced resize, and automatic performance governor.

The no-server build is usable now. Google OAuth, Stripe, account quotas, and server FFmpeg rendering are roadmap systems, not active local-build features yet.

See:

- `docs/EXTENSIVE_AUDIT_REPORT.md`
- `docs/PERFORMANCE_TUNING.md`
- `docs/SONG_TITLE_AUTHORITY.md`
- `docs/RELEASE_STATUS.md`
- `docs/OPERATOR_MANUAL.md`


**Voxel Audio** is a local-first, browser-based audio visualizer and export tool that turns a folder of songs into a playable voxel directory, binds artwork to tracks, previews SoundCloud-style export layouts live, and builds deterministic FFmpeg MP4 render kits for single tracks or full albums.

<p align="center">
  <strong>Local audio folder → playable voxel grid → image-bound visualizer → preview → MP4 kit</strong>
</p>

<p align="center">
  <a href="#features">Features</a> ·
  <a href="#quick-start">Quick Start</a> ·
  <a href="#export-workflows">Export Workflows</a> ·
  <a href="#album-route-builder">Album Route Builder</a> ·
  <a href="#docs-routing">Docs Routing</a> ·
  <a href="#roadmap">Roadmap</a>
</p>

---


## Powered by Proto-Synth Grid Engine

Voxel Audio is built as a creator-facing audio export platform using the design language of **Proto-Synth Grid Engine**.

Reference:

```text
https://github.com/GareBear99/Proto-Synth_Grid_Engine
```

Proto-Synth Grid Engine is a deterministic, math-first, low-weight 2D simulation projected to feel visually 3D. Voxel Audio adapts that doctrine into an audio product:

- folders become route surfaces
- tracks become playable voxels
- RGB color becomes export identity
- album routes become renderable structures
- Canvas2D keeps the platform no-server and lightweight
- FFmpeg kits provide deterministic release output


## Why Voxel Audio exists

Most quick music visualizer workflows are either locked behind cloud upload tools, fragile browser screen-recording, or heavyweight video editors. Voxel Audio is designed to be:

- **Local-first** — your audio and images stay on your machine.
- **Folder-native** — drag in a folder and every valid audio file becomes a playable voxel.
- **Release-aware** — preview visually in-browser, but generate final MP4 through deterministic FFmpeg scripts.
- **Album-capable** — build a route from selected tracks, current folder, search results, or all loaded songs.
- **Artist-friendly** — bind cover art, rename export titles, control colors, and produce SoundCloud-style video assets.

---



## Watermark and pricing policy scaffold

The browser Record renderer includes a free-tier watermark scaffold.

Planned USD tiers:

- **Free** — watermarked browser Record exports, 5 exports/week.
- **$3 USD/month** — 99 server FFmpeg exports/month.
- **$7 USD/month** — unlimited no-watermark browser Record exports and unlimited no-watermark server FFmpeg exports.


## Free and paid export positioning

Voxel Audio is being positioned with a creator-friendly **USD** export model once accounts and server rendering are connected.

### Free account plan

```text
$0 USD
```

The free account plan is intended for:

- browser **Record** exports
- watermarked exports
- **5 exports/week** once Google OAuth accounts are released
- local folder playback
- voxel directory browsing
- image binding
- live export preview

### Server FFmpeg tier

```text
$3 USD/month
```

Planned benefits:

- **99 server FFmpeg exports/month**
- server-side FFmpeg MP4 rendering
- Google OAuth account login
- Stripe subscription integration
- better reliability than browser recording for creators who need rendered MP4 output

### Unlimited Creator tier

```text
$7 USD/month
```

Planned benefits:

- **unlimited no-watermark browser Record exports**
- **unlimited no-watermark server FFmpeg exports**
- best fit for creators releasing polished visualizers regularly
- removes the weekly/monthly export ceiling

### Integration roadmap

The account/server plan requires:

- Google OAuth login
- Stripe subscription checkout and billing
- account export counters
- free weekly export limits
- monthly paid FFmpeg export quotas for the $3 USD tier
- unlimited entitlement checks for the $7 USD tier
- server-side FFmpeg render queue
- watermark policy for free browser Record exports
- no-watermark policy for paid tiers

## Features

### Local folder audio router

- Open a folder with the picker.
- Drag/drop a folder anywhere on the screen.
- Detects playable audio files:
  - `mp3`
  - `wav`
  - `ogg`
  - `m4a`
  - `aac`
  - `flac`
  - `opus`
  - `webm`
- Preserves nested route paths for search and album building.
- Every valid audio file becomes:
  - a voxel in the scene
  - a row in the Browser Hub
  - an exportable audio source

### Playable voxel directory

- Click a voxel to play its track.
- Voxel color is seeded and track-specific.
- Selected track color syncs with:
  - app border accent
  - waveform accent
  - export preview accent
  - browser record accent
  - FFmpeg render kit accent
  - album segment accent

### Search and panel safety

- Search filters valid track rows and voxels.
- Browser Hub is height-matched to the left panel.
- Browser Hub scrolls internally.
- Recenter button restores the voxel scene if the view is moved offscreen.

### Image binding

- Bind artwork to the selected track.
- Drag/drop an image onto a voxel to bind directly.
- Bound image is used by:
  - live floating image preview
  - Live Export Preview
  - Browser Record Export
  - single-track FFmpeg MP4 kit
  - album route export kit

### Live Export Preview

- Opens a scaled 1280×720 preview panel.
- Uses the same visual renderer as browser recording.
- Updates while audio plays.
- Uses the selected song’s voxel RGB color.
- Uses editable Song name.
- Shows the final single-track visualizer composition before export.

### Browser Record Export

Browser Record is included as a convenience preview/export path.

- `10s Record` records a short normal-speed preview.
- `Record Full` records the full track at normal 1x speed.
- `Record: Auto / MP4 / WebM` lets the browser pick supported output.
- Run log explains failures when browser recording APIs are unsupported.

> Browser recording is useful, but final release output should use the deterministic FFmpeg kit.

### Deterministic FFmpeg MP4 Kit

The production path is not browser self-recording.

`Build MP4 Kit` downloads:

- the selected audio source
- the bound cover image
- `render_manifest.json`
- `render_ffmpeg.sh`
- `render_ffmpeg.bat`
- run log

Run the script and FFmpeg renders a real H.264/AAC MP4.

### Album Route Builder

Album Route Builder can collect songs from anywhere in the loaded folder tree:

- selected track
- visible/search results
- current folder
- all loaded tracks

It then generates a full album render kit:

- all routed audio files
- per-track covers or fallback cover
- `album_manifest.json`
- `render_album_ffmpeg.sh`
- `render_album_ffmpeg.bat`
- album run log

Each track segment can use:

- its original voxel RGB color
- a per-track custom album color
- one album-wide color applied to every track

---


## No-server local mode

Voxel Audio is built to work as a **no-server local app**.

You can use it by simply double-clicking:

```text
index.html
```

No backend is required.

No account is required.

No upload is required.

No local Node server is required for normal use.

A local static server is optional only when you want more predictable browser behavior during development.

### What works locally

- Folder picker.
- Drag/drop folder loading.
- Audio playback.
- Voxel scene rendering.
- Search.
- Image binding.
- Live Export Preview.
- Browser Record Export.
- FFmpeg MP4 Kit generation.
- Album Route Builder.
- Info/docs overlay.

### Browser Record feature

Voxel Audio includes a no-server browser recording feature:

- **10s Record** records a short normal-speed preview.
- **Record Full** records the selected song at normal 1x playback speed.
- **Record: Auto / MP4 / WebM** selects the browser recording preference.
- Download Run Log explains any recording failure.

Browser Record is best for quick previews. For release-grade MP4 output, use **Build MP4 Kit**.


## Reliability patch: Quick Dock

The app includes a fixed upper-right **Quick Dock** so critical controls remain accessible even if the top bar overflows on smaller screens.

Quick Dock buttons:

- `＋ Folder`
- `＋ Image`
- `ⓘ Info`
- `Preview`
- `Record`
- `MP4 Kit`
- `Album`

A small startup diagnostic appears briefly on load and reports if required browser APIs or controls are missing.


## Hotbar cleanup and freeze guard

The app now keeps duplicated Quick Dock actions out of the top scroll bar, making the top bar shorter and easier to use.

Critical actions stay in the fixed Quick Dock:

- Folder
- Image
- Info
- Preview
- Record
- MP4 Kit
- Album
- Bindings

Runtime error diagnostics now appear onscreen if a control or browser API fails instead of silently freezing.

## Quick Start

### Option A — open directly

Double-click `index.html` or open it directly in a modern browser. This is the recommended no-server path.

Recommended browsers:

- Chrome
- Edge
- Safari for MP4 experiments
- Any browser with Web Audio and Canvas support for playback/visuals

### Option B — serve locally

Some browser features behave better from a local server.

```bash
python3 -m http.server 8080
```

Then open:

```text
http://localhost:8080
```

---

## Basic workflow

1. Click **Open Audio Folder**, or drag/drop a folder anywhere.
2. Click a voxel or Browser Hub row to select/play a song.
3. Click **Bind Image To Selected**, or drag an image onto a voxel.
4. Edit **Song name** in the export panel if needed.
5. Click **Preview Export**.
6. Use **10s Record** for a quick browser preview.
7. Use **Build MP4 Kit** for final release-quality MP4 output.

---



## Binding maps

Voxel Audio now supports binding-map metadata:

- **Export Bindings** downloads a JSON map of track/image/color binding metadata.
- **Import Bindings** matches loaded tracks by path/name and restores metadata.
- Image blobs may still need rebinding because browsers do not allow silent restoration of arbitrary local files.


## Session Export Vault

Browser Record exports are now protected by a session vault.

After **10s Record** or **Record Full** completes, Voxel Audio keeps the last **9 browser Record exports** in memory with Download buttons.

This solves the problem where a browser download prompt is missed or dismissed at the end of the recording stream.

Important notes:

- The vault is session-only.
- It clears when the page is closed or reloaded.
- It does not upload anything.
- It is for Browser Record outputs, not FFmpeg kit files.


## Image-required export policy

Voxel Audio now blocks visual export actions unless artwork is bound to the selected track.

Required before single-track export:

1. Select/play a song.
2. Bind or drop an image onto that song.
3. Confirm the floating image appears.
4. Then use Preview, Record, or Build MP4 Kit.

Blocked until artwork is present:

- Preview Export
- 10s Record
- Record Full
- Build MP4 Kit

Album export also requires artwork coverage: either every routed track has artwork, or a fallback album cover is set.

## Export shape safety

The renderer clamps rounded-rectangle radius values so tiny progress bars and UI pills cannot explode into giant foreground shapes. This prevents the waveform/progress accent color from covering the cover image or export layout.

## No foreground accent-shape policy

The export renderer now disables large RGB blob/triangle accent fills. Only subtle background glow is allowed.

This guarantees the cover image, title, description panel, waveform panel, and watermark are never covered by foreground color geometry.

## Selected voxel color identity

All export visual elements now follow the selected song's voxel RGB color:

- title glow
- metadata text
- description/capsule panel
- cover outline
- reactive circle
- waveform
- progress bar
- watermark
- preview/export panel borders
- background glow

## Export metadata and layering

Voxel Audio export layouts now include editable metadata:

- Song name
- Artist
- Feat
- Description

The Description field defaults to:

```text
full-track reactive visualizer
```

The export renderer uses a strict layer policy so RGB accent shapes stay behind the cover image, description panel, title, and waveform panel.

The circular visual element is now a real reactive frequency visualizer using bass, mid, treble, and frequency-spoke motion.

## Export Workflows

### Final release workflow

Use this for actual music distribution, store previews, YouTube uploads, SoundCloud visual assets, or release promos.

1. Select a song.
2. Bind artwork.
3. Click **Preflight**.
4. Click **Build MP4 Kit**.
5. Move all downloaded kit files into one folder if your browser separates downloads.
6. Run:

macOS/Linux:

```bash
chmod +x render_ffmpeg.sh
./render_ffmpeg.sh
```

Windows:

```bat
render_ffmpeg.bat
```

Output:

```text
<song>_Voxel_Audio.mp4
```

### Browser preview workflow

Use this for quick checks.

1. Select a song.
2. Bind artwork.
3. Click **Preview Export**.
4. Click **10s Record**.
5. Review the downloaded preview.

Browser recording is normal 1x song speed. It is intentionally not accelerated.

---

## Install FFmpeg

### macOS

```bash
brew install ffmpeg
```

### Windows

```powershell
winget install Gyan.FFmpeg
```

### Linux

```bash
sudo apt install ffmpeg
```

---

## Album Route Builder

Open **Album Route**.

Add tracks by:

- **Add Selected** — adds the current song.
- **Add Visible/Search** — adds whatever the current search/filter shows.
- **Add Current Folder** — adds tracks from the selected/current folder.
- **Add All Loaded** — adds every loaded track.

Then configure:

- Album title
- Route name
- Fallback cover image
- Per-track colors
- Album-wide color

Click **Build Full Album Kit**.

Run:

```bash
chmod +x render_album_ffmpeg.sh
./render_album_ffmpeg.sh
```

or on Windows:

```bat
render_album_ffmpeg.bat
```

The script renders each track segment and concatenates the full album MP4.

---

## Docs Routing

The app includes an in-app **ⓘ Info** overlay with route-based documentation:

- Overview
- Quick Start
- Controls
- Folder Loading
- Search
- Image Binding
- Live Preview
- Browser Record
- MP4 Kit
- Layout / Panels
- Troubleshooting
- Album Route Plan
- Release Notes

External docs mirror the same structure in `docs/routes`.

---

## Privacy

Voxel Audio is local-first.

- No uploads.
- No external API required.
- Audio files stay on your machine.
- Images stay on your machine.
- Export kits are generated locally in the browser.
- Final MP4 rendering happens locally through FFmpeg.

---

## Browser support notes

Playback and visualizer features use:

- HTML File APIs
- Canvas 2D
- Web Audio API
- drag/drop APIs

Browser Record uses:

- `MediaRecorder`
- `canvas.captureStream`
- WebAudio stream routing

These APIs vary by browser. When browser recording fails, use the deterministic FFmpeg kit.

---

## Project structure

```text
voxel-audio/
├── index.html
├── README.md
├── LICENSE
├── CHANGELOG.md
├── package.json
├── docs/
│   ├── routes/
│   ├── EXPORT_WORKFLOWS.md
│   ├── ALBUM_ROUTE_BUILDER.md
│   ├── TROUBLESHOOTING.md
│   └── ARCHITECTURE.md
├── examples/
│   └── example-render-manifest.json
├── scripts/
│   └── package_release.py
└── .github/
    ├── ISSUE_TEMPLATE/
    └── workflows/
```

---

## Roadmap

- Native desktop wrapper for automatic FFmpeg rendering.
- One-click final MP4 export without manual script execution.
- Persisted image binding maps.
- Saved export presets.
- Album route import/export JSON.
- Drag reorder album route tracks.
- Optional waveform style presets.
- GitHub Pages demo shell.
- Optional WebCodecs/WebGPU renderer path.

---

## SEO phrases

Voxel Audio targets:

- local audio visualizer
- SoundCloud style visualizer
- MP4 music visualizer generator
- FFmpeg audio visualizer
- browser music visualizer
- album visualizer export
- local-first music video generator
- canvas audio waveform visualizer
- Web Audio visualizer
- artist release video tool

---

## License

MIT License. See `LICENSE`.


## Compact blank-description layout

When the Description field is left blank, Voxel Audio now uses a tighter export layout instead of leaving empty text space.

- Blank Description = compact visualizer capsule.
- Typed Description = full description panel.
- Reactive circle stays active in both modes.

## Optional description behavior

The export Description field is optional. If left blank, no description is rendered.


## Export overlap safety

The export layout now prevents collisions between:
- watermark and waveform/timestamps
- metadata row and reactive circle
- description/capsule text and circle lane

Long metadata text is automatically ellipsized to stay inside the safe lane.



## Admin watermark unlock

The export panel includes **Admin name** and **Admin key** inputs.

Local dev/admin key:

```text
VOXEL-AUDIO-ADMIN
```

Entering the key disables the free watermark for browser Record exports in the current local browser/session. This is a development scaffold only; production no-watermark access must be enforced server-side through Google OAuth, Stripe, and render entitlement checks.


## TizWildin watermark branding

When the free watermark is active, exports display:

```text
TIZWILDIN ENTERTAINMENT
A TizWildin Entertainment Product
```

The Admin key can still disable the watermark locally for development/testing.


## Admin clean-export status and single export color

The export panel now includes:

- Admin name
- Admin key
- admin clean-export status hint
- single Export color chooser

The admin unlock removes the watermark from Live Preview and Browser Record immediately.

The Export color picker defaults to the selected voxel color, but can be changed for that single audio export.


## Where completed Record exports show up

Completed **10s Record** and **Record Full** exports appear in the **Session Export Vault**.

Use the Quick Dock:

```text
Vault
```

The Vault also opens automatically after a successful browser Record export. It keeps the last 9 completed browser Record exports from the current session, each with a Download button.


## Vault edit and re-export

Completed browser Record exports in the Session Export Vault can now be edited and re-exported.

Editable per vault item:

- Song name
- Artist
- Feat
- Description
- Export color

Click **Re-export** to re-run the same Record mode using the edited metadata. The original track and image binding must still be loaded in the current session.


## Artist required before export

Voxel Audio now requires an **Artist** name before Preview, Record, or MP4 Kit export.

Rules:

- Artist is required.
- Artist max length is 36 characters.
- Artist is locked into export metadata when recording/export starts.
- Vault re-export also requires Artist.


## Voxel click color sync

Selecting a voxel now always resets the export color to that voxel's RGB color.

Manual color override still works, but only until you select another voxel.


## PlayTrack color sync fix

Clicking/playing a real audio voxel now immediately pushes that voxel color into the Export color input and export renderer.

The issue was that the real audio-file branch played the track but skipped the color-sync call.


## Reset and Back behavior

- **Reset** fully returns the app to startup state and clears the loaded session.
- **Back** only backs out of panels, folder focus, search, selected voxel focus, or zoom. It does not delete the loaded folder/session.

---

## v1.8.0 production documentation map

For the current audited and production-hardened package state, use these docs first:

| Document | Purpose |
|---|---|
| `docs/EXTENSIVE_AUDIT_REPORT.md` | Full package audit, confirmed capabilities, known constraints, and next engineering pass. |
| `docs/PERFORMANCE_TUNING.md`
- `docs/SONG_TITLE_AUTHORITY.md` | Weak-hardware Lite/Eco operating guide and performance governor notes. |
| `docs/RELEASE_STATUS.md` | What is ready now vs. what is still roadmap. |
| `docs/OPERATOR_MANUAL.md` | Straight usage manual for loading, binding, previewing, recording, vault, and FFmpeg kit workflow. |
| `docs/ARCHITECTURE.md` | Runtime layer map and quality ladder. |
| `docs/PRODUCTION_HARDENING_PASS.md` | v1.8.0 runtime hardening details and remaining SaaS blockers. |
| `docs/RESET_AND_BACK_BEHAVIOR.md` | Correct Reset/Back behavior after v1.7.1 binding fix. |


### v1.8.4 Title Render Revert

The v1.8.2/v1.8.3 title marquee experiment has been reverted. Export title rendering is restored to v1.8.1 behavior while keeping Song Title Authority intact. See `docs/TITLE_RENDER_REVERT.md`.


### v1.8.5 Side Metadata Scroll Fix

The small `VOXEL AUDIO EXPORT • song • artist/feat` export metadata line now scrolls inside a clipped safe lane and cannot overlap the reactive circle. Main title rendering is untouched. See `docs/SIDE_METADATA_SCROLL_FIX.md`.


### v1.8.6 Preview Scroll Clock Fix

Live Export Preview now correctly shows the small metadata line scrolling because the preview renderer uses a persistent timing clock instead of resetting every frame. Main title rendering is untouched. See `docs/PREVIEW_SCROLL_CLOCK_FIX.md`.


### v1.8.7 Side Metadata End Pause

The small side metadata scroll now holds longer at the end before resetting back to the start. Main title rendering remains untouched. See `docs/SIDE_METADATA_END_PAUSE.md`.


### v1.8.10 MP4 Direct Audio Restore

Browser Record MP4 is restored and now tries direct `<audio>.captureStream()` before WebAudio capture to reduce silent MP4 exports. The recorder logs audio/video track counts before recording starts. See `docs/MP4_DIRECT_AUDIO_RESTORE.md`.
