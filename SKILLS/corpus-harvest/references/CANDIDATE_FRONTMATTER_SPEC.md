# Candidate-file frontmatter — spec (corpus-harvest Stage 4 outputs)

Candidate markdown files awaiting Gate 2 carry the standard `music-file-intake`
Mode B frontmatter PLUS four corpus-harvest fields. Field names snake_case, tags
plain strings, must pass `yaml.safe_load` (01_SPECS/FRONTMATTER_SPEC.md).

```yaml
---
# ---- Mode B standard fields (music-file-intake SKILL.md, Step 4) ----
source: "<original source name — e.g. '12tone (YouTube), directive D03 extraction'>"
date_extracted: "YYYY-MM-DD"
date_ingested: "YYYY-MM-DD"
original_folder: "<staging folder, e.g. _CT_RESEARCH_INTAKE/<source_slug>/EXTRACTIONS/>"
source_type: extracted_doc
status: ingested
topic_tags: [tag1, tag2]
chapter_tags: ["02.3", "02.4"]
feeds_chapter: "02.4"
needs_tagging: false
ingested_by: "<agent name>"
# ---- corpus-harvest additions (plan v0.3 provenance contract) ----
rights_status: needs_review      # default; only Doug changes it
directive_id: "D03"
run_id: "r0007"
extraction_records: "EXTRACTIONS/D03/records.jsonl"   # the JSONL authority these sections render
---
```

Rules:

- `rights_status: needs_review` is the DEFAULT and survives until Doug rules.
- Chapter IDs: current `"01.1"`–`"04.9"` scheme only, read from
  `01_SPECS/CHAPTER_MAP.md` at run time — never the legacy `chNN` scheme,
  never guessed.
- Content-type tags, standard wikilinks, and `## NN.N — Title` heading format
  per music-file-intake Mode B. Doug's theory names appear only as
  "candidate evidence for [[X]]" (Hard Rail #7).
- The markdown body is generated FROM the extraction JSONL; if they disagree,
  the JSONL wins and the markdown is regenerated.
