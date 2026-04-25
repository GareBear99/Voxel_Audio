# Architecture

Voxel Audio is a single-file local-first application built around browser-native APIs.

## Runtime layers

1. **File ingestion**
   - folder picker
   - drag/drop folder traversal
   - audio extension detection
   - route preservation

2. **Track registry**
   - one registry item per valid audio file
   - route path
   - display name
   - object ID
   - voxel color
   - optional bound image file/blob URL

3. **Voxel renderer**
   - Canvas 2D scene
   - Voxel Icon view
   - Web Node view
   - adaptive quality ladder
   - capped voxel/node/link rendering
   - recenter/fit viewport logic

4. **Audio engine**
   - HTMLAudioElement as playback clock
   - Web Audio API analyser
   - frequency data
   - time-domain waveform data
   - FFT size controlled by active quality mode

5. **Export renderer**
   - shared 1280×720 canvas composition
   - selected track color or manual export color override
   - bound cover art
   - editable song/artist/feat/description metadata
   - smoothed waveform / eased bars
   - watermark layer controlled by local admin scaffold for testing

6. **Export paths**
   - Browser Record: convenience preview/export path
   - FFmpeg Kit: deterministic production path
   - Album Route Kit: deterministic multi-track production path

7. **Session Export Vault**
   - last 9 Browser Record exports
   - download buttons
   - metadata edit fields
   - re-export while original track/artwork remain loaded

## Render/sync model

The application does not force every subsystem to redraw at the same rate.

| Path | Purpose |
|---|---|
| Main render clock | Voxel Icon / Web Node scene. |
| Wave render clock | Bottom waveform panel. |
| Audio analyser clock | Frequency/time-domain data refresh. |
| DOM/CSS pacing | Status text, CSS beat variables, and UI feedback. |
| Export render loop | Dedicated 1280×720 frame renderer during preview/record. |

## Quality ladder

| Mode | Main FPS | Wave FPS | Audio FPS | DPR cap | Voxel cap | Web node cap | Link cap | Bars | FFT | Shadows | Labels | Sections |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| Eco | 24 | 18 | 24 | 1.00 | 220 | 72 | 60 | 32 | 512 | Off | Off | Off |
| Auto | 36 | 24 | 30 | 1.15 | 520 | 160 | 150 | 48 | 1024 | Off | On | On |
| High | 60 | 45 | 45 | 1.50 | 1200 | 360 | 420 | 80 | 2048 | On | On | On |

## Why FFmpeg kit generation

Browser recording is inherently browser-dependent. FFmpeg output is deterministic, scriptable, and produces standard H.264/AAC MP4 output.

## Current production boundary

The no-server build is a strong local creator tool. Account-backed pricing, server FFmpeg, Stripe, Google OAuth, and secure no-watermark entitlement enforcement are roadmap items, not local-build features.


## v1.8.0 Production Renderer Notes

The runtime now uses four quality profiles:

| Mode | Intent |
|---|---|
| Lite | Lowest-cost survival path for weak hardware. |
| Eco | Smooth editing path for older Macs/integrated GPUs. |
| Auto | Balanced default. |
| High | Strong-hardware visual inspection. |

The render loop is protected by:

- cached static background canvas
- separate main/wave/audio pacing
- hidden-tab draw skipping
- debounced resize
- performance-governed quality fallback
- Web Node draw caps
- throttled floating image transform updates

The deterministic FFmpeg kit remains the preferred final-output path because browser recording is tied to real-time device performance and browser codec support.
