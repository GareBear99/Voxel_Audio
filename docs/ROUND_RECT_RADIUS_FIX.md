# Rounded Rectangle Radius Fix

The huge green foreground shape was caused by the custom `drawRoundedRect()` helper accepting a radius larger than the rectangle height.

Example:

```js
drawRoundedRect(ctx, x, y, width, 6, 999)
```

On a 6px-high progress bar, radius `999` produced malformed curves that expanded into a massive foreground shape.

## Fix

`drawRoundedRect()` now clamps radius to:

```js
min(radius, width / 2, height / 2)
```

The export progress bar also uses radius `3` instead of `999`.

This prevents progress bars, pills, and tiny UI shapes from exploding into giant export overlays.
