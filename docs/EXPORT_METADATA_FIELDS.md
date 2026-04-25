# Export Metadata Fields

Voxel Audio exports support editable metadata before and during browser recording.

## Fields

- Song name
- Artist
- Feat
- Description

## Defaults

If Song name is empty, it auto-fills from the selected audio file.

Artist and Feat are optional.

Description is also optional:
- If Description is blank, no description is rendered.
- If Description has text, that text is shown in the export layout.

## Live behavior

The browser Record renderer reads the fields while frames are being rendered, so edits made during recording can appear in the output after the edit point.

## Visualizer circle

The circle in the description area is a reactive frequency visualizer blending bass, mids, treble, and frequency spokes.
