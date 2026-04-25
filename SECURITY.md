# Security Policy

Voxel Audio is a local-first browser app. It should not upload audio, images, or generated logs.

## Reporting

Please open a private security advisory or contact the maintainer if you find:

- unintended network requests
- unsafe file handling behavior
- script injection risk from filenames or metadata
- browser crashers from malformed files

## Local-first requirements

- No analytics by default.
- No external API calls for core features.
- No remote audio/image processing.
