# Chain Test Synthetic Audio + visibleObjects Runtime Fix — v1.8.14

This patch fixes the `visibleObjects.find is not a function` Promise error caused by treating the `visibleObjects()` helper as an array.

It also makes Chain Test truly input-free:

- If a playable audio file is selected, Chain Test uses it.
- If no folder/audio is loaded, Chain Test generates a temporary 4-second 440Hz WAV in memory.
- If no artwork is bound, Chain Test generates temporary fallback art.
- If Artist is blank, Chain Test uses `CHAIN TEST`.
- Real Record/Preview/MP4 Kit exports still require the actual selected song, artist name, and bound artwork.

The export panel was reduced and constrained so it is less likely to cover controls during diagnostics.
