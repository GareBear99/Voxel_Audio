# Voxel Audio v1.8.13 — Chain Test No-Input + Panel Non-Blocking Fix

Fixes the operator workflow problem where Chain Test required artist/image inputs and opened a large panel that blocked the active control buttons.

## Changes

- Chain Test now auto-selects the selected/first playable audio file.
- Chain Test auto-fills `CHAIN TEST` as temporary Artist when blank.
- Chain Test generates temporary fallback cover art when the track has no bound image.
- Real Preview / Record / MP4 exports still enforce Artist + bound image policy.
- Export status panel is constrained to a smaller lower-right scrollable drawer.
- Export panel z-index is below the topbar/quick dock so it does not block those buttons.

## Purpose

The Chain Test exists only to quickly verify repeat browser-record exports before spending 10–20 minutes on a full-song render. It should not require final metadata inputs.
