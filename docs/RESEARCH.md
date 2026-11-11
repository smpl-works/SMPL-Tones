# SMPL Tones research dossier

**Research date: 11 November 2026. Status: historical investigations and a future product specification. No SMPL Tones application has been implemented.**

## How to read this dossier

The original task was to find Windows software, preferably downloadable, that converts audio or MIDI into complete sheet music. The important input was a **finished song with several instruments and/or vocals**, not simply a clean piano recording. The work then expanded into GitHub architecture reviews, REA investigations of three supplied installers, observation of Klangio's browser application, and planning a self-contained Windows app.

This document preserves the substantive conclusions without requiring the original local analysis folders. Supporting metadata is in [the evidence packet](evidence/README.md); [the appendices](RESEARCH_APPENDICES.md) preserve identities, graph contracts and declared routes; [the source index](SOURCES.md) preserves source references. Original filenames mentioned in historical ledgers are provenance labels, not required attachments.

The investigations answer **how the inspected implementations are structured**. They do not establish which model is most accurate on the same songs. No supplied installer or music application was run, no audio was uploaded to Klangio, no model inference or conversion benchmark was performed, and no released binary was proved equivalent to the inspected public source.

### Evidence vocabulary

| Label | Meaning |
|---|---|
| **Observed UI** | A visible interface was inspected. This does not prove that an offered action completed. |
| **Inspected source** | A specified source revision contains the described implementation. |
| **Static artifact evidence** | An executable/package contains the stated resource, metadata, import, graph or encoded reference. |
| **Documented capability** | A vendor/author manual or README describes the capability; it was not necessarily exercised. |
| **Inference** | A likely interpretation corroborated by context, with its boundary stated. |
| **Unknown** | The investigation did not establish the behavior or implementation. |

REA (the reverse-engineer-anything skill, called “RAE” in the conversation) was used for shipped-artifact and browser-source investigations. Ordinary source repositories were reviewed directly, as that skill instructs. REA CLI 6.8.0 ran on an existing bundled Node runtime. A native function-level decompiler was unavailable. Portable PE resources, managed metadata/CIL, package structures and focused JavaScript analysis supplied narrower evidence. Ordinary Python extraction and ONNX metadata parsing were labeled separately rather than misrepresented as REA-generated results.

## The engineering problem

“Audio to sheet music” spans several independent tasks:

1. Decode media and establish a time reference.
2. Optionally separate source audio into stems.
3. Recognize pitches, note boundaries, instruments, voices and percussion.
4. Estimate beats, downbeats, tempo, meter and performance timing.
5. Convert timestamps into meaningful written durations, rests, ties, tuplets and voices.
6. Construct parts, staves, clefs, key signatures, chord symbols and lyrics.
7. Engrave, edit, audition and export the score.

MIDI already supplies symbolic events, so it can enter after recognition. It still may contain expressive timing that needs interpretation. MusicXML contains more notation structure. A stem is reconstructed audio, not a notated part. A lead sheet is melody plus harmony, not a complete instrumental reconstruction. Polyphonic pitch recognition does not by itself identify the source instrument of each note.

These distinctions explain why several reviewed tools complement each other and why printing the output of a note detector is insufficient for readable music.

## Product and repository map

| Subject | Main responsibility | Relevant output | Investigation depth |
|---|---|---|---|
| MuseHub installer | Delivery/management of another application | Installer/launcher workflow | Static supplied artifact |
| MuseScore Studio | Symbolic score editing and engraving | Native score, MusicXML, PDF, MIDI, audio | Targeted pinned source; separate from installer |
| AudioScore Ultimate | Audio analysis, corrections and score creation | Score, MIDI/MusicXML and documented full-product exports | Package, managed boundary and bundled manuals |
| AnthemScore | Integrated recognition and correction workflow | MusicXML, score view, PDF/MIDI paths | Package, embedded models and viewer assets |
| Klangio Studio | Hosted transcription with browser editing | Structured score and server-requested exports | Visible input UI and public client source |
| MuScriptor | Full-mix recognition, timing cleanup and engraving integration | MIDI plus MuseScore-generated sheets | Targeted pinned source |
| NeuralNote v2 | Desktop/DAW workflow around MuScriptor | Multitrack MIDI and playback | Targeted pinned source and native dependency |
| Basic Pitch | Lightweight polyphonic pitch/note recognition | Notes, bends and MIDI | Targeted pinned source |
| MT3 | Research multitrack event prediction | NoteSequence/MIDI | Targeted pinned source/notebook |
| Omnizart | Separate music-analysis tasks | Task-specific MIDI/CSV/contours | Targeted pinned source |
| Sheet Sage | Melody-and-chord lead sheets | LilyPond, PDF and aligned MIDI | Targeted pinned source |
| UVR | Source separation | Audio stems | Targeted pinned inference/model source |

The eight-repository review acquired 84 source/documentation files and retained 59 selected code references, including the `muscriptor.cpp` dependency. “Acquired” is not a claim that every line or subsystem was comprehensively audited. Supplementary planning sources receive narrower labels below.

## 1. MuseHub installer and MuseScore Studio

### Supplied artifact: delivery rather than the editor

**Static artifact evidence.** The supplied `MuseScore_Studio_Installer_via_MuseHub.exe` was a signed native x64 **MuseHub Installer 3.6.0.2400**. The observed signer was MUSECY SM LTD. The input was 36,818,352 bytes, with SHA-256 `d9eea2ae7c8c7babc0c98a3d3b3591e2295eec02e362791836e7fe2d911caee2`.

An embedded `ZIP_MUSEHUB` resource begins at offset 950,496 and spans 35,798,508 bytes. The archive inventory contains 108 entries including directories, with 135,511,537 uncompressed bytes. It names MuseHub, updater/uninstaller components, authorization service components, Windows UI/runtime libraries, fonts and localization. It does not list a separately named MuseScore editor executable.

The ZIP uses compression method 95/XZ, which the initial extraction paths did not support. A format-aware standard-library decoder recovered six selected members. CRC32 checks passed, and the five non-manifest files matched the package's manifest hashes. This establishes integrity of those recovered files, not an executed installation or complete materialization of every archive entry.

The PE manifest declares administrator elevation. Installer messages reference staging, verification, moving aside an existing installation, registration, authorization/updater services and launching MuseHub. A MuseScore-specific deep link points into MuseHub's product store. **Inference:** these references outline its installation/launch responsibilities. Native branches, exact ordering, actual registry writes, networking and services were not dynamically verified.

### Editor functionality and implementation

**Inspected source / documented capability.** MuseScore Studio is a C++/Qt notation editor for composers, arrangers and musicians working with symbolic music. Relevant inputs include MIDI, MusicXML/MXL and native scores, with additional format readers. Users can edit notes, voices, parts, staves, keys, clefs, articulations, lyrics, notation and page layout; audition the result; and create printed/PDF scores and individual parts.

The targeted MIDI path is:

`MIDI reader → importMidi/convertMidi → track/instrument analysis → timing and voice processing → score construction → notation layout → export`

The importer groups musical events, handles timing, splits piano hands and drum voices/tracks, quantizes notes, deals with tuplets and differing durations, assigns instruments and constructs measures and score elements. These are musical interpretations of symbolic events, not waveform pitch recognition. The internal engraving model represents the resulting score; notation painting and output writers are separate layers.

MusicXML writing serializes the internal score. PDF writing creates a Qt `QPdfWriter` and asks the notation painting layer to draw pages. Per-part and multipart output are supported by the inspected writer. Audio-export registration includes score-to-audio writers; those registrations do not establish an audio-to-note input engine.

Two source traces must remain distinct: an earlier six-file trace pinned `701d557996fb0da981bc20e567d4c8efbe2433c7`, and the broader repository review pinned `82ba7e5736f7e5a3466de77c07cba0950c86606b`. Neither proves what editor version the supplied MuseHub installer would fetch.

Planning later checked that reviewed `main` identified itself as an unstable 5.0 prerelease. Stable **v4.7.6**, commit `96480d58445e3b24b230a3fe7d4725d639aa2eb3`, is the proposed application base. Its build is C++17/Qt-based. The Guitar Pro module inspected at this stable commit registers readers, not a writer; GP5 export therefore requires new work.

### Windows, licensing and reuse

MuseScore provides a native Windows editor. The inspected source headers are GPL-3.0-only; fonts, sounds and dependencies have additional notices. SMPL Tones should integrate a separately branded editor from the stable codebase, rather than requiring another installed application or invoking an online delivery manager. It should keep mature editing, engraving and import/export behavior while removing required cloud/download/account behavior.

**Unknowns:** no editor build or runtime conversion was tested; public-source behavior was not matched to a released editor binary; the analysis did not exhaust every plugin or optional product. Bad recognized notes cannot be corrected merely by engraving them. [Historical evidence](evidence/dossiers/musehub-installer.json), [source trace](evidence/musescore-source-trace.json), [stable release](https://github.com/musescore/MuseScore/releases/tag/v4.7.6).

## 2. AudioScore Ultimate 2020 Demo

### Product and functionality

**Documented capability.** AudioScore targets users who want to recognize music from recordings, correct it and produce notation or transfer the result into another score editor. The full-product documentation describes CD/MP3/WAV/MIDI input, microphone and MIDI-keyboard entry, instrument tracks, note corrections, score preview, score creation and Sibelius integration. MusicXML, NIFF, MIDI and Windows PDF output are documented for relevant full editions. These descriptions are not proof that the demo enables every export.

The workflow emphasizes a correction stage: recognize notes; inspect sensitivity and note counts; set/check time signature and barlines; correct instrument assignments and split/join notes; create editable tracks and a score preview; then create or export the formatted score.

### Supplied package and technical boundary

**Static artifact evidence.** `AudioScoreUltimateDemo.EXE` was a signed Neuratron Limited Wise installer, 16,972,520 bytes, SHA-256 `106dd615004840f3fc1a2e9986a733e32eff4c983b35e15b5af120080e69333e`. It identifies AudioScore Ultimate 2020 Demo, installer version 9.0.0, and an outer x86 PE with an administrator manifest.

The investigation recovered 102 contiguous raw-DEFLATE streams totaling 29,813,905 uncompressed bytes, with CRC32 verification for every retained stream. The count is not a count of installed files. Final metadata/padding/certificate-tail material was not interpreted. A recovered Wise installation script supplied human-readable packaging context.

The actual editor was a native x86 `Neuratron AudioScore.exe`, 9,872,896 bytes, version 9.0.0.0. Supporting components include an x64 .NET Framework WPF `Infinity Ripper.exe` helper and an x64 mixed C++/CLI `HitnMixLibCLR.x64.dll` bridge. Managed metadata and CIL establish encoded calls from window/background-work/stop/close paths into initialization, status, stopping and deinitialization wrappers, which cross into native Hit’n’Mix functions.

These observations explain the component boundary and lifecycle. They do not recover the native pitch-recognition algorithm, a specific neural architecture, interprocess protocol or dynamic sequence of calls. The main application SHA-256 and helper identities/call tokens are retained in [the finding ledger](evidence/dossiers/audioscore-demo.json).

### Limits important for full songs

The bundled manual describes up to **16 simultaneous notes**, which must not be rewritten as guaranteed isolation of 16 independent instruments. It states that percussion recognition is outside its design, that two instruments sharing a simultaneous pitch cannot be separated, and that heavy sustain/reverb makes rhythm recognition harder. These are consequential limits for finished band recordings.

Manual correction of timing, barlines and assignments is part of the intended workflow. Shared product resources contain names and limit messages belonging to other editions/products. In particular, generic helper messages were not treated as a reliable AudioScore-specific demo-duration limit. No application was run to establish edition enforcement.

### Relevance to SMPL Tones

The useful reference is its human-in-the-loop pipeline and separation of raw recognition from notation preparation. SMPL Tones should make barlines, note durations, instrument assignments and score preview easy to correct, preserve source timing and provide cancellation/recovery around long jobs. The proprietary native engine and extracted payloads are not reusable project dependencies. [Official manual reference](https://www.neuratron.com/downloads/NASHelp.pdf), [archived evidence](evidence/dossiers/audioscore-demo.json).

## 3. AnthemScore

### Product and delivery identity

AnthemScore is a downloadable Windows audio-to-notation product with recognition, timing/part corrections and score exports. Its user-facing workflow includes note detection, instrument assignment, percussion handling, editing and a notation viewer.

**Static artifact evidence.** The supplied `AnthemScore_installer_windows_x86_64.exe` was a signed Lunaverus LLC online bootstrapper, not a self-contained application payload. It uses Qt Installer Framework **4.8.1.0** and an appended configuration version **1.0.5**. Its SHA-256 was `a1da9aec1e702e180a563ba95470f20fb78d23dd90909c82d8d7c951987c79e9`.

The embedded configuration explicitly names the public AnthemScore repository. At retrieval, that repository declared package **6.3.100**, released 2026-09-30. The acquired `AnthemScore.exe` identifies file/product version **6.3.0.0**. The version layers describe different things and are not interchangeable.

Metadata, core and resource archives were downloaded from the declared repository and checked against published SHA-1 metadata/sidecars; SHA-256 identities were retained. Archive paths and link/traversal entries were checked before extraction. Framework dependency packages were not downloaded, so the extracted files were not a verified runnable installation.

### Components and pipeline

The actual application is native x64 C++/Qt 6, with Qt Multimedia, packaged FFmpeg libraries, ONNX Runtime, FluidLite and a General MIDI soundfont. A Qt WebEngine viewer contains OpenSheetMusicDisplay assets. Native MusicXML templates and viewer configuration support this static pipeline:

`audio decoding → spectral features → specialized predictions → rhythm/part corrections → MusicXML → embedded notation viewer → PDF/MIDI/MusicXML export paths`

The browser viewer's MusicXML loading/rendering and native `printToPdf` reference corroborate the viewing/PDF architecture. No score was actually generated, rendered or exported. The full native orchestration was not decompiled.

### Embedded models

Six distinct length-prefixed ONNX ModelProto graphs were decoded from the executable without running them or exporting standalone weight files. Their exact byte locations, lengths, hashes, graph inputs/outputs, node/operator counts and initializer types are in [the model metadata](evidence/anthemscore-models.json) and [the appendix](RESEARCH_APPENDICES.md#anthemscore-embedded-models).

All report ONNX IR version 8, opset 17 and PyTorch producer version 2.10.0. The observed contracts support the following interpretations:

- A chord/bass graph emits `chord_logp` and `bass_logp`.
- An onset graph emits `onsets`.
- A beat graph consumes `logmel` and emits beat/downbeat predictions.
- Two distinct graphs share instrument/percussion/volume output interfaces; their different selection purposes remain unknown.
- A small note-feature graph emits per-note logits and is a candidate hand tagger, supported by nearby native labels/UI. The binding to that precise graph was not decompiled.

Graph interfaces are facts; role labels are interpretations to the stated degree. Tensor dimensions are **not verified user-facing limits** on instrument counts, range or simultaneous notes. Spectral/MultiQ/FFT references and rhythm-quantization diagnostics suggest preprocessing, beat repair, swing/triplets and rolled-note handling. Exact parameters, thresholds, training data and model-selection rules remain unknown.

### Editing, constraints and reuse

Packaged UI/help describes automatic instrument detection and percussion detection, including drum/cymbal events. It says that with instrument detection disabled notes initially go to piano, with later assignment possible. Automatic hand assignment is also exposed. One specific English trial resource describes a 30-second limit; actual default checkbox state and trial/edition enforcement were not tested.

A REA pass over the minified viewer exceeded its bounded 512 MiB heap. Partial evidence and manually inspected source contexts were retained; a complete semantic graph was not established. Static local inference components do not prove absence of all network activity or offline activation requirements.

For SMPL Tones, AnthemScore is an architectural and finished-workflow reference: specialized note/timing/instrument models, explicit correction tools, percussion handling and a portable symbolic result. Its proprietary code and embedded weights are excluded from reuse. Native score rendering inside the proposed editor avoids adding a browser merely for notation display. [Historical evidence](evidence/dossiers/anthemscore.json), [official documentation](https://lunaverus.com/documentation).

## 4. Klangio Transcription Studio

### Observed interface and declared capabilities

**Observed UI.** The existing browser tab at `https://studio.klang.io/en/` showed an empty Songbook and New Transcription. Opening the dialog revealed file drop/selection, MP3/WAV/MP4/MIDI/FLAC and other formats, a YouTube/Instagram/TikTok link field and recording. The dialog was closed and the Songbook restored. No file, microphone recording, account mutation, purchase or transcription job was submitted.

**Inspected source.** Conditional wizard settings include instrument selection, difficulty, piano style/pedal, vocal language/lyrics, tuning/capo for guitar/bass/ukulele, drum-note selection, title/composer and advanced parameters. Mode identifiers include universal, classic, rock, solo, arrangement, multi and chorale. An enum entry is not proof that every mode was visible or available to every user.

### Client/server processing

The observed entry asset was `https://studio.klang.io/assets/index-DIr4Mtaw.js`: 4,450,311 bytes, SHA-256 `7e641e9db38279872fa665dd85c8897fd33f8cec5916b86ad290d2465c5b8142`, with a last-modified date of 2026-11-09. It declares `https://ai2notes.klang.io` as the transcription service base.

The custom upload helper builds multipart data with file, credit/ticket flags, source, type, JSON settings and title, then sends it to `/api/transcription/upload`. A social-link method sends URL and settings to `/api/Transcription/social`. The client expects a job ID. A React provider polls `/api/Transcription/get` about once per second while jobs are queued/processing and stops on terminal states including success, error or refunded.

The score page obtains structured MusicJSON through `/api/Transcription/musj`; the parser expects metadata, music information and parts. Editor stores manage score data, playback, piano roll, selection, settings and rendering. A VexFlow renderer can update affected measures. Saving uploads edited JSON with a transcription ID, while retranscription uses a distinct endpoint. This is useful evidence that editing and new recognition are separate client operations; it does not reveal every server operation triggered by a save.

The generated API-service inventory has **30 method declarations**, including file-list/update/delete/job operations and exports. The separate custom upload helper is described in addition to that inventory. All 30 declarations and their purposes are retained in [the API appendix](RESEARCH_APPENDICES.md#klangio-declared-transcription-api) and [machine-readable inventory](evidence/klangio-client-api.json).

Declared result routes include PDF, MIDI, unquantized MIDI, MusicXML, Guitar Pro, LilyPond, original/synthesized audio and MusicJSON. These are client contracts, not completed exports. They do not establish whether the server renders PDFs with VexFlow, LilyPond or another system.

### Analysis coverage and unknown backend

The public asset was acquired by its exact browser-observed URL without copying cookies or authorization values. It advertised a source map, but the requested map URL returned an HTML application shell rather than a JSON map. No alternate paths were probed.

Babel parsed inert JavaScript to select exact workflow declarations. A 31,649-byte aggregate was analyzed with REA: one parsed file, 7,878 visited AST nodes, 64 findings and no parse failure. Syntax examination of that selected input completed, while application/semantic coverage remained partial/unknown; 1,892 semantic unknowns were reported. Additional renderer context was inspected outside the aggregate. The source acquisition was not independently matched to a browser-cache script hash.

No existing Chrome debugging endpoint was available, so there was no REA live CDP/network capture. Browser UI observation and public static source were separate evidence types. No server code/weights, source-separation method, training data, backend language, storage platform or recognition quality was recovered.

### Relevance to SMPL Tones

Klangio supplies a useful product-flow reference: explicit settings, job progress, editable structured results, source/score playback and multiple exports. SMPL Tones should implement those capabilities locally, with no server upload or social URL dependency. Proprietary service behavior cannot be recreated merely by copying a frontend. [Historical evidence](evidence/dossiers/klangio-studio.json), [UI observations](evidence/browser-observations.json), [service terms describing uploads](https://klang.io/terms/).

## 5. MuScriptor

**Inspected source**, commit `8a1ef88672cc23c26619adaff37ec48d82c0b906`. MuScriptor is a multi-instrument audio-to-note model with CLI and local web UI. Its integrated workflow was the closest reviewed source implementation to complete audio-to-score output, before the final model-licensing requirement was fixed.

The Python/PyTorch pipeline resamples to 16 kHz mono and processes five-second segments. A conditioner computes 512-bin log-mel features with a 2048-point FFT and 100 frames/second, projects them to the transformer dimension and prepends audio/optional instrument conditioning to the token stream. A decoder-only transformer predicts MT3-style events. Published/configured small/medium/large sizes are approximately 103M/307M/1.4B parameters with 14/24/48 layers; these sizes were not measured from downloaded weights.

Events encode time shifts, pitch, instrument program/group, binary note-on/off, drums and sustained-note ties. Default prelude forcing carries genuinely unfinished notes from one chunk into the next. Optional instrument restrictions mask forbidden token classes. The note representation does not recover expressive velocities or supply the beat/meter analysis itself.

Timing is a separate stage using Beat This audio beat/downbeat predictions. MIDI export can create a tempo map, correct onset delay, select a subdivision, quantize partially or fully, fill short gaps and trim empty leading bars. Rhythm mistakes can therefore be corrected without necessarily rerunning recognition.

The `write_sheets` path invokes a separate MuseScore 4+ executable: write MIDI, import it into MSCX, export MusicXML and a full-score PDF, generate part PDFs, then modify a copy for suitable fretted-part tablature. Those exports depend on the notation application; they are not generated directly by the transformer.

The FastAPI backend streams note/progress events with SSE. Separate export endpoints can rewrite MIDI from existing events and request engraving. In self-hosting, inference runs on the host rather than inside browser JavaScript. Initial model acquisition requires author access/authentication and downloads; cached local operation and truly complete offline packaging are different deployment states.

The README describes CPU/GPU tradeoffs and poorer results with rubato. Recognition, instrument and beat mistakes can propagate into notation. No same-song benchmark established superiority over commercial tools or other models.

**Licensing/decision:** MIT code; official weights CC BY-NC 4.0 with access conditions. The final SMPL Tones policy excludes those weights from its required bundle. Its model/notation separation, caching, timing controls and export orchestration remain useful references. [Code and author documentation](https://github.com/muscriptor/muscriptor/tree/8a1ef88672cc23c26619adaff37ec48d82c0b906), [official weight card](https://huggingface.co/MuScriptor/muscriptor-medium).

## 6. NeuralNote v2 and muscriptor.cpp

**Inspected source**, NeuralNote commit `ae7fd808d2879a5ca32f93bf9666310ceeb6a9ed`; pinned `muscriptor.cpp` submodule `8589219cc3b584bce970f95aec2ec4a04e53b280`.

NeuralNote offers a standalone application and DAW plugin workflow: record or drop audio, choose instruments or automatic detection, transcribe in the background, audition recognized instruments and export/drag MIDI. Its Windows package includes x64 Standalone and VST3. Version 2 replaces Basic Pitch with MuScriptor, making it a second interface/runtime for the same model family rather than an independent recognition alternative.

The C++/JUCE frontend manages source audio, mono resampling, transcription jobs, piano-roll updates, instrument levels and soundfont synthesis. `MuscriptorEngine` calls the native `msl::Transcriber` API with samples, instrument choices, cancellation and resume state. Chunk callbacks stage completed notes for the UI thread. Saved state supports pause/resume across a closed application/DAW session. The model is released after processing rather than indefinitely occupying memory.

The C++ dependency uses ggml and GGUF weights, supporting CPU, Metal on macOS and Vulkan on Windows/Linux without Python at runtime. Its five-second chunking and stateful note assembly follow the model's event representation. The model-download manifest fixes filenames, expected sizes and SHA-256 digests; downloads are checked before acceptance. Published downloads are about 210 MB, 620 MB and 2.7 GB. These are file sizes, not full memory budgets.

An important score-preparation difference is in `MidiFileWriter`: it converts timestamps with one supplied BPM, writes one conductor tempo and explicitly inserts placeholder 4/4 because this model interface does not provide meter. It then writes per-instrument tracks and drum-channel handling. This export path does not reproduce MuScriptor Python's separate audio beat/tempo-map stage.

The native model documentation excludes expressive dynamics, pitch bends, tempo, meter, key and per-note confidence from recognized output. Readable notation therefore requires additional processing. Performance claims in author documentation are machine-specific; this investigation did not measure Windows parity or speed.

**Licensing/decision:** NeuralNote code is Apache-2.0; the model remains subject to MuScriptor weight terms. SMPL Tones should learn from its native runtime boundary, integrity verification, progress, model lifecycle and recoverable jobs. It should not assume this runtime makes the weights unrestricted. [Application source](https://github.com/DamRsn/NeuralNote/tree/ae7fd808d2879a5ca32f93bf9666310ceeb6a9ed), [native dependency](https://github.com/DamRsn/muscriptor.cpp/tree/8589219cc3b584bce970f95aec2ec4a04e53b280).

## 7. Basic Pitch

**Inspected source**, commit `fa5997af0a8210982619003269994a1be25eddf3`. Basic Pitch is a lightweight instrument-agnostic polyphonic pitch/note recognizer with Python/CLI use and model serializations for multiple inference runtimes. It accepts compatible audio through local decoding and produces MIDI, note-event CSV, model activations and optional synthesized preview audio.

Audio becomes 22.05 kHz mono and is processed in overlapping roughly two-second windows. The TensorFlow/Keras model computes a constant-Q representation, aligns harmonic information and applies small convolutional heads for note activity, onsets and fine pitch contours. Inference trims overlap margins and concatenates activations. Note decoding finds onset peaks, tracks frame energy, rejects short events and can recover remaining note energy; pitch bends are obtained from nearby contour bins.

TensorFlow, CoreML, TensorFlow Lite and ONNX serializations are described. Runtime selection depends on installed packages; the README describes Windows ONNX support. Native deployment can use the graph and reproduce the decoding rules without shipping the training framework, but that C++ implementation/parity work has not been performed here.

The model does not classify each source instrument. Its MIDI writer assigns Electric Piano 1. In multiple-pitch-bend mode, tracks are separated by pitch to work around MIDI bend behavior, not because it identified different instruments. MIDI tempo is supplied/default rather than estimated from an audio beat map. It includes no complete score-engraving stage.

The README says it works best on one instrument at a time. A guitar chord or piano passage is polyphonic while still being a single source; a full band presents a different assignment problem. Separation can simplify the input, but artifacts can hurt pitch and timing.

**Licensing/decision:** Apache-2.0 code, with exact model/runtime distribution notices to be verified in the asset gate. Use it as a lightweight isolated-instrument engine and bend-capable alternative, not as evidence that full-mix part identification is solved. [Pinned project](https://github.com/spotify/basic-pitch/tree/fa5997af0a8210982619003269994a1be25eddf3).

## 8. Original MT3

**Inspected source**, commit `7ecf19d75f5d5863ef46c5b47aceba0ab3bcbff9`. Magenta MT3 is a research implementation of multitrack music transcription using T5X/JAX/Flax, with TensorFlow/SeqIO data preprocessing. The documented user route is a Colab notebook, not a ready-made Windows score editor.

Its continuous-input encoder reads 512-bin log-mel features at 16 kHz, using a 2048-point FFT and hop 128. The reviewed gin preset supplies 256 input frames and 1024 target tokens. The checked network preset uses eight encoder layers, eight decoder layers, 512-dimensional embeddings and six heads; these are the selected configuration's values, not a universal description of derivatives.

The autoregressive decoder predicts time shifts, pitches, instrument programs, drums and ties. Stateful event conversion merges segments and active sustained notes into NoteSequences. The multitrack preset has one nonzero velocity bin, so it does not recover detailed dynamics. The notebook restores a checkpoint, performs prediction and exports MIDI. Other tooling writes per-note JSON. Dataset configurations reference MAESTRO, GuitarSet, URMP, MusicNet, Cerberus and Slakh.

The supplied flow processes a mixture directly rather than requiring stem separation. It still does not provide the entire beat/meter interpretation, notation editing and page-engraving pipeline. The README says training is not easily supported out of the box.

**Licensing/decision:** repository code Apache-2.0. Separately hosted checkpoint rights were not established as identical to the code license. Preserve this distinction from the later YourMT3+ author repository, which has its own observed license metadata. MT3 is a useful architecture/tokenization reference, but the original research stack is not the chosen end-user Windows deployment. [Pinned project](https://github.com/magenta/mt3/tree/7ecf19d75f5d5863ef46c5b47aceba0ab3bcbff9).

## 9. Omnizart

**Inspected source**, commit `bcd8cb44d4da66ce87df10b6abee5c35a8cc2886`. Omnizart is a Python collection of specialized transcription/analysis tasks. It should not be described as a completed single pipeline that automatically combines everything into a full score.

The pitched-music path extracts CFP-family features: spectrum, cepstrum and generalized-cepstrum information, with optional harmonic variants. TensorFlow/Keras U-Net-style segmentation models, including an attention variant in the checked Pop configuration, predict activity channels. Postprocessing normalizes onset/duration channels, applies note thresholds and a statistical instrument-presence filter, then maps channels into MIDI programs.

Other tasks have different representations and semantics. The inspected vocal path separates vocals using a two-stem Spleeter ONNX model through sherpa-onnx, estimates note intervals and combines them with a vocal-contour pitch result. The outputs are MIDI/F0/contour-related results, not recognized lyrics. The drum task uses CQT patches and a dedicated spectral-normalized model; its docstring describes 13 predicted classes with three written to MIDI. The chord task consumes chroma features and writes chord timing/names to CSV plus a MIDI rendering of default chord voicings.

The beat module takes **MIDI input** and extracts symbolic features; it is not equivalent to the audio beat tracker selected for SMPL Tones. Instrument sets and thresholds depend on checkpoints rather than an unrestricted vocabulary.

The combined CLI is explicitly marked preparing, and `omnizart.transcribe_all.process` consists of `pass`. Separate modules contain implementations, but automatic orchestration, alignment and unified score export need development. Python, TensorFlow, audio/plugin and model dependencies also make full Windows packaging more involved than a small native executable.

**Licensing/decision:** repository code/metadata MIT; checkpoint and third-party terms were not all audited. Use specific task implementations as references, preserve the integration gap and avoid shipping the whole toolkit simply to claim feature coverage. [Pinned project](https://github.com/Music-and-Culture-Technology-Lab/omnizart/tree/bcd8cb44d4da66ce87df10b6abee5c35a8cc2886).

## 10. Sheet Sage

**Inspected source**, commit `bbdd7b7b6a5fb845828f82790acdceb03a197779`. Sheet Sage turns a pop recording into a lead sheet with a monophonic melody and chord symbols. It outputs LilyPond source, PDF and audio-aligned melody/harmony MIDI. It is not intended to reconstruct every instrument's complete part.

Beat/downbeat tracking with madmom precedes transcription. Features are resampled onto a sixteenth-note grid. The default representation is a 229-bin log-mel spectrogram at 16 kHz; an optional much larger Jukebox representation uses intermediate learned activations rather than generated audio.

Separate PyTorch encoder-only transducers predict melody and harmony. The loader supports probe or transformer configurations, with transformer settings of 512 dimensions, eight heads and four or six layers depending on the checkpoint. Melody has 89 states including null. Harmony has 97 states: null plus 12 roots across eight chord-quality families. Argmax or threshold-controlled selection yields note/chord changes.

The `LeadSheet` structure combines meter, tempo, key, melody and harmony. Key estimation calls Melisma and falls back to C major on failure. The inspected path assumes a constant three- or four-beat meter and four subdivisions per beat, limiting complex meter/rhythm coverage. The documented quickstart is Linux/Docker; the optional Jukebox path is substantially heavier and requires a suitable CUDA GPU. Windows/WSL operation was not tested.

**Licensing/decision:** MIT code, CC BY-NC-SA 3.0 transcription models, plus other component terms. SMPL Tones should implement lead-sheet output and editable harmonic analysis with its selected components, rather than package those restricted models or the heavy Jukebox stack. [Pinned project](https://github.com/chrisdonahue/sheetsage/tree/bbdd7b7b6a5fb845828f82790acdceb03a197779).

## 11. Ultimate Vocal Remover

**Inspected source**, commit `a5f88453bfb2b38b05a965bcf67727243e0cbf19`. UVR is a Windows-downloadable source-separation interface spanning several model families and ensemble options. Its input and output are audio. A separated vocal/bass/other stem remains a waveform that requires another recognition stage to become notes.

`separate.py` dispatches VR, MDX, MDX-C and Demucs paths. MDX computes an STFT, predicts source spectra through ONNX Runtime or a PyTorch implementation depending on model/settings, and reconstructs audio with inverse STFT. The VR family cascades low-band, high-band and full-band convolutional encoder/decoder networks with ASPP/LSTM components and spectral masks. MDX-C uses TFC/TDF-style spectral networks. Hybrid Transformer Demucs joins waveform and spectrogram branches with a cross-transformer.

Processing includes segment handling, overlap, optional shifts, source caching, secondary models/ensembles and final waveform reconstruction. Results are written through audio libraries and optional format conversion. Stem vocabulary and quality depend on the selected checkpoint: a broad other stem can still contain several sources.

Separation can reduce note overlap but also remove harmonics, smear transients and introduce leakage. Running it by default on every song is not automatically more accurate or faster. A direct full-mix engine and a separated alternative should be compared rather than blindly concatenated.

**Licensing/decision:** the GUI README describes MIT code; every selected model/dependency needs its own ledger. SMPL Tones should offer separation when useful, share media caches and job controls, and retain alternative takes. It need not package every UVR network and Python dependency to reproduce the capability. [Pinned project](https://github.com/Anjok07/ultimatevocalremovergui/tree/a5f88453bfb2b38b05a965bcf67727243e0cbf19).

## 12. Supplementary planning components

These entries are based on targeted primary-source inspection or discovery, not the same 84-file depth as the main review. Their sources and retrieval digests are recorded in [planning provenance](evidence/planning-sources.json).

### YourMT3+

The author's `mimbres/YourMT3` checkpoint repository is labeled Apache-2.0 and says it hosts YourMT3+ checkpoints. The author's inference Space also publishes Apache-2.0 metadata. This is separate evidence from the GPL-labeled landing repository and from an independently encountered `amt-os/YourMT3` fork without a root license established in this investigation. Prefer the author-published inference source rather than silently incorporating that fork.

The selected **YPTF+Multi (PS)** configuration uses a Perceiver-TF encoder, multi-T5 decoder, `mc13_full_plus_256` task, 26 latents, spectrogram frontend, hop 300 and attention-to-channel. Author configuration uses 16 kHz audio and 32,767-sample input windows. Source inference batches segments, predicts token channels, decodes events and merges ties/notes into MIDI. It is a multitrack recognition component, not a finished Windows notation application.

The checkpoint is pinned to model repository revision `e45ebd70398682d54b7bb1901a5216e18f3b1824`, path `logs/2024/mc13_256_all_cross_v6_xk5_amp0811_edr005_attend_c_full_plus_2psn_nl26_sb_b26r_800k/checkpoints/model.ckpt`, 541,553,263 bytes, LFS SHA-256 `f7ed46a7c61244bd35485143a791b3cf46515ef96239793845ae8e4084865130`. The author inference Space is pinned to `5e66c1ea173a8186e0d20432b841d3180cc015b5`.

Native export, CPU/DirectML operator support, feature parity, event decoding, memory use and speed are unvalidated. The author license labels are evidence, not a completed integrated asset/distribution audit. These are explicit first-phase gates before relying on the model in a public app. [Author checkpoint repository](https://huggingface.co/mimbres/YourMT3), [author inference source](https://huggingface.co/spaces/mimbres/YourMT3/tree/5e66c1ea173a8186e0d20432b841d3180cc015b5).

### Beat This

The author project provides audio beat/downbeat tracking with a neural model over log-mel features. Its README explicitly describes code and published weights as MIT, with a training-material caveat. Main `final0` variants are around 78 MB; smaller variants around 8.1 MB. MuScriptor's inspected path uses `final0`, because smaller tracking errors can worsen notation. The intended SMPL Tones default is final0, with a smaller draft path.

An ONNX conversion must preserve the exact frontend, padding, normalization, windows and postprocessing. Third-party conversions encountered in search are not automatically trusted originals. Beats and downbeats do not eliminate ambiguity between all compound/odd meters; expose manual correction. Source pin: `b95c8ab0c58c2d9fcfd40508ae8dffbc05ac4f5c`. [Author source](https://github.com/CPJKU/beat_this/tree/b95c8ab0c58c2d9fcfd40508ae8dffbc05ac4f5c).

### Whisper and whisper.cpp

Whisper supplies local language-to-text recognition, while whisper.cpp supplies a C/C++ runtime supporting Windows and CPU/GPU paths. The original Whisper README explicitly licenses code and weights under MIT. Published unquantized whisper.cpp examples put base around 142 MiB and small around 466 MiB; these are model file sizes and version-dependent memory illustrations, not the final app footprint.

The chosen direction is a bundled multilingual small model, with quantization subject to a quality gate. Run it on a vocal source where possible and label its output a **lyric draft**. Singing, layered voices, accompaniment and repeated phrases can cause missing or invented text. Word timestamps are not correct musical syllable placement. Users need text correction and manual syllable alignment. No singing benchmark or forced-alignment pipeline was validated. [Original model documentation](https://github.com/openai/whisper), [native runtime release](https://github.com/ggml-org/whisper.cpp/tree/v1.9.5).

### Demucs and demucs.cpp

Demucs supplies waveform/spectral source separation rather than note recognition. Its repository states MIT licensing; exact shipped weight identities and notices still require a release ledger. The C++17 `demucs.cpp` project supports hybrid/transformer variants using Eigen and a ggml-format serialization. Its author explicitly describes a memory-versus-speed tradeoff, so native alone must not be equated with faster.

The intended production direction is a bounded local separation worker with native ONNX processing where validated. The C++ port is a technical reference, not proof that the desired Windows GPU path already works. No stems or parity/speed measurements were produced. Native reference pin: `4edae497a114de1ccb17ac9b4a2b8fc0144714d7`. [Demucs](https://github.com/facebookresearch/demucs), [C++ reference](https://github.com/sevagh/demucs.cpp/tree/4edae497a114de1ccb17ac9b4a2b8fc0144714d7).

### ONNX Runtime and DirectML

App-local ONNX Runtime CPU and DirectML providers can provide Windows inference without a Python environment. DirectML uses DirectX 12 and broad GPU support. Its documentation says it remains supported in sustained engineering, with new Windows development moving toward WinML. The planned fixed app-local provider avoids an execution-provider catalog that might need dynamic downloads.

Operator/opset support, shapes and session settings need validation. The inspected documentation requires sequential execution and disabled memory-pattern optimization for DirectML and notes that laptop adapter zero may be the integrated GPU. The implementation must select the intended adapter and provide CPU fallback. No runtime package or model graph was tested here. [Provider documentation](https://onnxruntime.ai/docs/execution-providers/DirectML-ExecutionProvider.html).

### Tsumugi

Discovery/README inspection found instrument-agnostic recognition based on Neural Semi-CRF ideas, plus supplementary velocity/instrument/beat/chord facilities. The author describes instrument classification as experimental. It is not established as a reliable part-identification replacement, was not included in the main source review and has not been selected for the required bundle. Optional SheetSage2-associated weights described there have separate non-commercial conditions; a repository MIT label must not flatten those differences. [Author repository](https://github.com/anime-song/tsumugi).

### TuxGuitar and export references

TuxGuitar documentation lists GP3/GP4/GP5 writing and LilyPond export. It is a useful interoperability reference because the inspected MuseScore module only imports Guitar Pro formats. SMPL Tones should implement and test its own integrated GP5/LilyPond writers against compatible readers, with explicit limitations for unsupported score constructs. No TuxGuitar application, Java runtime or source implementation is included. [Official format documentation](https://www.tuxguitar.app/files/1.6.0/desktop/help/file_formats.html).

### Discovery-only or rejected paths

The `amt-os/YourMT3` fork had source inspected during planning, but no root license was established; it is not the chosen authority for reusable inference source. The author landing page originally offered little implementation code, which is why YourMT3+ was not among the original eight recommendations; the later author checkpoint/Space inspection changed that availability picture.

The earlier `piano2sheet` candidate concerned visual/Synthesia-style piano-video conversion rather than general mixed-song recognition and was not recommended for the requested task. Sibling TypeScript Basic Pitch tools and third-party ONNX mirrors were discovered but not fully audited. Jukebox, madmom and Melisma were examined only as dependencies/context, not independently selected app engines. Search-result appearance alone does not constitute review or redistribution approval.

## Comparative conclusions and final selection

The investigations did not establish a universal accuracy winner. MuScriptor initially led on **workflow completeness**: direct multitrack recognition, separate beats, MIDI cleanup and a ready engraving bridge. NeuralNote makes that model family convenient on desktop. AnthemScore is a relevant complete-product benchmark/reference, while AudioScore emphasizes guided correction and has documented full-mix limitations. Klangio demonstrates a useful hosted interaction model but exposes no reusable offline recognition backend in the inspected frontend.

The final product constraints changed the component decision: public source, one self-contained offline installer, a full integrated editor and required model terms permitting commercial use. Under those constraints, the required direction is stable MuseScore-derived editing plus the author-published YourMT3+ candidate, Basic Pitch, Beat This, Demucs-based separation and whisper.cpp, each behind explicit feasibility/provenance gates. Code openness, model access and complete offline installation are distinct questions.

SMPL Tones should preserve three data layers: immutable input/performance, raw versioned recognition results, and the human-edited score. Automatic note recognition, notation interpretation and layout must remain separate. Changing barlines or score layout should not force expensive recognition; trying another engine should not erase corrections.

The planned application should reproduce relevant capabilities rather than distribute all upstream applications. It will not require separately installed MuseScore, MuScriptor, UVR, Python or an online account. It will not incorporate extracted proprietary engines or secretly use a hosted service when a local path fails.

## Remaining unknowns and preservation boundary

The original static investigations did not validate model quality, deployment speed, editing latency, network behavior of unopened proprietary apps, all edition entitlements or full code/binary equivalence. The native YourMT3+/separation/beat conversions are proposed work. Hardware and package-size estimates are targets, not measurements. Exact model/dependency distribution terms need the first milestone's ledger.

The [evidence packet](evidence/README.md) retains the conclusions, identities, graph contracts, API declarations and original coverage boundaries needed to understand this research without local REA files. The [source index](SOURCES.md) retains pinned code references. Neither is a byte-for-byte backup of every original extraction or a guarantee that changing vendor download servers will continue serving historical binaries.

Before deleting a local working archive, verify a clean clone of this repository and its evidence packet. No automated deletion is part of this project publication. The application remains **planned** until its roadmap gates are implemented and measured.
