# Binding Maps

Voxel Audio supports exporting and importing binding metadata.

## Export Bindings

Downloads:

```text
voxel_audio_binding_map.json
```

The map includes:

- audio path
- track name
- folder
- image filename metadata
- color
- binding status

## Import Bindings

Imports metadata and matches loaded tracks by path or name.

Browser security prevents restoring raw image file blobs automatically. If image blobs are unavailable, rebind image files after import.

## Why it exists

Binding maps make repeat work faster when building a release visualizer project around the same folder structure.
