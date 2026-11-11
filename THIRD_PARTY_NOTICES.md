# Third-party references and licensing boundaries

This is an original research dossier and development specification. It contains no working application, vendor binaries, extracted model weights, complete vendor manuals, production JavaScript bundles or copies of the 84 inspected source files. Factual manifests and source links identify the material inspected.

## Project material

Original SMPL Tones documents, authored metadata and validation tooling are GPL-3.0-only. A standard GPL version 3 text is in [LICENSE](LICENSE). The proposed MuseScore-derived application must preserve applicable upstream notices and fulfill its distribution obligations when source is integrated. The presence of a license document here does not imply that upstream implementation is already included.

## Referenced code and weights

| Reference | Published code terms observed | Weight/asset distinction |
|---|---|---|
| MuseScore Studio | GPL-3.0-only in inspected source headers | Fonts, sounds and other dependencies require their own notices; retain original attribution when integrated. |
| MuScriptor | MIT | Official model weights CC BY-NC 4.0, with access conditions. Excluded from the required unrestricted bundle. |
| NeuralNote v2 | Apache-2.0 | Uses MuScriptor weights, whose restrictions remain. JUCE, ggml, soundfont and other dependency terms are separate. |
| muscriptor.cpp | Native dependency examined in the NeuralNote context | GGUF conversion does not remove the MuScriptor weight conditions. |
| Basic Pitch | Apache-2.0 | Track the exact bundled model artifact and runtime notices before release; do not infer dataset terms from code headers. |
| Original Magenta MT3 | Apache-2.0 | No blanket conclusion about separately hosted checkpoint licensing was established. Do not substitute the YourMT3+ model-card label for original MT3's terms. |
| Omnizart | MIT repository metadata | Separate checkpoint, Spleeter, runtime and plugin terms were not comprehensively audited. |
| Sheet Sage | MIT code | Transcription models CC BY-NC-SA 3.0; further component terms apply. Restricted weights excluded. |
| UVR GUI | MIT as described in its README | Selected VR/MDX/Demucs checkpoints and dependencies must be assessed individually. |
| YourMT3+ author model repository and inference Space | Apache-2.0 metadata observed for both | Pin exact checkpoint, source revision and author statements. Training-data provenance and integrated distribution review remain release-gate work. |
| Beat This | Author README explicitly describes code and published weights as MIT | Preserve its training-material caveat and exact checkpoint/export provenance. |
| Whisper / whisper.cpp | Original Whisper README explicitly describes code and weights as MIT; whisper.cpp MIT | Converted/quantized files need source identity, conversion description and notices. |
| Demucs / demucs.cpp | MIT repository statements | Confirm the exact separation weight and conversion chain; README code licensing alone is not a complete asset ledger. |
| ONNX Runtime / DirectML | Runtime/provider distribution terms must be retained | Verify the exact app-local native packages before installer publication. |
| Tsumugi and TuxGuitar | Supplementary discovery/format references | No blanket approval of optional models or every dependency was established. |

These entries record the evidence and intended policy, not an exhaustive licensing audit. The first roadmap milestone must complete the component/asset ledger. Required shipped models must permit commercial use; this does not eliminate attribution, notice, copyleft or redistribution conditions.

## Proprietary products

MuseHub, AudioScore Ultimate, AnthemScore and Klangio were investigated as products or artifacts. Their proprietary implementation, trained weights, branding and service internals are not project source dependencies. Static extraction or observation does not establish permission to incorporate their implementation. SMPL Tones should reuse independently licensed components and implement its own workflow where appropriate.

## Citation and quotation policy

The dossier paraphrases functionality and technical conclusions. Small identifiers, hashes, function names and model interfaces serve as factual provenance. Public source and documentation links remain attributed in [the source index](docs/SOURCES.md). Historical machine-readable report text has been sanitized; original evidence filenames are labels, not assertions that excluded raw files are present.
