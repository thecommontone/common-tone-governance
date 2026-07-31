# SALAMI Timeline Import Test — Anne Murray, "A Love Song"

Generated: 2026-05-01

## Test Target

| Field | Value |
|---|---|
| CTSF file | `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/ANNE_MURRAY - A_LOVE_SONG.md` |
| SALAMI song id | `532` |
| SALAMI file | `salami_0078.txt` |
| SALAMI title / artist | Anne Murray — A Love Song |
| SALAMI tonic | G |
| Crosswalk decision | Accept exact match for timeline import |

## Command

```bash
python3 - <<'PY'
import importlib.util
from pathlib import Path
root=Path('/Users/dougsmith/Docs/__MY_BOOK')
script=root/'_SYSTEM/scripts/salami_to_ctsf.py'
spec=importlib.util.spec_from_file_location('salami_to_ctsf_module', script)
mod=importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
print(mod.salami_to_ctsf(str(root/'SALAMI_PROJECT/salami_db.sqlite'), 'A Love Song', song_id=532))
PY
```

## Converter Output

```markdown
# A LOVE SONG — Anne Murray (G)

**Tonic:** G  **Estimated BPM:** ~133
**SALAMI Song ID:** 532

## Timeline

*Converted from SALAMI corpus (estimated tempo: ~133 BPM)*

### [Verse]  16 bars
I | I | I | I
ii | V | ii | V
I | I | I | I
ii | V | ii | V

### [Chorus]  16 bars
I | I | ii | V
ii | V | I | I
I | I/3 | ii | V
ii | V | I | I

### [Verse]  18 bars
I | I | I | I
ii | V | ii | V
I | I | I | I
ii | V | ii | V
IV | V

### [Chorus]  20 bars
I | I | ii | V
ii | V | I | I
I | I/3 | ii | V
ii | V | I | I
ii | V | IV | I
```

## Test Result

**PASS as draft import.** The converter successfully produced CTSF-style Roman-numeral timeline material from SALAMI `song_id=532`.

## Review Notes Before CTSF Writeback

- The output is musically useful as a draft timeline, but it is not yet a finished CTSF entry.
- The converter repeats `### [Verse]` and `### [Chorus]` section headers for later occurrences. Before writing to CTSF, either the `form:` array should represent repeated section labels cleanly or later occurrences should be renamed `Verse 2` / `Chorus 2` if the harmonic content differs.
- Estimated BPM `~133` is converter-derived and should not overwrite any trusted tempo without listening or external confirmation.
- SALAMI tonic `G` can be written as a proposed/imported source field, but should not automatically overwrite CTSF `tonic` until the import workflow is approved.
- The next safe implementation step is an import-preview mode that writes this kind of output to a report or staging file, then a reviewed writeback mode for the CTSF entry.
