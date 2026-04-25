# Admin Watermark Unlock

Voxel Audio includes a local admin watermark unlock scaffold.

## Export panel inputs

- Admin name
- Admin key

## Local admin key

```text
VOXEL-AUDIO-ADMIN
```

Entering the key unlocks no-watermark browser Record exports for the current browser/session and persists the unlock locally with `localStorage`.

## Important

This is a local/dev scaffold only.

For production, no-watermark must be controlled by server-side entitlement through:

- Google OAuth account identity
- Stripe subscription status
- server-side entitlement checks
- secure render worker policy

Client-side keys are not secure for real paid access control.

## Watermark wording

When watermark is active, the export watermark says:

```text
TIZWILDIN ENTERTAINMENT
A TizWildin Entertainment Product
```
