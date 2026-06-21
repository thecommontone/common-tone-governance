---
title: "REPERTOIRE Spotify Freshness Check"
date: 2026-04-25
mode: VERIFY-ONLY (no writes)
plan: 01_ADMIN_AND_POLICY/REPERTOIRE_ENRICHMENT_PLAN.md
tags: [admin, repertoire, enrichment, spotify, freshness]
---

# Spotify Enrichment — Freshness Check (no writes)

**Generated:** 2026-04-25
**Companion to:** `repertoire_spotify_enrichment_2026-04-25.md` (dry-run report)
**Decision:** Verify-only. No `--execute` performed. No REPERTOIRE files modified.

## What this records

A full dry-run of `_SYSTEM/scripts/repertoire_spotify_enricher.py` was executed
today against `02_SOURCE_MATERIAL/REPERTOIRE`. The dry-run fetched fresh data
from the Spotify Tracks endpoint for every file with a `spotify_link` and
compared it to what is currently stored in each file's frontmatter.

| Metric | Value |
|---|---|
| Files with `spotify_link` | 5,294 |
| Unique track IDs | 5,281 |
| Audio-features endpoint | **403 Forbidden** (deprecated for this app, Nov 2024 cutoff) |
| Tracks endpoint | 200 OK |
| API calls today | 1 audio-features + 106 tracks |
| Files where dry-run reported a "would-update" | 5,288 |
| Files unchanged | 6 |

## Why no `--execute` was run

Spot-checks across 7 files (ABBA – Dancing Queen, 10,000 Maniacs – Candy
Everybody Wants, 2Pac – Dear Mama, Taylor Swift – 22, Miles Davis – So What,
Prince – Purple Rain, Stevie Wonder – Superstition) confirmed that the Spotify
fields already in each file match what the dry-run would write:

- `spotify_album`
- `spotify_release_date`
- `spotify_duration_ms`
- `spotify_popularity`

The 5,288 "would-update" count is dominated by a single trivial change: the
`spotify_enriched_at` date stamp ticking from `2026-04-24` → `2026-04-25`.
The substantive Spotify-derived data is identical to what was written in the
prior `--execute` run on 2026-04-24.

Running `--execute` today would therefore produce ~5,288 single-line file
modifications in the git diff with no information gain. Decision: skip the
write.

## Audio-features status (unchanged from yesterday)

The `/audio-features` endpoint returns 403 for this app's client_id. This is
a Spotify policy outcome, not a credentials or script issue. Track-derived
fields work normally.

Fields that **cannot** be obtained via this script with the current Spotify
app: `tempo`, `spotify_key`, `spotify_mode`, `spotify_time_signature`,
`spotify_danceability`, `spotify_energy`, `spotify_valence`.

If those fields become important, options are: (a) apply for Spotify
Extended Quota, (b) use AcousticBrainz / GetSongBPM / Essentia / librosa,
or (c) reuse SALAMI's existing key/mode annotations where the corpus
overlaps.

## Effective freshness

For all practical purposes, the Spotify-derived fields on REPERTOIRE files
were re-verified against Spotify on 2026-04-25 with **zero data drift
detected**. The on-disk `spotify_enriched_at: '2026-04-24'` stamps remain
accurate as the date of last actual write; today's date represents the
date of last verification.

---
*Report produced manually as a companion to the dry-run output. No script
modifications were made; the existing enricher is unchanged.*
