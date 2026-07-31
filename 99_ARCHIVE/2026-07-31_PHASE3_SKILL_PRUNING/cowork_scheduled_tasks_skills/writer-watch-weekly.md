---
name: writer-watch-weekly-scheduled
description: Scheduled-task shim that invokes the writer-watch skill for the weekly Monday hunt across THE_WRITERS_DEN_ARCHIVE
---

Run the weekly writer-watch hunt.

VAULT STRUCTURE (authoritative — two-tier):
- $OUTER_VAULT = /Users/dougsmith/Docs/__MY_BOOK/
    Contains Cowork_log_file.md, RENDERS/, VAULT_MAPS/, and The_Common_Tone_Project/.
- $VAULT = $OUTER_VAULT/The_Common_Tone_Project/
- $DEN   = $OUTER_VAULT/THE_WRITERS_DEN_ARCHIVE/
    The scheduled task's working folder. Writer registry (WRITERS.md), per-writer
    subfolders of scraped Markdown, and dedup state all live here.

IMPORTANT — /Users/dougsmith/Documents/ is FORBIDDEN for Common Tone work.
Nothing from this project may ever be written to any path under /Users/dougsmith/Documents/,
even if a tool, mount, or environment variable seems to point there. If a path check
resolves anywhere under /Users/dougsmith/Documents/, STOP and flag the mount
misconfiguration in the Cowork log rather than writing the file.

Mounted sandbox equivalents:
- $OUTER_VAULT → /sessions/*/mnt/__MY_BOOK/
- $DEN        → <outer-mount>/THE_WRITERS_DEN_ARCHIVE/

Invoke the writer-watch skill. Follow its instructions exactly. Key anchors:
- Writer registry:  $DEN/WRITERS.md
- Scraped archive:  $DEN/by/<writer-subfolders>/
- Run log:          $DEN/_log/RUN_LOG.md   ← canonical run log for this task (skill convention)
- Weekly digests:   $DEN/_log/YYYY-Www_digest.md and YYYY-Www_digest_email.md
- Local cowork log: $DEN/Cowork_log_file.md   ← folder-local cowork log (for task events)
- Digest email:     composed as a DRAFT to thecommontone@gmail.com; not auto-sent

This task's granted folder is $DEN/ only. Do NOT attempt to write to the outer
$OUTER_VAULT/Cowork_log_file.md — that's outside the folder grant and will fail the
mount check. All logs stay inside $DEN/.

Output rules:
- All scraped article Markdown, per-writer folders, dedup state, and run logs MUST land
  inside $DEN/. Never write writer-watch artifacts to __MY_BOOK/ root, to
  The_Common_Tone_Project/, or to any legacy folder. NEVER anywhere under
  /Users/dougsmith/Documents/.
- New articles are saved as Markdown with frontmatter (source URL, date scraped, writer,
  title) — deduplicated against prior runs before being written.
- The weekly digest email to thecommontone@gmail.com is composed as a Gmail DRAFT for
  review. It is NOT sent automatically — Doug reviews and sends manually.
- If any required path resolves outside $DEN/ unexpectedly (mount misconfiguration), STOP
  and flag it as a red-box entry in the Cowork log rather than writing anywhere unsafe.

After the hunt completes, the writer-watch skill's own log_run.py appends to
$DEN/_log/RUN_LOG.md as its standard behavior. Additionally, prepend a short entry
to $DEN/Cowork_log_file.md — newest entry at the top — documenting the run date,
number of new articles found per writer, any scraping failures, and confirmation that
the digest draft was composed (with Gmail draft ID if available).
