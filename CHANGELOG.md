# Changelog

## v1.8.10 — Restore Browser MP4 with direct audio capture

- Restored Browser Record MP4 as an available option.
- Changed recorder audio capture priority to direct `<audio>.captureStream()` first.
- Kept WebAudio MediaStreamDestination as fallback.
- Added mixed stream audio/video track verification before recording starts.
- Added detailed recorder audio-policy logs.
- Added `docs/MP4_DIRECT_AUDIO_RESTORE.md`.

## v1.8.7 — Longer side metadata end pause

- Increased the end pause on the small side metadata scroll before it resets.
- Kept scroll speed, start pause, and main title rendering unchanged.
- Added `docs/SIDE_METADATA_END_PAUSE.md`.

## v1.8.6 — Preview side-scroll clock fix

- Fixed the Live Export Preview side metadata line not visibly scrolling.
- Root cause: preview was passing `performance.now()` every frame, resetting the animation timer.
- Added a persistent preview clock so the side metadata line now scrolls correctly.
- Main title rendering remains untouched.
- Added `docs/PREVIEW_SCROLL_CLOCK_FIX.md`.

## v1.8.5 — Side metadata scroll fix

- Fixed only the small `VOXEL AUDIO EXPORT • song • artist/feat` side text line.
- Added a clipped safe scrolling lane so long metadata cannot overlap the reactive circle.
- Main export title rendering is untouched and remains reverted to v1.8.1/v1.8.4 behavior.
- Added `docs/SIDE_METADATA_SCROLL_FIX.md`.

## v1.8.4 — Revert title marquee experiment

- Reverted the v1.8.2/v1.8.3 title marquee changes.
- Restored the export title renderer to v1.8.1 behavior.
- Removed title animation, ghost repeat behavior, title safe-box shrink, and title fade logic.
- Kept v1.8.1 Song Title Authority intact so Song name still beats filename.
- Added `docs/TITLE_RENDER_REVERT.md`.

## v1.8.1 — Song title authority fix

- Fixed preview/export title authority so the visible Song name wins over raw filename.
- Added lightweight ID3v2 MP3 `TIT2` reader and WAV/RIFF `INAM` reader for embedded song titles.
- Browser Hub, hover cards, Now Playing, preview canvas, browser Record filenames, vault names, binding maps, and FFmpeg manifest now prefer the canonical song title.
- Filename is now treated only as a fallback and original source-file trace, not the public export title.
- Manual Song name edits persist onto the selected track and update the preview/export path live.

## v1.8.0 — Production hardening / weak-hardware renderer

- Added `Quality: Lite`.
- Added automatic performance governor: High → Auto → Eco → Lite.
- Added static background cache for the main canvas.
- Added hidden-tab render skip.
- Added debounced resize handling.
- Added Web Node draw caps in low modes.
- Suppressed registry labels when low-quality modes disable labels.
- Throttled floating artwork transform updates in Lite/Eco.
- Reduced analyser loop work further in Lite.
- Updated docs for production status, performance tuning, and release readiness.
- Fixed package `check:js` so syntax validation fails properly instead of being ignored.


## 1.7.1 — Documentation Audit + Reset/Back Binding Alignment

- Added `docs/EXTENSIVE_AUDIT_REPORT.md` with package scope, confirmed behavior, known constraints, and next engineering pass.
- Added `docs/PERFORMANCE_TUNING.md` for weak hardware, Eco mode, sync drift, and production workflow guidance.
- Added `docs/RELEASE_STATUS.md` to clearly separate ready local features from planned Google OAuth/Stripe/server FFmpeg systems.
- Added `docs/OPERATOR_MANUAL.md` as the practical usage guide.
- Expanded architecture docs with render/sync model and exact quality ladder.
- Updated troubleshooting docs for lag, sync drift, browser recording failures, and admin unlock persistence.
- Corrected Reset/Back button bindings so they call the intended helper functions.
- Aligned Reset so it clears the loaded track registry before returning to startup/demo state.


## 1.7.0 — Low-Weight Render Sync Pass

- Added split render clocks for voxel scene, waveform, and audio analyser.
- Lowered Eco/Auto GPU and FFT pressure for weak hardware.
- Disabled expensive web glow shadows outside High quality.
- Added low-weight docs for recommended weak-hardware settings.


## 1.6.9 — Reset and Back Behavior Fix

- Reset now hard-resets the app back to startup state.
- Back now exits preview/panels/folder focus/search/selection/zoom without deleting loaded audio.
- Recenter now only recenters current view.
- Added `docs/RESET_AND_BACK_BEHAVIOR.md`.

## 1.6.8 — PlayTrack Color Sync Fix

- Fixed real audio voxel clicks not updating Export color.
- `playTrack()` now calls `setAccentFromTrack(tr)` and `syncExportAccentFromTrack(tr)` in the audio-file branch.
- Added `docs/PLAYTRACK_COLOR_SYNC_FIX.md`.

## 1.6.7 — Voxel Click Color Sync Fix

- Fixed selected voxel click not changing export color.
- Selecting/clicking a voxel now clears manual color override.
- Export color picker still allows manual override after selection.
- Crosscheck now labels active color as selected voxel or manual override.
- Added `docs/VOXEL_CLICK_COLOR_SYNC_FIX.md`.

## 1.6.6 — Artist Required / 36 Character Cap

- Artist input is now required before Preview, Record, or MP4 Kit export.
- Artist field is capped at 36 characters.
- Artist name is locked into export metadata when export starts.
- Crosscheck now validates Artist requirement.
- Vault Re-export requires Artist metadata.
- Added `docs/ARTIST_REQUIRED_POLICY.md`.

## 1.6.5 — Vault Edit and Re-export

- Session Export Vault items now include editable metadata fields.
- Vault items can edit Song name, Artist, Feat, Description, and Export color.
- Added Re-export button per vault item.
- Re-export restores metadata and re-runs the same browser Record mode.
- Added `docs/VAULT_EDIT_AND_REEXPORT.md`.

## 1.6.4 — Session Export Vault Visibility

- Added Vault button to the Quick Dock.
- Session Export Vault now opens automatically after successful Browser Record.
- Added empty-state text explaining when no exports exist yet.
- Added Close button to the vault panel.
- Enlarged vault panel for easier download access.
- Added `docs/SESSION_EXPORT_VAULT_VISIBILITY.md`.

## 1.6.3 — Admin Preview Unlock + Single Export Color

- Admin unlock now clearly removes watermark in Live Preview and Browser Record.
- Admin status hint now says whether the current export is clean or watermarked.
- Preflight/Crosscheck now reports audio, image, watermark status, and export color.
- Added single Export color chooser for the selected audio export.
- Export color defaults to selected voxel color and can be overridden.
- Added `docs/ADMIN_PREVIEW_UNLOCK_AND_COLOR.md`.

## 1.6.2 — TizWildin Watermark Branding

- Changed active watermark wording to TizWildin Entertainment branding.
- Watermark now says:
  - `TIZWILDIN ENTERTAINMENT`
  - `A TizWildin Entertainment Product`
- Added `docs/TIZWILDIN_WATERMARK_BRANDING.md`.

## 1.6.1 — Admin Watermark Unlock

- Added Admin name input.
- Added Admin key input.
- Added Unlock No-Watermark and Lock Watermark controls.
- Browser Record watermark is skipped when admin unlock is active.
- Admin unlock persists locally with localStorage.
- Added `docs/ADMIN_WATERMARK_UNLOCK.md`.
- Documented that client-side admin key is a local/dev scaffold only.

## 1.6.0 — Export Overlap Cleanup

- Moved watermark out of waveform area into a compact top-right dock.
- Added ellipsis fitting for metadata row.
- Narrowed metadata/description capsule to reserve clear space for the reactive circle.
- Repositioned and slightly reduced reactive circle.
- Added `docs/EXPORT_OVERLAP_CLEANUP.md`.

## 1.5.9 — Full Selected Voxel Color Sync

- Export layout now colors all major visual elements from the selected song voxel color.
- Metadata text, title glow, panel borders, cover outline, waveform, progress, watermark, and background glow now sync to the selected voxel.
- Preview/export panel borders also sync to selected voxel color.
- Added `docs/SELECTED_VOXEL_COLOR_POLICY.md`.

## 1.5.8 — Compact Blank-Description Layout

- Blank Description now collapses to a compact visualizer capsule.
- Empty description text is not rendered.
- Metadata panel becomes shorter when Description is blank.
- Reactive circle becomes slightly larger in compact mode.
- Added `docs/COMPACT_BLANK_DESCRIPTION_LAYOUT.md`.

## 1.5.7 — Optional Description Behavior

- Description field is now truly optional.
- Blank Description no longer auto-fills.
- Blank Description renders no description text in export preview/record.
- Updated placeholder text to clarify that blank means no description.
- Added `docs/OPTIONAL_DESCRIPTION_POLICY.md`.

## 1.5.6 — Rounded Rectangle Clamp Fix

- Fixed giant foreground green shape in export preview/record.
- Root cause was `drawRoundedRect()` allowing radius `999` on a 6px-high progress bar.
- Radius now clamps to `min(radius, width/2, height/2)`.
- Export progress bar radius changed from `999` to `3`.
- Added `docs/ROUND_RECT_RADIUS_FIX.md`.

## 1.5.5 — No Foreground Accent Shapes

- Removed large RGB blob/triangle accent fills from the export renderer.
- Added safe radial background glow helper.
- Reset composite mode before cover and panel rendering.
- Guaranteed accent color cannot cover the image, title, description panel, or waveform panel.
- Added `docs/EXPORT_NO_FOREGROUND_SHAPES.md`.

## 1.5.4 — Export Metadata / Layering Fix

- Added editable Artist field.
- Added editable Feat field.
- Added editable Description field.
- Description defaults to `full-track reactive visualizer`.
- Export renderer now keeps RGB accent shapes behind cover art and panels.
- Rebuilt export layer order to prevent colored shapes covering the image.
- Reactive circle now visualizes bass, mids, treble, and frequency spokes.
- Single-track FFmpeg kit manifest stores title, description, artist, and feat metadata.
- Added `docs/EXPORT_METADATA_FIELDS.md`.
- Added `docs/EXPORT_LAYERING_POLICY.md`.

## 1.5.3 — Image-Required Export Policy

- Preview Export is blocked until selected song has bound artwork.
- 10s Record and Record Full are blocked until selected song has bound artwork.
- Build MP4 Kit is blocked until selected song has the original bound image file.
- Album Kit now gives clearer artwork coverage errors.
- Added `docs/IMAGE_REQUIRED_EXPORT_POLICY.md`.
- Added image-required route documentation.
- Added clearer runtime messages when image is missing.

## 1.5.2 — Runtime Async Freeze Fix

- Fixed browser runtime error: `ReferenceError: async is not defined`.
- Removed stray standalone `async` token before `getExportTitle`.
- Preserved compact topbar / Quick Dock layout.
- App no longer freezes during startup from that generated token issue.

## 1.5.1 — Hotbar Cleanup / Freeze Guard

- Removed duplicated Quick Dock actions from the visible top scroll bar.
- Kept hidden file inputs functional for Quick Dock buttons.
- Added binding map export button to Quick Dock.
- Added optional-control guards so missing controls do not freeze startup.
- Added runtime error and promise rejection diagnostics.
- Added `docs/HOTBAR_AND_FREEZE_GUARD.md`.

## 1.5.0 — Proto-Synth Platform Hardening

- Positioned Voxel Audio as powered by Proto-Synth Grid Engine.
- Added Proto-Synth engine integration docs.
- Added in-app Proto-Synth Engine docs route.
- Added fixed Engine quick-dock button.
- Added browser Record watermark scaffold.
- Added local settings persistence scaffold.
- Added Export Bindings / Import Bindings controls.
- Added binding-map docs.
- Added watermark policy docs.
- Preserved Session Export Vault, no-server local mode, browser Record, MP4 Kit, and Album Route Builder.

## 1.4.5 — Session Export Vault

- Added Session Export Vault panel.
- Browser Record exports are now retained in memory after completion.
- Last 9 browser Record exports can be downloaded again.
- Fixes missed/hidden browser save prompt issue.
- Vault is local session-only and clears on page reload/close.
- Added `docs/SESSION_EXPORT_VAULT.md`.

## 1.4.4 — USD Three-Tier Pricing Plan

- Clarified all prices are USD.
- Added $7 USD/month Unlimited Creator tier.
- Unlimited Creator tier includes unlimited no-watermark browser Record exports.
- Unlimited Creator tier includes unlimited no-watermark server FFmpeg exports.
- Preserved $3 USD/month tier for 99 server FFmpeg exports/month.
- Preserved free tier: watermarked browser Record exports, 5 exports/week.
- Updated README, Info route, pricing docs, monetization architecture, SEO docs, export workflows, and package metadata.

## 1.4.3 — Account Pricing / Export Quotas Plan

- Replaced prior $7/month unlimited/no-watermark plan.
- Added planned free account export model:
  - browser Record exports
  - watermark
  - 5 exports/week
- Added planned paid server FFmpeg model:
  - $3/month
  - 99 FFmpeg exports/month
- Added Google OAuth and Stripe integration requirements.
- Added `docs/MONETIZATION_AND_ACCOUNTS.md`.
- Updated README, Info route, SEO docs, and export workflow docs.

## 1.4.2 — Pro Version Positioning

- Added Voxel Audio Pro positioning.
- Planned Pro price documented as `$7/month`.
- Planned Pro benefits documented as no watermark and unlimited exports.
- Added in-app Info route for Pro Version.
- Added `docs/PRO_VERSION.md`.
- Updated README, SEO, and export workflow docs.

## 1.4.1 — Local Reliability / Quick Dock Fix

- Added fixed Quick Dock for critical actions.
- Added startup self-test diagnostics.
- Hardened file input hiding so native "No file chosen" text does not appear in the scene.
- Added "Nothing Works?" docs route.
- Added scan/load diagnostic messages.
- Preserved no-server local mode and browser Record feature.

## 1.4.0 — No-Server Local + Record Feature Hardening

- Reinforced no-server local app positioning.
- Added `docs/NO_SERVER_LOCAL_MODE.md`.
- Added `docs/BROWSER_RECORD_FEATURE.md`.
- Added in-app No-Server Local docs route.
- Clarified Browser Record as normal-speed local recording feature.
- Updated public README and metadata for local/offline/no-server SEO.
- Kept deterministic FFmpeg MP4 Kit as final production path.

## 1.3.0 — Professional Public Repo Release

- Packaged Voxel Audio as a public-facing GitHub-ready repository.
- Added full README with SEO positioning.
- Added docs routing.
- Added architecture, export, album, troubleshooting, SEO, and development docs.
- Added GitHub issue templates and CI.
- Preserved latest app build:
  - local audio folder voxel directory
  - live export preview
  - browser record export
  - deterministic MP4 kit
  - album route builder
  - album color controls
  - info/docs overlay
  - smooth export waveform

## 1.2.9 — Album Route + RGB Sync

- Added full album route builder.
- Added per-track and album-wide color controls.
- Added album FFmpeg kit export.
- App/export accent syncs to selected song voxel RGB.

## 1.2.8 — Smooth Export Waveform

- Added waveform smoothing buffers.
- Browser Record capture requests 60 FPS.
- FFmpeg scripts request 60 FPS output.

## 1.2.7 — Info Docs Overlay

- Added route-based in-app docs overlay.

## 1.2.6 — Live Export Preview

- Added scaled 1280×720 live export preview.

## 1.2.5 — Panel Fit / Recenter

- Fixed Browser Hub height.
- Added internal scrolling and Recenter.

## 1.2.4 — Color-Synced Title Export

- Added Song name input.
- Export accent uses selected track voxel color.

## 1.2.3 — Normal-Speed Browser Record

- Browser Record locked to normal 1x song speed.

## 1.2.0 — Hybrid Export

- Added both browser recording and FFmpeg kit export paths.
