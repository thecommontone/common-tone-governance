# General intake modes

This reference preserves the provider-neutral behavior of the pre-existing
Cowork `music-file-intake` skill. The live project governance and specifications
remain canonical; this file does not freeze folder maps, status vocabularies, or
chapter identifiers.

## Mode A — file routing

Use when an existing file needs classification and filing without substantive
extraction.

1. Inspect the source read-only and identify its provenance and current owner.
2. Read the live vault map, Research Domain Charter, frontmatter specification,
   and any destination-specific schema.
3. Propose the exact destination, filename, required conversion, duplicate
   risks, and whether the operation copies or moves the source.
4. Obtain Doug's authorization for the filesystem change. Never treat permission
   to inspect as permission to move or delete.
5. Convert external text material to governed Markdown at the Ingestion Gate.
   Keep binaries only where a live project rule expressly permits them.
6. Verify the resulting bytes and frontmatter. Report the source disposition.

Images require the live image-library rules. Repertoire material requires the
current CTSF specification and repertoire pipeline. This skill never writes the
textbook layer.

## Mode B — document extraction

Use for a PDF, DOCX, Pages document, handout, essay, pasted notes, or similar
source whose theory-relevant contents should become an Obsidian-ready research
file.

1. Preserve the source and record its identity. Extract text with the relevant
   document tool; use OCR only when necessary and label uncertainty.
2. Capture definitions, claims, examples, quotations, exercises, terminology,
   bibliographic details, and explicit disagreements. Keep fact, interpretation,
   and creator claim distinct.
3. Preserve exact quotations and page or location evidence. Do not invent a
   missing citation or silently repair ambiguous source text.
4. Classify against the current chapter map and research folders. Split only
   when one source genuinely feeds materially different governed destinations.
5. Create Markdown using the live `FRONTMATTER_SPEC.md`. Typical provenance
   fields include the original source, extraction and ingestion dates,
   `source_type: extracted_doc`, topic/chapter tags, primary chapter,
   `needs_tagging`, and the extracting agent; use only currently valid fields
   and values.
6. Deliver an ingestion summary: extracted item count, chapters served,
   evidence gaps, duplicate warnings, and exact filing recommendation.

Material that is primarily Doug's voice belongs in the voice-preservation
workflow; preserve it verbatim rather than treating it as ordinary source prose.

## Mode C — Consensus research synthesis

Use for structured Consensus.app exports containing questions, consensus
summaries, findings, and paper references.

1. Survey the whole export and identify each independent research question.
2. Plan a split by research question or coherent subject, not arbitrary length.
3. For each section, preserve the question, consensus strength, supporting and
   challenging evidence, population/context limits, paper-level links, and any
   uncertainty in the export.
4. Use the live frontmatter specification with
   `source_type: research_synthesis`; do not assert that every cited paper was
   independently opened unless it was.
5. Build or update bibliography CSV material only through the current canonical
   bibliography pipeline. Deduplicate by stable identifiers and links, flag
   collisions, and never delete a competing record automatically.
6. Report loaded-versus-unverified sources explicitly. A synthesis export is
   not itself proof that every underlying paper supports the generated wording.

## Conventions shared by all modes

- Cover relevant musical traditions without silently forcing every claim into a
  Western-theory frame.
- Preserve useful repertoire examples and credit their creators.
- Add Roman-numeral interpretation only as clearly labeled analysis, not as if
  it appeared in the source.
- Flag duplicates; Doug decides disposition.
- Use the current project specs rather than remembered chapter maps or status
  lists.
- Never invent, finish, or ghostwrite Doug's named theoretical concepts.
