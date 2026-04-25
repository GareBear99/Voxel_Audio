# Extensive Audit Report — v1.8.0 Production Hardening

This audit reviews the current single-file Voxel Audio package after the low-weight render/sync pass and the v1.8.0 production hardening pass.

## Audit scope

Reviewed package areas:

- `index.html` application shell, controls, renderer, audio graph, export renderer, in-app docs, vault, album route, reset/back controls, and local admin scaffold.
- `README.md` public-facing usage, feature, pricing, and workflow documentation.
- `docs/*.md` feature docs and policy docs.
- `package.json` package metadata, keywords, scripts, and release identity.
- `scripts/package_release.py` release ZIP builder.

## Current release identity

- Package version: `1.8.0`
- Baseline: `1.7.1` audited docs/runtime alignment.
- Patch purpose: production hardening for weak hardware, smoother audio sync, and cleaner release-candidate packaging.

## Confirmed runtime capabilities

### Local-first folder visualizer

- Runs from `index.html` with no build step.
- Can also be served with `python3 -m http.server 8080`.
- Audio files become clickable voxels and Browser Hub rows.
- Supported extensions are `mp3`, `wav`, `ogg`, `m4a`, `aac`, `flac`, `opus`, and `webm`.
- Nested folder paths are preserved for routes/search/album building.

### Audio-reactive render loop

The render loop is split into separate pacing buckets:

- main voxel scene FPS
- waveform FPS
- audio analyser FPS
- DOM/CSS update pacing

This is the correct low-weight direction because the app avoids forcing every visual subsystem to redraw at the display refresh rate.

### Quality ladder

| Mode | Main FPS | Wave FPS | Audio FPS | DPR cap | Voxel cap | Web node cap | Link cap | Bars | FFT | Shadows | Labels | Sections |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| Lite | 18 | 12 | 18 | 0.85 | 120 | 32 | 24 | 20 | 256 | Off | Off | Off |
| Eco | 24 | 18 | 24 | 1.00 | 220 | 72 | 60 | 32 | 512 | Off | Off | Off |
| Auto | 36 | 24 | 30 | 1.15 | 520 | 160 | 150 | 48 | 1024 | Off | On | On |
| High | 60 | 45 | 45 | 1.50 | 1200 | 360 | 420 | 80 | 2048 | On | On | On |



### v1.8.0 hardening additions

- Static main-background cache removes repeated radial-gradient/grid work from the hot render loop.
- Hidden-tab pause skips scene/wave drawing when the page is not visible.
- Performance governor measures draw cost and can step down `High → Auto → Eco → Lite`.
- Web Node mode is capped by node and link budgets in lower modes.
- Floating artwork transforms are throttled in Lite/Eco.
- Browser Record capture uses 30 FPS in Lite/Eco and 60 FPS in Auto/High.
- `npm run check:js` now fails properly on syntax errors instead of ignoring them.

### Export paths

- Browser Record is a convenience path that records at normal 1x playback speed.
- FFmpeg Kit is the deterministic production path.
- Album Route Kit builds multi-track FFmpeg scripts/manifests.
- Export color follows the selected voxel unless manually overridden.
- Bound artwork is required for Preview, Browser Record, and MP4 Kit.
- Artist name is required before export and capped at 36 characters.

### Session Export Vault

- Stores the last 9 completed Browser Record outputs in the current browser session.
- Includes Download and Re-export actions.
- Allows editing Song name, Artist, Feat, Description, and Export color before re-export.
- Re-export requires the original track and image binding to still exist in the current page session.

### Admin watermark scaffold

- Local key scaffold: `VOXEL-AUDIO-ADMIN`.
- Unlock state persists locally with `localStorage`.
- Unlock hides watermark in Live Preview and Browser Record.
- FFmpeg Kit manifest records the admin clean-export status.
- This is not a secure production entitlement system; production must use account/server checks.

## Fix applied during audit

### Reset / Back binding alignment

The runtime already contained stronger helper functions for reset/back behavior, but the final event-binding block was still wired to older lightweight inline handlers.

This patch wires:

- `Reset` → `resetToStartupState`
- `Back` → `backOutOfZoomOrFocus`

The reset helper was also aligned to clear the loaded track registry before rebuilding the startup/demo state.

## Remaining known constraints

### Browser Record is browser-dependent

MediaRecorder, canvas capture, and MP4 support vary by browser. WebM tends to be more reliable than browser MP4. FFmpeg Kit remains the correct production path.

### `file://` behavior can vary

The app is designed to work by double-clicking `index.html`, but some browser file/folder APIs can behave differently under `file://`. If folder input or drag/drop acts weird, serve locally:

```bash
python3 -m http.server 8080
```

Then open:

```text
http://localhost:8080
```

### Large libraries still need user-side discipline

Eco mode reduces pressure, but thousands of tracks can still cost CPU/memory in browser state, list rendering, search, and object registry work. Use search/folder focus and hide the Hub during playback on older machines.

### In-app docs are concise

The overlay docs inside `index.html` are intentionally shorter than the markdown docs. The markdown docs are the source for deeper operator/release guidance.

## Recommended next engineering pass

1. Add a true render budget meter showing frame timing, analyser timing, visible voxels, and dropped-frame estimates.
2. Add a hard library cap warning for huge folder loads.
3. Virtualize Browser Hub rows beyond the first visible list window.
4. Add an explicit `Ultra Eco` mode for 2012-era hardware.
5. Move CSS glow/filter effects behind a `Visual FX` toggle.
6. Add a persistent settings object for last-used quality, hub visibility, and export format.
7. Add a real test harness that extracts the script block and runs syntax checks on the actual app code, not only the extractor script.

## Operator verdict

The app is now documented as a local-first visualizer/export workstation with a realistic split between:

- live browser preview and quick Record exports
- deterministic FFmpeg production rendering
- future paid/account/server roadmap
- low-weight weak-hardware operation

The main immediate production risk remains browser codec inconsistency, not the visualizer concept itself.
