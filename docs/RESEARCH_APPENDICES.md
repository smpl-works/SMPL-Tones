# Research appendices

These are factual metadata and client contracts, not executed workflows, exported models or proof of recognition quality. The readable [dossier](RESEARCH.md) explains their scope.

## Supplied and acquired artifact identities

Full records, including signatures and layer-specific versions, are in [artifact identities](evidence/artifact-identities.json).

| Subject | Bytes | SHA-256 |
|---|---|---|
| musehub-installer input | 36,818,352 | `d9eea2ae7c8c7babc0c98a3d3b3591e2295eec02e362791836e7fe2d911caee2` |
| audioscore-demo input | 16,972,520 | `106dd615004840f3fc1a2e9986a733e32eff4c983b35e15b5af120080e69333e` |
| AnthemScore bootstrapper | 33,189,600 | `a1da9aec1e702e180a563ba95470f20fb78d23dd90909c82d8d7c951987c79e9` |
| Acquired AnthemScore.exe | 37,151,008 | `2ee9695e302dc98ec182f54ef38c38f8c6d1ab84e08856e91050b181ab8e2716` |
| Klangio public JavaScript asset | 4,450,311 | `7e641e9db38279872fa665dd85c8897fd33f8cec5916b86ad290d2465c5b8142` |

The AudioScore editor identity is retained in its [ledger](evidence/dossiers/audioscore-demo.json). Original report hashes are retained in the [archive manifest](evidence/archive-manifest.json).

## AnthemScore embedded models

All six models were decoded as length-prefixed ONNX ModelProto metadata from the acquired application. No inference or standalone weight export was performed. All report IR 8, opset 17 and PyTorch producer 2.10.0. The enclosing executable SHA-256 is `2ee9695e302dc98ec182f54ef38c38f8c6d1ab84e08856e91050b181ab8e2716`.

| Model | File offset | Prefix offset | Bytes | Nodes | Initializers | Inferred role |
|---|---|---|---|---|---|---|
| 0 | 4,604,352 | 4,604,348 | 1,636,717 | 490 | 112 | Chord/bass |
| 1 | 6,241,073 | 6,241,069 | 3,498,166 | 79 | 77 | Onsets |
| 2 | 9,739,243 | 9,739,239 | 10,498,989 | 4740 | 138 | Beat/downbeat |
| 3 | 20,238,236 | 20,238,232 | 4,956,262 | 121 | 89 | Instrument/percussion/volume |
| 4 | 28,225,140 | 28,225,136 | 4,956,262 | 121 | 89 | Second variant; selection unknown |
| 5 | 36,051,019 | 36,051,015 | 369,429 | 475 | 62 | Candidate hand tagger; binding unproved |

### Model 0: Chord/bass

SHA-256: `3c9d6527b5f3fe5ada98777e129b452cbe7332f869282b407740099fdd2986dc`.

| Direction | Tensor | Element type ID | Shape |
|---|---|---|---|
| Input | `x` | 1 | `[1, 4, 400, "L"]` |
| Input | `beat` | 1 | `[1, "L", 2]` |
| Output | `chord_logp` | 1 | `["Transposechord_logp_dim_0", "L", 133]` |
| Output | `bass_logp` | 1 | `["Transposechord_logp_dim_0", "L", 12]` |

Operators: `Cast` × 109, `Conv` × 39, `Constant` × 115, `Div` × 19, `Erf` × 19, `Add` × 53, `Mul` × 55, `MaxPool` × 3, `Shape` × 18, `Slice` × 2, `Concat` × 1, `Reshape` × 35, `Transpose` × 3, `InstanceNormalization` × 17, `LogSoftmax` × 2.

Initializer element-type counts: `{"10": 109, "1": 3}`.

### Model 1: Onsets

SHA-256: `db1bcbce43d54793423330d5fd10b9cb8b9f4fd8a1fabbee6be40eebd0892cff`.

| Direction | Tensor | Element type ID | Shape |
|---|---|---|---|
| Input | `input` | 1 | `["batch_size", 4, 352, 720]` |
| Output | `onsets` | 1 | `["batch_size", 88, "Sigmoidonsets_dim_2"]` |

Operators: `Constant` × 15, `Clip` × 2, `Div` × 2, `Log` × 1, `Mul` × 2, `Add` × 8, `LayerNormalization` × 1, `Conv` × 13, `Relu` × 12, `BatchNormalization` × 12, `MaxPool` × 2, `Split` × 1, `Concat` × 1, `Gather` × 2, `Shape` × 1, `Sub` × 1, `Unsqueeze` × 1, `Slice` × 1, `Sigmoid` × 1.

Initializer element-type counts: `{"1": 77}`.

### Model 2: Beat/downbeat

SHA-256: `cbab8ede9dae5b0aa81d854e1ebe3a3fc9a10bce7d029b170d656075263c0783`.

| Direction | Tensor | Element type ID | Shape |
|---|---|---|---|
| Input | `logmel` | 1 | `[1, "T", 128]` |
| Output | `beat` | 1 | `["Addbeat_dim_0", "T"]` |
| Output | `downbeat` | 1 | `["Addbeat_dim_0", "T"]` |

Operators: `Transpose` × 60, `BatchNormalization` × 1, `Shape` × 467, `Constant` × 1790, `Gather` × 425, `Unsqueeze` × 496, `Concat` × 150, `Reshape` × 102, `Conv` × 4, `Div` × 97, `Erf` × 16, `Add` × 103, `Mul` × 300, `ReduceL2` × 25, `Clip` × 25, `Expand` × 29, `MatMul` × 86, `Cast` × 138, `Split` × 37, `Squeeze` × 86, `Range` × 2, `Einsum` × 2, `ConstantOfShape` × 2, `Equal` × 2, `Where` × 2, `Slice` × 135, `ScatterND` × 2, `Neg` × 48, `Cos` × 24, `Sin` × 24, `Sqrt` × 36, `Softmax` × 12, `Sigmoid` × 12.

Initializer element-type counts: `{"1": 138}`.

### Model 3: Instrument/percussion/volume

SHA-256: `d1cbd214eb539e4a32b5e5bc957625f67a1ed0ef71d87a1b823db7fae2e82887`.

| Direction | Tensor | Element type ID | Shape |
|---|---|---|---|
| Input | `views` | 1 | `["batch", 4, 400, 720]` |
| Output | `inst_logp` | 1 | `["batch", 22, 88, "Sliceinst_logp_dim_3"]` |
| Output | `perc_prob` | 1 | `["batch", 14, "Sliceinst_logp_dim_3"]` |
| Output | `vol_logp` | 1 | `["batch", 16, 102, "Sliceinst_logp_dim_3"]` |

Operators: `Identity` × 2, `Constant` × 33, `Clip` × 2, `Div` × 2, `Log` × 1, `Mul` × 2, `Add` × 8, `LayerNormalization` × 1, `Conv` × 18, `Relu` × 13, `BatchNormalization` × 13, `MaxPool` × 2, `Split` × 1, `Concat` × 3, `Shape` × 3, `Gather` × 4, `Slice` × 4, `Unsqueeze` × 4, `Reshape` × 1, `Sub` × 1, `LogSoftmax` × 2, `Softmax` × 1.

Initializer element-type counts: `{"1": 89}`.

### Model 4: Second variant; selection unknown

SHA-256: `05a8cd747c57e9f37d2bbaf26e9eb5a7fb45cfd0522aace9a42dfed7865f8dd9`.

| Direction | Tensor | Element type ID | Shape |
|---|---|---|---|
| Input | `views` | 1 | `["batch", 4, 400, 720]` |
| Output | `inst_logp` | 1 | `["batch", 22, 88, "Sliceinst_logp_dim_3"]` |
| Output | `perc_prob` | 1 | `["batch", 14, "Sliceinst_logp_dim_3"]` |
| Output | `vol_logp` | 1 | `["batch", 16, 102, "Sliceinst_logp_dim_3"]` |

Operators: `Identity` × 2, `Constant` × 33, `Clip` × 2, `Div` × 2, `Log` × 1, `Mul` × 2, `Add` × 8, `LayerNormalization` × 1, `Conv` × 18, `Relu` × 13, `BatchNormalization` × 13, `MaxPool` × 2, `Split` × 1, `Concat` × 3, `Shape` × 3, `Gather` × 4, `Slice` × 4, `Unsqueeze` × 4, `Reshape` × 1, `Sub` × 1, `LogSoftmax` × 2, `Softmax` × 1.

Initializer element-type counts: `{"1": 89}`.

### Model 5: Candidate hand tagger; binding unproved

SHA-256: `abf004cdb3519ae41397798d4211f9de0c7b3d589f01e67a49a3aabdaafc1118`.

| Direction | Tensor | Element type ID | Shape |
|---|---|---|---|
| Input | `features` | 7 | `[1, 384, 9]` |
| Input | `pad_mask` | 9 | `[1, 384]` |
| Output | `logits` | 1 | `[1, 384]` |

Operators: `Cast` × 43, `Constant` × 136, `Gather` × 30, `Add` × 42, `Where` × 5, `LayerNormalization` × 9, `Transpose` × 32, `MatMul` × 21, `Mod` × 4, `Shape` × 8, `Reshape` × 56, `Slice` × 12, `Concat` × 4, `Unsqueeze` × 4, `Squeeze` × 5, `ConstantOfShape` × 4, `Mul` × 20, `Equal` × 4, `Expand` × 4, `Sqrt` × 12, `Div` × 8, `Softmax` × 4, `Gemm` × 4, `Erf` × 4.

Initializer element-type counts: `{"10": 34, "1": 28}`.

Type IDs use ONNX TensorProto enums (1 float32, 10 float16, 7 int64, 9 bool). Symbolic dimensions and class counts are graph interfaces, **not** verified user-facing limits. Two instrument graphs have different hashes but matching interfaces; their variant selection is unresolved. Hand assignment remains a candidate interpretation.

## Klangio declared transcription API

Base URL declared in the inspected client: `https://ai2notes.klang.io`. These 30 generated-service declarations were inventoried without invoking any endpoint. Authentication, authorization, file contents, response quality and internal server implementation were not tested. The separate custom multipart file uploader uses lowercase `/api/transcription/upload`; its data flow is described in the dossier.

| Client method | HTTP | Declared path | Purpose inferred from declaration |
|---|---|---|---|
| `transcriptionGetMyFilesGet` | GET | `/api/Transcription/my_files` | List/filter saved transcriptions |
| `transcriptionGetMyFilesPost` | POST | `/api/Transcription/my_files` | List/filter saved transcriptions |
| `transcriptionGetGet` | GET | `/api/Transcription/get` | Read transcription state/result metadata |
| `transcriptionGetPost` | POST | `/api/Transcription/get` | Read transcription state/result metadata |
| `transcriptionDelete` | DELETE | `/api/Transcription/delete` | Delete transcription |
| `transcriptionUpdateTranscription` | PUT | `/api/Transcription/update` | Update transcription metadata |
| `transcriptionGetTranscriptionUpdate` | GET | `/api/Transcription/transcriptionProgress` | Read/update progress-related metadata |
| `transcriptionUnlock` | POST | `/api/Transcription/unlock` | Unlock transcription entitlement |
| `transcriptionRetranscribeSheet` | POST | `/api/Transcription/retranscribe` | Request new processing |
| `transcriptionAccept` | POST | `/api/Transcription/accept` | Accept a transcription/result |
| `transcriptionRefund` | POST | `/api/Transcription/refund` | Request refund-related operation |
| `transcriptionYouTube` | POST | `/api/Transcription/youtube` | Submit a YouTube link |
| `transcriptionSocial` | POST | `/api/Transcription/social` | Submit a supported social link |
| `transcriptionUpload` | POST | `/api/Transcription/upload` | Generated service upload declaration |
| `transcriptionMove` | PATCH | `/api/Transcription/{id}` | Move/update transcription location |
| `transcriptionMidi` | GET | `/api/Transcription/midi` | Download MIDI |
| `transcriptionUnquantizedMidi` | GET | `/api/Transcription/midi_unquantized` | Download performance/unquantized MIDI |
| `transcriptionMp3` | GET | `/api/Transcription/mp3` | Download original/result audio |
| `transcriptionSynth` | GET | `/api/Transcription/synth` | Download synthesized audio |
| `transcriptionPdf` | GET | `/api/Transcription/pdf` | Download PDF |
| `transcriptionMusicXml` | GET | `/api/Transcription/xml` | Download MusicXML |
| `transcriptionLilypond` | GET | `/api/Transcription/lilypond` | Download LilyPond |
| `transcriptionMusicJson` | GET | `/api/Transcription/musj` | Read/save structured MusicJSON |
| `transcriptionUpdateMusicJson` | PUT | `/api/Transcription/musj` | Read/save structured MusicJSON |
| `transcriptionMusicJsonPlain` | GET | `/api/Transcription/music_json` | Download plain MusicJSON |
| `transcriptionOmrXml` | GET | `/api/Transcription/omr_xml` | Download OMR-related XML |
| `transcriptionOmr` | GET | `/api/Transcription/omr` | Download OMR-related result |
| `transcriptionGuitarPro` | GET | `/api/Transcription/gp` | Download Guitar Pro result |
| `transcriptionClaimTranscription` | POST | `/api/Transcription/claim` | Claim a transcription |
| `transcriptionGetPopularSongs` | GET | `/api/Transcription/popular` | List popular-song metadata |

Names such as OMR in a generated API do not prove that an image-scanning workflow was visible, available or tested. The selected SMPL Tones scope is audio/MIDI transcription, not inferred functionality from every endpoint name.

## REA coverage and interpretation

- MuseHub, AudioScore and AnthemScore installers/app payloads were not executed. Native DSP algorithms were not recovered through a function decompiler.
- AudioScore CIL call references establish encoded method boundaries, not runtime traces.
- AnthemScore viewer analysis exceeded a bounded 512 MiB heap; complete JavaScript semantics were not obtained.
- Klangio used browser-extension UI observation and static public source. No live CDP capture or server access occurred.
- Klangio REA analyzed a selected 31,649-byte aggregate: 7,878 AST nodes, 64 findings, no parse failure, partial/unknown application semantics and 1,892 semantic unknowns.
- Source parsing, UI observation, package decoding and graph-contract interpretation remain separate evidence types.
- Complete per-case evidence IDs and limitations are in the [five normalized ledgers](evidence/README.md).
