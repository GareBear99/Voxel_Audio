# Export No-Foreground-Shapes Policy

The export renderer no longer draws large RGB blob/triangle shapes.

## Why

Large filled accent shapes could visually appear in front of the cover image or export panels during preview/recording.

## Current policy

- No large filled foreground accent geometry.
- Only subtle radial background glow is allowed.
- Cover art, text panels, description panel, waveform panel, and watermark always render above the background.
- Reactive circle and waveform remain the primary audio-reactive visual elements.

## Layer order

1. Background cover blur.
2. Dark overlay.
3. Subtle safe background glow.
4. Cover art.
5. Title/metadata.
6. Description panel.
7. Reactive circle.
8. Waveform panel.
9. Watermark.
