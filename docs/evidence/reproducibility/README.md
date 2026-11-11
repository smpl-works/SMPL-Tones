# Preservation audit and reproducibility records

Audit date: **11 November 2026**. The repository preserves the project knowledge, and this supplement closes additional provenance/method gaps found before considering local cleanup. Nothing in the local investigations was deleted or moved.

## What was added

- [Archive index](archive-index.json): sanitized metadata records and authored analysis-method reference texts, with original and archived hashes.
- [Local file inventory](local-file-inventory.json): relative filenames, sizes and SHA-256 identities for all files in the five original investigation folders. The files themselves are not thereby included.
- [REA envelope index](rea-envelope-index.json): selected original Evidence identities, subject digests, provider/operation/parameter information, result sections and coverage limitations. These are not full replayable REA records.
- [Preservation audit](preservation-audit.json): what is preserved, remaining raw-data boundaries and private-backup advice.

The extra metadata retains MuseHub resource/ZIP ranges, selected-member CRC/hashes and archive names; AudioScore verified Wise-stream offsets/checksums and installation-file/PE inventories; AnthemScore bootstrap/package acquisition and member/schema provenance; and Klangio acquisition, source-map status and exact JavaScript declaration/slice ranges.

The `methods` directory contains original analysis/extraction/acquisition/parsing scripts authored during the investigation, saved as `.txt` reference material. Machine-specific paths were replaced by explicit placeholders, and the Babel parser reference was normalized. Original file hashes and transformed-text hashes are both retained. These are **not ready-to-run tools**: adapting inputs, output directories and dependencies is necessary. No archived script, extractor, download routine, vendor executable or model was run during this audit.

`original_sha256` identifies the unmodified original local file bytes. `archived_sha256` identifies canonical UTF-8 text with LF line endings, matching the committed Git blob. A Windows checkout may use CRLF; normalize those line endings before comparing an archived-text digest.

HTTP headers were reduced to public identity-related fields such as ETag, content length/type and modification time. Personal absolute paths, tool-install prefixes, cookies/authorization headers and verbose embedded output previews were excluded. The original knowledge/evidence labels and limitations still apply.

## Can the local folders be removed?

**For understanding the findings and developing SMPL Tones:** the self-contained dossier, decision ledger, development plan and evidence supplement preserve the important project knowledge. Verify the published repository/clone first and keep the SMPL Tones repository itself.

**For exact forensic replay or a lossless archive:** the repository is intentionally insufficient. It does not contain original/extracted binaries, compressed packages, model bytes, complete manuals, the exact production browser bundle, all raw REA results or every source snapshot/log. Hashes identify missing bytes but cannot recreate them.

If replay matters, retain one private backup of the five original investigation directories before deleting the working copies. For a smaller backup, keep the three original supplied installers; the exact AnthemScore `6.3.100meta.7z`, `6.3.100content.7z` and `6.3.100AS_resources.7z` archives (or expanded equivalents); and the historical Klangio `index-DIr4Mtaw.js` asset plus raw REA bundle. The AnthemScore bootstrapper points at a mutable repository and the Klangio URL may disappear, so those two inputs cannot be assumed recoverable from the original links later.

The smaller selection is useful but is not a fully lossless backup of all research outputs. The original supplied MuseHub/AudioScore installers contain material that was extracted locally; the AnthemScore bootstrapper alone does not contain its inspected application payload.

The publication-helper directory is separate from the five investigated targets. It is unnecessary for reading the dossier or following the development plan, and its verification clone is a duplicate. No automated cleanup is performed by this audit or publication.
