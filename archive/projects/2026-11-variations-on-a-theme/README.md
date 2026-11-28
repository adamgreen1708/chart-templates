# Variations on a Theme — Exhibit 003

Approved 23-second simulated gallery camera journey; four panels from the supplied dot portrait, displayed as large canvases. No blog post. Publication image is a JPEG derived from the approved still, and the film is an optimised H.264 encode of the approved video (1600 × 900, 30 fps, 690 frames, 23 seconds). No change to composition, camera timing or artwork. The publication MP4 is 5,374,379 bytes. Both release files are locked in ASSETS.sha256. A more aggressively compressed version was rejected at visual QA because it lost dot detail.

For every release, stage the complete media first, verify its SHA-256 manifest, run scripts/validate_gallery_assets.py before Jekyll and with --built _site after Jekyll, check mobile playback and links, then merge only after CI succeeds. Never merge missing media. Keep one-time transfer workflows and temporary chunks out of the final merged tree.
