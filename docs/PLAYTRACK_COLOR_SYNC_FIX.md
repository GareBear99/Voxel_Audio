# PlayTrack Color Sync Fix

Fixed a bug where clicking/playing a real audio voxel selected and played the track but did not call `setAccentFromTrack(tr)`.

## Root cause

The non-file branch synced color, but the real audio-file branch did not.

## Fix

The audio-file branch now calls:

```js
setAccentFromTrack(tr);
syncExportAccentFromTrack(tr);
```

immediately after assigning `currentTrack`, `focusedObjectId`, and `focusedFolder`.

## Result

Clicking the pink voxel now updates the Export color input to that voxel color.
