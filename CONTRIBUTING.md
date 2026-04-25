# Contributing

Thank you for considering a contribution to Voxel Audio.

## Good contributions

- Browser compatibility fixes.
- Export renderer improvements.
- FFmpeg script hardening.
- Album route workflow improvements.
- Accessibility and keyboard navigation.
- Documentation fixes.
- Performance improvements for large folders.

## Development

Run locally:

```bash
python3 -m http.server 8080
```

Open `http://localhost:8080`.

## Pull request expectations

- Keep the app local-first.
- Do not add telemetry.
- Do not upload user audio/images.
- Preserve the deterministic FFmpeg kit as the recommended final output path.
- Update docs for user-facing behavior changes.
