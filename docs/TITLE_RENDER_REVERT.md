# Title Render Revert — v1.8.4

This release reverts the v1.8.2/v1.8.3 title marquee experiments.

## Restored

- Export title rendering is back to the v1.8.1 behavior.
- No title marquee.
- No title ghost-repeat text.
- No title safe-box shrink.
- No duplicate scrolling copy.
- No title fade mask.
- No title animation changes.

## Kept

- v1.8.1 Song Title Authority remains active:
  - Song name is preferred over raw filename.
  - Filename remains only a fallback/source trace.
  - Preview/export/vault/kit naming still prefer canonical Song name.

## Note

Future scrolling behavior should not touch the main export title unless explicitly requested.
