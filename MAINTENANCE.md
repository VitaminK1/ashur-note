# Maintenance Guide

This repository builds a ProperDocs/MkDocs Material site with a large amount of
game-reference content. Keep source edits small and verify generated output when
refactoring presentation helpers.

## Editing Rules

- Prefer Markdown for prose, lists, admonitions, and tables that do not need a
  custom layout.
- Use macros for repeated presentation patterns: speech bubbles, media figures,
  story cards, stat rows, preference icons, and tabbed blocks.
- Avoid adding raw `<br>` for spacing. Prefer paragraph breaks, list structure,
  or a CSS class that owns the spacing.
- Keep page-specific HTML in the smallest possible area. If a pattern is used
  twice, consider a macro or a shared CSS utility before copying it again.
- Do not move or rename generated assets unless every reference is checked with
  a strict build.
- `docs/navigation.md` currently uses empty child links for section index pages.
  Changing those labels is a visible navigation change, so do it in a separate
  content pass and compare the rendered navigation.

## CSS Layout

- `docs/css/box.css` owns story speech and tag styles.
- `docs/css/extra.css` owns global Material overrides and story card layouts.
- `docs/css/battle.css` owns battle, growth, preference-table, intimacy, and
  rank-list components that are used by growth/battle pages.
- `docs/css/relationship.css` owns the relationship page and imports shared
  preference-size tokens from `docs/css/prefs.css`.
- Keep new tokens in a small shared file when they are consumed by more than one
  component family.

## Macro Layout

- `main.py` is the central macro module.
- Keep path handling in `get_asset_path()` and `get_doc_path()`.
- Keep generated HTML defaults backward-compatible. When a macro is simplified,
  compare the generated page against a baseline build.
- Use `tabs()` when repeated tab blocks only differ by title and body.

## Verification

Run the strict build and script checks before finishing:

```powershell
properdocs build --strict -f properdocs.yml
node --check docs\javascripts\collapsible.js
node --check docs\javascripts\lore.js
```

For output-preserving refactors, use `tools\verify-site.ps1` to build a baseline
and a candidate site into `C:\tmp`, then compare generated files. Use
`-HtmlOnly` when CSS files are reorganized but rendered page content must remain
unchanged.
