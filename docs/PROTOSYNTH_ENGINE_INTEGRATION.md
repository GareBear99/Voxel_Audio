# Proto-Synth Grid Engine Integration

Voxel Audio is designed as an audio-export platform using the design language and runtime doctrine of Proto-Synth Grid Engine.

Reference repository:

```text
https://github.com/GareBear99/Proto-Synth_Grid_Engine
```

## Concepts carried over

Proto-Synth Grid Engine presents a deterministic 2D simulation projected to feel visually 3D, where geometry becomes computation and the world is a programmable surface. Voxel Audio adapts those ideas into an audio workflow:

| Proto-Synth concept | Voxel Audio adaptation |
|---|---|
| Geometry as computation | Folder/audio files become spatial voxel objects |
| Deterministic 2D core | Canvas2D low-weight render loop |
| Visually 3D projection | Voxel directory scene with depth shading |
| Blueprint/routing surface | Folder paths and album routes |
| Entities/executors | Audio tracks as playable/exportable nodes |
| RGB identity | Voxel RGB drives export visuals |
| No-server baseline | Single-file local app |

## Product positioning

Voxel Audio is not just a visualizer. It is a local-first RGB voxel directory for turning music libraries into playable/exportable spatial routes.

## Export doctrine

- Browser Record is the local/free preview path.
- FFmpeg Kit is the deterministic production path.
- Server FFmpeg will become the paid cloud-assisted path later.
- Album Route Builder turns folder/search/selection paths into exportable release structures.
