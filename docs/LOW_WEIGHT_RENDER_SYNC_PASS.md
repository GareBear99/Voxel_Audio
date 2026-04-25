# Low-Weight Render + Audio Sync Pass

This pass targets older Macs and weak integrated graphics.

## Runtime changes

- Eco mode caps the main voxel renderer at 24 FPS and the waveform at 18 FPS.
- Audio analysis has its own cap so FFT reads do not run at full display refresh rate.
- Waveform, audio analysis, and main scene rendering are decoupled so one expensive path does not stall the others.
- Eco mode uses a smaller analyser FFT buffer, fewer bars, wider waveform sampling, fewer web nodes, fewer links, and fewer rendered voxels.
- Canvas contexts request opaque/desynchronized rendering where supported.
- Web Node glow shadows are disabled in Eco/Auto and only enabled in High.
- Eco skips section outlines and label boxes to prevent text-measure/layout cost from spiking.
- Floating image movement is damped in Eco so it stays synced without causing heavy transform churn.

## Recommended settings for weak hardware

Use `Quality: Eco`, keep `Hub: Hidden` during playback/export preview, and search/focus a folder when loading very large music libraries.

## Quality ladder

| Mode | Main FPS | Wave FPS | Audio FPS | FFT | Voxel cap | Web node cap | Link cap | Bars |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Eco | 24 | 18 | 24 | 512 | 220 | 72 | 60 | 32 |
| Auto | 36 | 24 | 30 | 1024 | 520 | 160 | 150 | 48 |
| High | 60 | 45 | 45 | 2048 | 1200 | 360 | 420 | 80 |

## Practical rule

Eco is the editing mode. High is the inspection mode. FFmpeg Kit is the final-render mode.
