# SMPL Tones

**Project status: research and development specification. No working SMPL Tones application, model conversion or installer has been built or benchmarked.**

SMPL Tones is a planned, self-contained Windows application for converting complete songs and MIDI into editable sheet music. It combines replaceable local transcription engines, a full notation editor, optional stem separation, vocal transcription, tablature, playback and professional exports. Audio processing and AI inference will run on the user's computer, without a cloud service, account, first-launch download or required internet connection.

The project is intended for musicians, arrangers, teachers and composers who need an editable starting point from an existing performance. It will preserve the original audio and performance timing, make automatic decisions inspectable, and provide correction tools instead of claiming universally perfect transcription.

## Read the dossier

| Document | What it contains |
|---|---|
| [Research dossier](docs/RESEARCH.md) | The supplied Windows installers, Klangio browser investigation, eight deeply reviewed GitHub repositories, supplementary components, technical pipelines, limitations and reuse decisions. |
| [Development plan](docs/DEVELOPMENT_PLAN.md) | Product scope, fixed component choices, native architecture, engine contracts, twelve implementation milestones and acceptance criteria. |
| [Source index](docs/SOURCES.md) | Pinned source identities, 59 code references, official documentation and supplementary-source provenance. |
| [Evidence guide](docs/evidence/README.md) | Sanitized finding ledgers, input hashes, model metadata, API contracts, coverage limits and preservation boundaries. |
| [Decision ledger](docs/evidence/decision-ledger.json) | Which decisions changed during research and the final accepted product constraints. |
| [Roadmap](docs/ROADMAP.md) | The twelve planned milestones and links to their implementation issues. |
| [Third-party notices](THIRD_PARTY_NOTICES.md) | Code/model licensing distinctions and what this documentation release does and does not contain. |

Research date: **11 November 2026**. Findings describe the inspected artifacts and pinned source revisions at that time; they are not a claim about every release or product edition.

## Planned capabilities

- Import local audio/video, MIDI, MusicXML and native scores; record microphone, system audio and MIDI.
- Transcribe full mixes into instrument, vocal and percussion parts; process selected ranges or batches.
- Estimate beats/downbeats, maintain tempo maps and correct meter, quantization, swing and tuplets.
- Review source audio, waveform, piano roll and notation in synchronization; correct notes, parts, hands and voices.
- Generate stems, chord/key suggestions, lead sheets, simplified arrangements and editable lyric drafts.
- Edit full scores and individual parts, including guitar/bass/ukulele tablature, tuning and capo.
- Audition with a bundled soundfont; loop, slow playback, mute/solo and adjust part levels.
- Save recoverable projects; retain manual corrections when trying another engine or retranscribing.
- Export native projects, performance and quantized MIDI, MusicXML, PDF/parts, audio, GP5 and LilyPond text.

Every item above is **planned SMPL Tones functionality**, even where an upstream project already implements a similar feature.

## Design decisions

The target is Windows 11 x64. A separately branded application based on stable MuseScore 4.7.6 will provide the full editor and engraving model **inside SMPL Tones**. Users will not need a separate MuseScore installation. Native worker processes will provide replaceable inference engines through a versioned local protocol.

The default full-mix candidate is the author-published YourMT3+ **YPTF+Multi (PS)** checkpoint, subject to the provenance/licensing and native-inference gates in the development plan. Basic Pitch, Beat This, Demucs-based separation and whisper.cpp are selected for complementary roles. Source inference configurations are references, not proof that compact Windows deployment already works.

Earlier research favored MuScriptor's integrated audio-to-score workflow. The final requirement that bundled model terms permit commercial use excludes its CC BY-NC weights from the required installation. NeuralNote v2 uses that model family; choosing its runtime does not change those weight terms. Sheet Sage's restricted transcription weights are likewise excluded. These projects remain documented as technical references.

## Offline and installation promise

The finished product is intended to have one complete x64 installer containing the required models, runtimes, fonts and sounds. No separately installed music application, Python environment, external AI API, login or provider/model download will be required. Development-time conversion tools and build dependencies will not become end-user installation requirements.

The initial product excludes cloud transcription, social-link retrieval, online collaboration, model training, Android and a VST3 plugin. It implements the complete modern music workflow rather than packaging every historical file format or research framework.

## Performance and reliability targets

Initial budgets are **1.5 GiB compressed installer**, **3 GiB installed application/assets**, **500 MiB idle RAM** and **6 GiB working RAM** for the reference workflow. Balanced full-mix processing targets approximately real time on an i9-13900H / 32 GB RAM / RTX 4060 Laptop GPU with 8 GB VRAM. These are engineering targets; no measurements support them yet.

Core workflows must remain usable on CPU. Bounded processing, isolated workers, checkpoints, autosave, atomic saves and non-destructive reprocessing are required. See the [verification plan](docs/DEVELOPMENT_PLAN.md#verification-and-release-criteria) for the actual release gates.

## Research preservation

This repository preserves the analytical knowledge from the local investigations: all essential conclusions, artifact identities, reviewed commits, model contracts, selected code references and limitations. It does not depend on an active REA session or personal filesystem paths.

It is not a byte-for-byte backup of the original investigations. Repeating binary inspection requires the original input artifacts. Proprietary installers, extracted binaries/weights, complete manuals, source snapshots and copied production JavaScript are not published. The local investigation directories are not deleted by this publication.

## License and contribution status

Original repository material is licensed under **GPL-3.0-only**, matching the proposed application direction; see [LICENSE](LICENSE). Referenced upstream projects and models retain their own licenses. No third-party application source or model weights are bundled in this documentation release.

Implementation should follow the [development plan](docs/DEVELOPMENT_PLAN.md) and [roadmap issues](docs/ROADMAP.md). Claims of functionality, accuracy, offline operation or speed must be backed by the corresponding implementation and validation before appearing in a release description.
