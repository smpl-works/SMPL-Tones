# Evidence packet guide

This packet preserves the analytical knowledge from 11 November 2026 without an active REA session or a personal filesystem. It is a curated, sanitized archive, not a copy of every extraction or an executable software distribution.

## Normalized historical investigations

- [MuseHub installer and separate editor-source trace](dossiers/musehub-installer.json)
- [AudioScore package, component boundary and manual findings](dossiers/audioscore-demo.json)
- [AnthemScore bootstrapper, actual payload and model/viewer findings](dossiers/anthemscore.json)
- [Klangio browser/public-client findings](dossiers/klangio-studio.json)
- [Eight-repository source review](dossiers/github-review.json)

Earlier MuScriptor recommendations in historical records are retained as history. [The final decision ledger](decision-ledger.json) supersedes their component-selection implications after the requirement for commercially usable model terms was set.

## Identity, code and model records

- [Artifact identities](artifact-identities.json): supplied/acquired versions, sizes, hashes and observed signatures.
- [Original report manifest](archive-manifest.json): hashes/byte counts of the five original finding ledgers and their normalized equivalents.
- [AnthemScore graph metadata](anthemscore-models.json): six graph locations, hashes, producer/opset data, interfaces and operator/initializer counts, without weight files.
- [Klangio API inventory](klangio-client-api.json): 30 declared service methods and parameter/media-type context, not tested endpoints.
- [Browser observations](browser-observations.json): selected public UI, actions and boundaries; no account/session values.
- [84-file source manifest](source-manifest.json): repository/path/commit/Git blob identity and inspected-text digests; no copied source snapshots.
- [59 selected code references](code-references.json): pinned links, line numbers and the conclusion/context of each reference.
- [Earlier six-file MuseScore trace](musescore-source-trace.json): different source revision, not part of the MuseHub payload.
- [Planning-source identities and selected YourMT3+ checkpoint](planning-sources.json): source URLs, retrieval digests, model revision/hash and unvalidated deployment status.
- [Supplementary GitHub document identities](supplementary-github-sources.json): observed source URLs and immutable Git blob object URLs.
- [Global/per-case limitations](limitations.json): evidence and execution boundaries.
- [Roadmap definitions](roadmap.json): future milestones; issue metadata is added after submission.

## Preservation boundary

All essential conclusions are restated in the [research dossier](../RESEARCH.md), [appendices](../RESEARCH_APPENDICES.md) and these records. Unlinked original evidence filenames inside historical JSON are provenance labels; they do not indicate that excluded raw files are present or needed to understand the finding.

Proprietary installers, executables, model weights, complete manuals, source snapshots and the production browser bundle are deliberately absent. Personal Windows prefixes, emails and unrelated browser/account information are not part of this packet. The public source index supplies canonical references instead.

Re-running a binary investigation requires its original input. Vendor servers and versioned browser assets may change or disappear; hashes identify past inputs but do not recreate their bytes. No numerical transcription benchmark or native-export proof was run during this research.

Before removing any local working archive, verify a clean clone of this repository, open the dossier and evidence files, and retain original installers separately if future replay matters. Publication does not delete local data automatically.
