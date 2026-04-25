# Browser Record Feature

Browser Record is the built-in no-server recording feature.

## Buttons

- **10s Record** — records a short normal-speed preview.
- **Record Full** — records the selected song at normal 1x playback.
- **Record: Auto / MP4 / WebM** — sets recording format preference.

## Important behavior

Browser Record does not speed up the song.

The audio and visual output are recorded at normal 1x playback speed.

## When to use it

Use Browser Record for:

- quick previews
- checking cover layout
- checking color sync
- checking waveform motion
- short demo clips

## When not to use it

Do not rely on Browser Record as the final production path when browser codec support is uncertain.

Use **Build MP4 Kit** for release-grade final MP4 output.

## Failure logs

If recording fails:

1. Click **Download Run Log**.
2. Check MediaRecorder support.
3. Try Record: WebM.
4. Use Build MP4 Kit if browser recording remains unsupported.
