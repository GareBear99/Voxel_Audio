# Monetization and Accounts Architecture

This document defines the planned Voxel Audio account/export model.

All prices are **USD**.

## Free tier

- Price: $0 USD.
- Export type: browser Record.
- Watermark: yes.
- Limit: 5 exports/week.
- Reset cadence: weekly.
- Requires account once account system is active.

## Server FFmpeg tier

- Price: $3 USD/month.
- Export type: server-side FFmpeg MP4.
- Limit: 99 exports/month.
- Reset cadence: monthly subscription period.
- Billing provider: Stripe.
- Login provider: Google OAuth.
- Watermark: no watermark planned for server FFmpeg exports unless revised.

## Unlimited Creator tier

- Price: $7 USD/month.
- Export type: browser Record and server-side FFmpeg MP4.
- Limit: unlimited exports.
- Watermark: no watermark.
- Reset cadence: active subscription entitlement.
- Billing provider: Stripe.
- Login provider: Google OAuth.

## Required backend components

1. Google OAuth authentication.
2. User table.
3. Stripe customer/subscription mapping.
4. Export quota ledger.
5. Weekly free quota reset.
6. Monthly paid quota reset for the $3 USD tier.
7. Unlimited entitlement checks for the $7 USD tier.
8. Server-side FFmpeg render worker.
9. Watermark renderer for free browser Record path.
10. No-watermark render path for paid tiers.
11. Download storage or temporary signed file links.
12. Abuse/rate-limit controls.

## Suggested quota rules

### Free

```text
price = 0 USD
exports_weekly_limit = 5
export_type = browser_record
watermark = true
```

### Server FFmpeg

```text
price = 3 USD/month
ffmpeg_exports_monthly_limit = 99
export_type = server_ffmpeg
watermark = false
```

### Unlimited Creator

```text
price = 7 USD/month
record_exports_limit = unlimited
ffmpeg_exports_limit = unlimited
watermark = false
```

## Product copy

> Free users can create watermarked browser Record exports up to 5 times per week. The $3 USD/month server FFmpeg tier unlocks 99 server-rendered MP4 exports per month. The $7 USD/month Unlimited Creator tier unlocks unlimited no-watermark Record and server FFmpeg exports.
