# Performance Tuning Guide

This guide is for older Macs, weak integrated GPUs, browser lag, and audio/visual sync drift.

## Fastest stable setup

Use this when the render feels laggy:

1. Set `Quality: Lite` on the weakest hardware, or `Quality: Eco` if Lite is too visually stripped down.
2. Set `Hub: Hidden` during playback.
3. Use Voxel Icon view instead of Web Node view.
4. Clear Search unless you are intentionally filtering.
5. Focus a smaller folder instead of rendering the full loaded library.
6. Avoid High mode while editing on weak hardware.
7. Use FFmpeg Kit for final output instead of full Browser Record when possible.

## Why Lite/Eco helps

Lite and Eco lower the cost of the three expensive areas:

- Canvas scene rendering.
- Waveform drawing.
- Web Audio analyser frequency reads.

Lite/Eco also disable or reduce extra section outlines, label boxes, web-node glow shadows, waveform density, analyser FFT size, and floating image transform frequency.

## Quality settings

| Mode | Best use |
|---|---|
| Lite | Lowest-cost fallback for weak GPUs/CPUs, very large folders, or screen recording while CPU-bound. |
| Eco | Old Macs, weak CPUs/GPUs, large folders, smooth editing. |
| Auto | Normal default when hardware can handle it. |
| High | Final visual checking on stronger hardware. |

## Sync behavior

The app uses the HTML audio element as the timing source. Visuals should follow audio time rather than trying to create a separate clock.

Render paths are paced separately:

- Main scene: voxel/folder/web view.
- Wave panel: bottom waveform canvas.
- Audio analyser: frequency and waveform data updates.
- Export renderer: fixed 1280×720 visualizer canvas during preview/record.

This prevents one expensive path from stalling every other path.

## Heavy features to avoid on weak hardware

- High quality mode.
- Web Node view with many tracks.
- Huge folders with thousands of playable files.
- Browser Record full-song exports in MP4 mode.
- Multiple browser tabs using audio/canvas at the same time.
- Browser zoom above 100% while rendering large canvases.

## Best production workflow on weak hardware

Use the browser only to prepare the render:

1. Load folder.
2. Select song.
3. Bind image.
4. Set Artist/Song/Description.
5. Preview briefly in Eco.
6. Build MP4 Kit.
7. Run FFmpeg locally from the generated folder.

This avoids long real-time browser capture sessions.


## v1.8.0 render governor

Voxel Audio now measures main scene draw cost and automatically steps quality down when the current mode cannot keep its frame budget. The downgrade path is:

```text
High → Auto → Eco → Lite
```

This is intentional. On weak hardware, smooth audio playback matters more than keeping every decorative glow or label visible. The governor does not change the selected song, metadata, export color, image binding, vault entries, or FFmpeg kit output.

## Cached background path

The dark grid/gradient background is now rendered into an offscreen cache and reused until theme, size, or quality changes. This removes repeated radial-gradient and grid-line work from the hot animation loop.

## Hidden-tab pause

When the tab is hidden, the animation loop skips canvas and waveform drawing. Audio/browser behavior remains controlled by the browser, but Voxel Audio no longer wastes render budget on an invisible tab.
