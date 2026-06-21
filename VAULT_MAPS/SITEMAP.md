---
last_updated: 2026-05-01
current_map_file: sitemap_2026-05-01.md
vault_level: outer
---

# Current Outer Vault Sitemap — Pointer File

This file points to the most recently generated sitemap of the **outer vault**
(`__MY_BOOK/`). This covers all folders except `The_Common_Tone_Project/`, which
has its own separate sitemap at:
`The_Common_Tone_Project/01_ADMIN_AND_POLICY/VAULT_MAPS/SITEMAP.md`

**Current sitemap:** `sitemap_2026-05-01.md`

---

## Sitemap Archive

| Date | File | Notes |
|------|------|-------|
| 2026-05-01 | `sitemap_2026-05-01.md` | Refresh — 64,526 outer files indexed, 37.5 GB, stat-only mode; excludes `The_Common_Tone_Project/` per two-sitemap system |
| 2026-04-21 | `sitemap_2026-04-21.md` | Initial run — 37,192 files, 16.0 GB, stat-only mode |
| 2026-04-21 | `sitemap_2026-04-21.md` | Post-thinning refresh — 34,066 files, 11.1 MB sitemap, stat-only mode |

---

## How to Use This Sitemap

**For humans:** Open `sitemap_2026-05-01.md`. Use Cmd+F to search by filename,
folder name, or extension. The **Domain Index** section is organized by top-level
folder — ideal for housekeeping and migration planning.

**For AI assistants:** Start with the **Quick-Find Guide** and **Folder Tree**
sections. For targeted file searches, grep the **Flat File Index** (one line per
file, format: `path · size · modified`). This is a stat-only scan — titles and
tags are not extracted; use the inner vault sitemap for rich metadata on book content.

**When to regenerate:**
- After adding, moving, or deleting outer vault folders
- Before/after any migration from outer vault into the inner sanctum
- Run the `vault-sitemap` skill in Cowork to regenerate.

---

## Two-Sitemap System

| Sitemap | Root | Scope | Mode |
|---------|------|-------|------|
| This file | `__MY_BOOK/VAULT_MAPS/SITEMAP.md` | Outer vault (staging, legacy, raw) | stat-only |
| Inner sitemap | `The_Common_Tone_Project/01_ADMIN_AND_POLICY/VAULT_MAPS/SITEMAP.md` | Inner sanctum (authoritative book content) | full (frontmatter + word counts) |
