Vinelife Wilmslow - Recent Changes Log

Date: 2026-02-21

Summary of recent edits:

- Restored the YouTube section to a simpler, earlier layout.
  - Reverted experimental visual helper classes (`box-drop`, `enhanced-shadow`, `muted-note`).
  - Kept the `glass-effect` style for the YouTube container.
  - Restored the iframe embed for the latest video and YouTube subscribe widget.

- Removed temporary helper stylesheet block that added extra box shadows and text effects.

- Removed helper classes from multiple sections (About, Founders, Services, Events, YouTube buttons) to return to the previous baseline styling.

Files changed:
- index.html (YouTube section and style cleanup)
- README.d (this changelog)

Notes:
- No build files were modified.
- If you want these UI experiments reapplied selectively, we can reintroduce a consistent `.glass` helper and apply it to chosen cards only.

Next steps (optional):
- Push changes to GitHub (requires remote `origin`).
- Reduce icon sizes in the YouTube action cards to responsive sizes.
- Reapply selective glassmorphism if desired.
