# Reset and Back Behavior

## Reset

Reset returns Voxel Audio to startup state.

It clears:

- loaded audio objects
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
4. clear selected voxel focus
5. recenter/zoom out to root view

Use Back when you zoomed/focused into something and want to return.
