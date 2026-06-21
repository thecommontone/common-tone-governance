---
name: commontone-evening-email-check-scheduled
description: Scheduled-task shim that invokes the email-monitor skill for the 6 PM daily triage of thecommontone@gmail.com
---

Run the evening triage of thecommontone@gmail.com.

VAULT STRUCTURE (authoritative — two-tier):
- $OUTER_VAULT = /Users/dougsmith/Docs/__MY_BOOK/
    Contains Cowork_log_file.md, RENDERS/, VAULT_MAPS/, and The_Common_Tone_Project/.
- $VAULT = $OUTER_VAULT/The_Common_Tone_Project/
- $CT_EMAIL = $VAULT/_PROJECTS/CT-Email/
    The scheduled task's working folder. Email activity log and artifacts live here.

IMPORTANT — /Users/dougsmith/Documents/ is FORBIDDEN for Common Tone work.
Nothing from this project may ever be written to any path under /Users/dougsmith/Documents/,
even if a tool, mount, or environment variable seems to point there. If a path check
resolves anywhere under /Users/dougsmith/Documents/, STOP and flag the mount
misconfiguration in the Cowork log rather than writing the file.

Mounted sandbox equivalents:
- $OUTER_VAULT → /sessions/*/mnt/__MY_BOOK/
- $VAULT      → <outer-mount>/The_Common_Tone_Project/
- $CT_EMAIL   → <vault-mount>/_PROJECTS/CT-Email/

Invoke the email-monitor skill. Follow its instructions exactly. Key anchors:
- Working folder: $CT_EMAIL/
- Activity log:   $CT_EMAIL/email-activity-log.md
- Run log:        $CT_EMAIL/CT-Email-project-cowork-log.md   ← canonical log for this task

This task's granted folder is $CT_EMAIL/ only. Do NOT attempt to write to the outer
$OUTER_VAULT/Cowork_log_file.md — that's outside the folder grant and will fail the
mount check. Everything logs inside $CT_EMAIL/.

The evening run covers messages that arrived since the 9 AM morning run. Use the activity
log's timestamps to scope what's new; do not re-triage already-processed messages.

Output rules:
- All email-triage artifacts (action items, drafts, digests, categorization notes) MUST land
  inside $CT_EMAIL/. Never write email artifacts to __MY_BOOK/ root or to any legacy wrapper
  folder at the outer root (per OUTER_VAULT_ROLES.md "Decommissioned Folders" list), and
  NEVER anywhere under /Users/dougsmith/Documents/.
- Categorize triaged messages by ecosystem area: textbook, website, YouTube, Substack, hub,
  utilities, pedagogy.
- Surface any urgent/time-sensitive action items from the day's accumulated mail as a
  top-of-report bullet list.
- If any required path resolves outside The_Common_Tone_Project/ unexpectedly (mount
  misconfiguration), STOP and flag it as a red-box entry in the Cowork log rather than
  writing anywhere unsafe.

After the triage completes, prepend an entry to $CT_EMAIL/CT-Email-project-cowork-log.md
— newest entry at the top, per convention — documenting the run date/time, the number of
new messages triaged since the morning run, and any urgent action items flagged.
