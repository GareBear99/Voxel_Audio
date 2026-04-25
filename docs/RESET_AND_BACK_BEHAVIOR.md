# Reset and Back Behavior

## Reset

Reset returns Voxel Audio to startup/demo state.

It clears:

- loaded audio track registry
- generated voxel objects
- current playback
- selected voxel
- search
- folder focus
- image bindings in memory
- album route
- session export vault
- export fields
- panels/overlays

Use Reset when you want to start over completely.

## Back

Back does not delete loaded audio.

It steps out in this order:

1. close active preview/album/docs/export/vault panels
2. leave focused folder
3. clear search
4. clear selected voxel/current track focus
5. recenter/zoom out to root view

Use Back when you zoomed/focused into something and want to return without losing the loaded session.

## v1.7.1 audit correction

The stronger reset/back helper functions existed in the app, but the final button bindings were still pointing at older inline handlers. v1.7.1 wires the buttons to the correct helpers.
