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
   - optional bound image file

3. **Voxel renderer**
   - Canvas 2D scene
   - adaptive quality
   - capped voxel rendering
   - recenter/fit viewport logic

4. **Audio engine**
   - HTMLAudioElement
   - Web Audio API analyser
   - frequency data
   - time-domain waveform data

5. **Export renderer**
   - shared 1280×720 canvas composition
   - selected track color
   - bound cover art
   - editable song name
   - smoothed waveform / eased bars

6. **Export paths**
   - Browser Record: convenience preview path
   - FFmpeg Kit: deterministic production path

7. **Album Route Builder**
   - route list of track IDs
   - per-track color override
   - album fallback image
   - render scripts and manifest generation

## Why FFmpeg kit generation

Browser recording is inherently browser-dependent. FFmpeg output is deterministic, scriptable, and produces standard H.264/AAC MP4 output.
