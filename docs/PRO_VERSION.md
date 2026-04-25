# Voxel Audio Pricing / Accounts Plan

Voxel Audio is planned as a 3-tier **USD** export model once Google OAuth, Stripe, and server FFmpeg rendering are connected.

## Free account

```text
$0 USD
```

Planned free account rules:

- Browser Record exports.
- Watermark on free exports.
- 5 exports per week.
- Local folder playback.
- Search, voxel browsing, image binding, and live preview.

Browser Record remains the free export path.

## Server FFmpeg tier

```text
$3 USD/month
```

Planned quota:

```text
99 server FFmpeg exports/month
```

This tier gives users server-side FFmpeg MP4 rendering without relying only on browser recording.

## Unlimited Creator tier

```text
$7 USD/month
```

Planned benefits:

- Unlimited no-watermark browser Record exports.
- Unlimited no-watermark server FFmpeg exports.
- Best fit for creators releasing polished visualizers regularly.

## Required integrations

- Google OAuth login.
- Stripe subscription checkout.
- Account dashboard.
- Export counter and quota ledger.
- Weekly free quota reset.
- Monthly paid quota reset for the $3 USD tier.
- Unlimited entitlement checks for the $7 USD tier.
- Server-side FFmpeg render queue.
- Watermark handling for free browser Record exports.
- No-watermark handling for paid tiers.

## Public copy

Suggested product line:

> Voxel Audio is free for local playback and watermarked browser Record exports up to 5 times per week. Upgrade to the $3 USD/month server FFmpeg tier for 99 FFmpeg exports/month, or the $7 USD/month Unlimited Creator tier for unlimited no-watermark Record and server FFmpeg exports.
