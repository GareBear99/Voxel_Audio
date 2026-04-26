# Release Status — v1.8.16

## Status

Production-track local prototype / creator tool package.

Voxel Audio is usable as a no-server local audio visualizer and export kit builder. It is not yet the final account-backed SaaS/server export platform.

## Ready now

- Local folder loading.
- Clickable voxel playback.
- Image binding per track.
- Search and folder routing.
- Live export preview.
- Browser Record preview exports.
- Session Export Vault.
- Vault metadata edit and re-export.
- Single-track FFmpeg MP4 Kit.
- Album Route FFmpeg Kit.
- Artist-required metadata policy.
- Admin no-watermark scaffold for local testing.
- Low-weight render/audio sync quality ladder.
- Lite renderer for weak hardware.
- Static background cache instead of rebuilding grid/gradient every frame.
- Performance governor that auto-downgrades High → Auto → Eco → Lite when frame cost stays too high.
- Hidden-tab render pause.
- Debounced resize/recenter flow.
- Web Node draw caps and label suppression in low modes.
- Throttled floating artwork transforms.

## Planned / not built yet

- Google OAuth login.
- Stripe subscription checkout.
- Server-side entitlement checks.
- Server FFmpeg render queue.
- Account export counters.
- Weekly/monthly quota ledgers.
- Secure no-watermark entitlement enforcement.
- Cloud-hosted download storage or signed temporary links.

## Pricing roadmap

All pricing is planned in USD once accounts/server rendering exist:

| Tier | Price | Export plan |
|---|---:|---|
| Free | $0 | Watermarked Browser Record, 5/week. |
| Server FFmpeg | $3/month | 99 server FFmpeg exports/month. |
| Unlimited Creator | $7/month | Unlimited no-watermark Browser Record + server FFmpeg exports. |

## Honest production note

The current no-server build can generate local browser recordings and FFmpeg kits, but a real paid no-watermark product cannot depend on a client-side admin key. Paid entitlement must be verified server-side.


## v1.8.16 production-hardening verdict

The local single-file app is now suitable as a production-track no-server release candidate for creator testing. The remaining gap to a fully commercial SaaS platform is not renderer quality; it is account infrastructure: OAuth, Stripe, quota ledgers, secure entitlement checks, server FFmpeg rendering, abuse controls, and hosted storage.
