# Export Overlap Cleanup

This patch removes remaining export layout overlaps.

## Fixed
- Watermark no longer sits over the waveform panel/timestamps.
- Metadata row is now width-fitted with ellipsis.
- Description/capsule panel is narrowed so the reactive circle has a dedicated lane.
- Circle is repositioned slightly right and scaled down to stay clear of text.
- Timestamp row is nudged for cleaner spacing.

## Intent
No export element should cover another export element.
