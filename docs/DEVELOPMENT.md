# Development

Voxel Audio is intentionally simple to run.

```bash
python3 -m http.server 8080
```

Open:

```text
http://localhost:8080
```

## JavaScript syntax check

The app is contained in `index.html`. You can extract the script block and run `node --check` manually, or use `scripts/package_release.py`.

## Release packaging

```bash
python3 scripts/package_release.py
```

This creates a ZIP of the repo contents.
