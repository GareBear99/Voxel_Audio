# Export Workflows

## Use Build MP4 Kit for final output

The final-release workflow should be:

1. Select track.
2. Bind image.
3. Set Song name.
4. Click Preflight.
5. Click Build MP4 Kit.
6. Run FFmpeg script.

This path renders faster than realtime depending on CPU, while preserving normal audio speed.

## Use Browser Record for previews

Browser Record exists for convenience.

- 10s Record: quick normal-speed visual check.
- Record Full: full browser recording.
- Record: Auto / MP4 / WebM: format preference.

If it fails, download the run log and use Build MP4 Kit.

## Kit speed

- Kit: Fast — default balance.
- Kit: Turbo — fastest render, larger files / lower quality.
- Kit: Quality — slower, cleaner output.






## Account export plan

Once accounts and server FFmpeg are connected, all prices are USD.

### Free

- $0 USD.
- Browser Record export path.
- Watermark.
- 5 exports/week.

### Server FFmpeg

- $3 USD/month.
- 99 server FFmpeg exports/month.
- Stripe billing.
- Google OAuth login.

### Unlimited Creator

- $7 USD/month.
- Unlimited no-watermark browser Record exports.
- Unlimited no-watermark server FFmpeg exports.
