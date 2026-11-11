# Source index

Research date: **11 November 2026**. This index preserves source identity and targeted references; it does not imply a complete repository audit or prebuilt-binary equivalence. Inspected source text is not republished.

## Main repository review

84 source/documentation files were acquired across eight reviewed projects and the pinned muscriptor.cpp dependency. The inspected-text digest describes the retained normalized text; the Git blob SHA identifies the upstream bytes. The recorded normalization match explains line-ending/trailing-newline differences.

| Repository | Commit | Files |
|---|---|---|
| muscriptor/muscriptor | `8a1ef88672cc23c26619adaff37ec48d82c0b906` | 13 |
| DamRsn/NeuralNote | `ae7fd808d2879a5ca32f93bf9666310ceeb6a9ed` | 9 |
| spotify/basic-pitch | `fa5997af0a8210982619003269994a1be25eddf3` | 6 |
| magenta/mt3 | `7ecf19d75f5d5863ef46c5b47aceba0ab3bcbff9` | 11 |
| Music-and-Culture-Technology-Lab/omnizart | `bcd8cb44d4da66ce87df10b6abee5c35a8cc2886` | 15 |
| MuseScore/MuseScore | `82ba7e5736f7e5a3466de77c07cba0950c86606b` | 8 |
| chrisdonahue/sheetsage | `bbdd7b7b6a5fb845828f82790acdceb03a197779` | 10 |
| Anjok07/ultimatevocalremovergui | `a5f88453bfb2b38b05a965bcf67727243e0cbf19` | 7 |
| DamRsn/muscriptor.cpp | `8589219cc3b584bce970f95aec2ec4a04e53b280` | 5 |

## Selected code references

59 selected references underpin the main review. They include the dependency context; muscriptor.cpp is not a ninth independent recognition model.

| Project | Conclusion / context | Pinned source |
|---|---|---|
| MuScriptor | Audio/model entry | [muscriptor/transcription_model.py:93](https://github.com/muscriptor/muscriptor/blob/8a1ef88672cc23c26619adaff37ec48d82c0b906/muscriptor/transcription_model.py#L93) |
| MuScriptor | Decoder-only transformer | [muscriptor/models/lm.py:88](https://github.com/muscriptor/muscriptor/blob/8a1ef88672cc23c26619adaff37ec48d82c0b906/muscriptor/models/lm.py#L88) |
| MuScriptor | Event vocabulary | [muscriptor/tokenizer/notes.py:118](https://github.com/muscriptor/muscriptor/blob/8a1ef88672cc23c26619adaff37ec48d82c0b906/muscriptor/tokenizer/notes.py#L118) |
| MuScriptor | Independent beat detector | [muscriptor/utils/beats.py:367](https://github.com/muscriptor/muscriptor/blob/8a1ef88672cc23c26619adaff37ec48d82c0b906/muscriptor/utils/beats.py#L367) |
| MuScriptor | MIDI cleanup | [muscriptor/utils/midi.py:27](https://github.com/muscriptor/muscriptor/blob/8a1ef88672cc23c26619adaff37ec48d82c0b906/muscriptor/utils/midi.py#L27) |
| MuScriptor | External engraving | [muscriptor/utils/sheets.py:333](https://github.com/muscriptor/muscriptor/blob/8a1ef88672cc23c26619adaff37ec48d82c0b906/muscriptor/utils/sheets.py#L333) |
| MuScriptor | Streaming API | [muscriptor/server.py:284](https://github.com/muscriptor/muscriptor/blob/8a1ef88672cc23c26619adaff37ec48d82c0b906/muscriptor/server.py#L284) |
| MuScriptor | License split | [README.md:203](https://github.com/muscriptor/muscriptor/blob/8a1ef88672cc23c26619adaff37ec48d82c0b906/README.md#L203) |
| NeuralNote v2 | Model migration | [README.md:12](https://github.com/DamRsn/NeuralNote/blob/ae7fd808d2879a5ca32f93bf9666310ceeb6a9ed/README.md#L12) |
| NeuralNote v2 | JUCE | [CMakeLists.txt:64](https://github.com/DamRsn/NeuralNote/blob/ae7fd808d2879a5ca32f93bf9666310ceeb6a9ed/CMakeLists.txt#L64) |
| NeuralNote v2 | Inference dependency | [CMakeLists.txt:96](https://github.com/DamRsn/NeuralNote/blob/ae7fd808d2879a5ca32f93bf9666310ceeb6a9ed/CMakeLists.txt#L96) |
| NeuralNote v2 | Native inference call | [Lib/Model/MuscriptorEngine.cpp:211](https://github.com/DamRsn/NeuralNote/blob/ae7fd808d2879a5ca32f93bf9666310ceeb6a9ed/Lib/Model/MuscriptorEngine.cpp#L211) |
| NeuralNote v2 | Download verification | [Lib/Model/ModelDownloader.cpp:187](https://github.com/DamRsn/NeuralNote/blob/ae7fd808d2879a5ca32f93bf9666310ceeb6a9ed/Lib/Model/ModelDownloader.cpp#L187) |
| NeuralNote v2 | Meter limitation | [NeuralNote/Source/MidiFile/MidiFileWriter.cpp:108](https://github.com/DamRsn/NeuralNote/blob/ae7fd808d2879a5ca32f93bf9666310ceeb6a9ed/NeuralNote/Source/MidiFile/MidiFileWriter.cpp#L108) |
| NeuralNote v2 | Native model/output contract | [docs/MODEL.md:37](https://github.com/DamRsn/muscriptor.cpp/blob/8589219cc3b584bce970f95aec2ec4a04e53b280/docs/MODEL.md#L37) |
| NeuralNote v2 | Pinned native implementation | [cpp/src/transcriber.cpp:505](https://github.com/DamRsn/muscriptor.cpp/blob/8589219cc3b584bce970f95aec2ec4a04e53b280/cpp/src/transcriber.cpp#L505) |
| Basic Pitch | CNN architecture | [basic_pitch/models.py:193](https://github.com/spotify/basic-pitch/blob/fa5997af0a8210982619003269994a1be25eddf3/basic_pitch/models.py#L193) |
| Basic Pitch | Audio constants | [basic_pitch/constants.py:33](https://github.com/spotify/basic-pitch/blob/fa5997af0a8210982619003269994a1be25eddf3/basic_pitch/constants.py#L33) |
| Basic Pitch | Windowed inference | [basic_pitch/inference.py:282](https://github.com/spotify/basic-pitch/blob/fa5997af0a8210982619003269994a1be25eddf3/basic_pitch/inference.py#L282) |
| Basic Pitch | Activation-to-note rules | [basic_pitch/note_creation.py:360](https://github.com/spotify/basic-pitch/blob/fa5997af0a8210982619003269994a1be25eddf3/basic_pitch/note_creation.py#L360) |
| Basic Pitch | No instrument classification | [basic_pitch/note_creation.py:244](https://github.com/spotify/basic-pitch/blob/fa5997af0a8210982619003269994a1be25eddf3/basic_pitch/note_creation.py#L244) |
| Basic Pitch | Intended use | [README.md:14](https://github.com/spotify/basic-pitch/blob/fa5997af0a8210982619003269994a1be25eddf3/README.md#L14) |
| MT3 | Encoder-decoder implementation | [mt3/network.py:265](https://github.com/magenta/mt3/blob/7ecf19d75f5d5863ef46c5b47aceba0ab3bcbff9/mt3/network.py#L265) |
| MT3 | Model preset | [mt3/gin/model.gin:53](https://github.com/magenta/mt3/blob/7ecf19d75f5d5863ef46c5b47aceba0ab3bcbff9/mt3/gin/model.gin#L53) |
| MT3 | Multitrack preset | [mt3/gin/mt3.gin:4](https://github.com/magenta/mt3/blob/7ecf19d75f5d5863ef46c5b47aceba0ab3bcbff9/mt3/gin/mt3.gin#L4) |
| MT3 | Audio features | [mt3/spectrograms.py:23](https://github.com/magenta/mt3/blob/7ecf19d75f5d5863ef46c5b47aceba0ab3bcbff9/mt3/spectrograms.py#L23) |
| MT3 | Instrument-aware note data | [mt3/note_sequences.py:42](https://github.com/magenta/mt3/blob/7ecf19d75f5d5863ef46c5b47aceba0ab3bcbff9/mt3/note_sequences.py#L42) |
| MT3 | Notebook export | [mt3/colab/music_transcription_with_transformers.ipynb:469](https://github.com/magenta/mt3/blob/7ecf19d75f5d5863ef46c5b47aceba0ab3bcbff9/mt3/colab/music_transcription_with_transformers.ipynb#L469) |
| MT3 | Training boundary | [README.md:18](https://github.com/magenta/mt3/blob/7ecf19d75f5d5863ef46c5b47aceba0ab3bcbff9/README.md#L18) |
| Omnizart | Music pipeline | [omnizart/music/app.py:97](https://github.com/Music-and-Culture-Technology-Lab/omnizart/blob/bcd8cb44d4da66ce87df10b6abee5c35a8cc2886/omnizart/music/app.py#L97) |
| Omnizart | Segmentation model | [omnizart/models/u_net.py:65](https://github.com/Music-and-Culture-Technology-Lab/omnizart/blob/bcd8cb44d4da66ce87df10b6abee5c35a8cc2886/omnizart/models/u_net.py#L65) |
| Omnizart | Instrument/note decoding | [omnizart/music/inference.py:372](https://github.com/Music-and-Culture-Technology-Lab/omnizart/blob/bcd8cb44d4da66ce87df10b6abee5c35a8cc2886/omnizart/music/inference.py#L372) |
| Omnizart | Vocal separation | [omnizart/vocal/app.py:62](https://github.com/Music-and-Culture-Technology-Lab/omnizart/blob/bcd8cb44d4da66ce87df10b6abee5c35a8cc2886/omnizart/vocal/app.py#L62) |
| Omnizart | Drum output boundary | [omnizart/drum/app.py:39](https://github.com/Music-and-Culture-Technology-Lab/omnizart/blob/bcd8cb44d4da66ce87df10b6abee5c35a8cc2886/omnizart/drum/app.py#L39) |
| Omnizart | MIDI beat input | [omnizart/beat/app.py:66](https://github.com/Music-and-Culture-Technology-Lab/omnizart/blob/bcd8cb44d4da66ce87df10b6abee5c35a8cc2886/omnizart/beat/app.py#L66) |
| Omnizart | Combined command stub | [omnizart/transcribe_all.py:8](https://github.com/Music-and-Culture-Technology-Lab/omnizart/blob/bcd8cb44d4da66ce87df10b6abee5c35a8cc2886/omnizart/transcribe_all.py#L8) |
| Omnizart | Combined CLI | [omnizart/cli/transcribe.py:15](https://github.com/Music-and-Culture-Technology-Lab/omnizart/blob/bcd8cb44d4da66ce87df10b6abee5c35a8cc2886/omnizart/cli/transcribe.py#L15) |
| MuseScore Studio | MIDI entry | [src/importexport/midi/internal/notationmidireader.cpp:31](https://github.com/MuseScore/MuseScore/blob/82ba7e5736f7e5a3466de77c07cba0950c86606b/src/importexport/midi/internal/notationmidireader.cpp#L31) |
| MuseScore Studio | MIDI-to-score conversion | [src/importexport/midi/internal/midiimport/importmidi.cpp:1133](https://github.com/MuseScore/MuseScore/blob/82ba7e5736f7e5a3466de77c07cba0950c86606b/src/importexport/midi/internal/midiimport/importmidi.cpp#L1133) |
| MuseScore Studio | Rhythm quantization | [src/importexport/midi/internal/midiimport/importmidi_quant.cpp:1487](https://github.com/MuseScore/MuseScore/blob/82ba7e5736f7e5a3466de77c07cba0950c86606b/src/importexport/midi/internal/midiimport/importmidi_quant.cpp#L1487) |
| MuseScore Studio | MusicXML serialization | [src/importexport/musicxml/internal/musicxmlwriter.cpp:59](https://github.com/MuseScore/MuseScore/blob/82ba7e5736f7e5a3466de77c07cba0950c86606b/src/importexport/musicxml/internal/musicxmlwriter.cpp#L59) |
| MuseScore Studio | PDF output | [src/importexport/imagesexport/internal/pdfwriter.cpp:61](https://github.com/MuseScore/MuseScore/blob/82ba7e5736f7e5a3466de77c07cba0950c86606b/src/importexport/imagesexport/internal/pdfwriter.cpp#L61) |
| MuseScore Studio | Audio export | [src/importexport/audioexport/audioexportmodule.cpp:59](https://github.com/MuseScore/MuseScore/blob/82ba7e5736f7e5a3466de77c07cba0950c86606b/src/importexport/audioexport/audioexportmodule.cpp#L59) |
| Sheet Sage | Default features | [sheetsage/representations/handcrafted.py:10](https://github.com/chrisdonahue/sheetsage/blob/bbdd7b7b6a5fb845828f82790acdceb03a197779/sheetsage/representations/handcrafted.py#L10) |
| Sheet Sage | Optional learned features | [sheetsage/representations/jukebox.py:79](https://github.com/chrisdonahue/sheetsage/blob/bbdd7b7b6a5fb845828f82790acdceb03a197779/sheetsage/representations/jukebox.py#L79) |
| Sheet Sage | Beat tracking | [sheetsage/beat_track.py:9](https://github.com/chrisdonahue/sheetsage/blob/bbdd7b7b6a5fb845828f82790acdceb03a197779/sheetsage/beat_track.py#L9) |
| Sheet Sage | Model configurations | [sheetsage/infer.py:94](https://github.com/chrisdonahue/sheetsage/blob/bbdd7b7b6a5fb845828f82790acdceb03a197779/sheetsage/infer.py#L94) |
| Sheet Sage | Output vocabularies | [sheetsage/infer.py:78](https://github.com/chrisdonahue/sheetsage/blob/bbdd7b7b6a5fb845828f82790acdceb03a197779/sheetsage/infer.py#L78) |
| Sheet Sage | Meter assumption | [sheetsage/infer.py:206](https://github.com/chrisdonahue/sheetsage/blob/bbdd7b7b6a5fb845828f82790acdceb03a197779/sheetsage/infer.py#L206) |
| Sheet Sage | Notation output | [sheetsage/infer.py:863](https://github.com/chrisdonahue/sheetsage/blob/bbdd7b7b6a5fb845828f82790acdceb03a197779/sheetsage/infer.py#L863) |
| Sheet Sage | Model terms | [README.md:61](https://github.com/chrisdonahue/sheetsage/blob/bbdd7b7b6a5fb845828f82790acdceb03a197779/README.md#L61) |
| Ultimate Vocal Remover (UVR) | MDX | [separate.py:472](https://github.com/Anjok07/ultimatevocalremovergui/blob/a5f88453bfb2b38b05a965bcf67727243e0cbf19/separate.py#L472) |
| Ultimate Vocal Remover (UVR) | MDX-C | [separate.py:639](https://github.com/Anjok07/ultimatevocalremovergui/blob/a5f88453bfb2b38b05a965bcf67727243e0cbf19/separate.py#L639) |
| Ultimate Vocal Remover (UVR) | Demucs | [separate.py:797](https://github.com/Anjok07/ultimatevocalremovergui/blob/a5f88453bfb2b38b05a965bcf67727243e0cbf19/separate.py#L797) |
| Ultimate Vocal Remover (UVR) | VR | [separate.py:1023](https://github.com/Anjok07/ultimatevocalremovergui/blob/a5f88453bfb2b38b05a965bcf67727243e0cbf19/separate.py#L1023) |
| Ultimate Vocal Remover (UVR) | VR architecture | [lib_v5/vr_network/nets_new.py:41](https://github.com/Anjok07/ultimatevocalremovergui/blob/a5f88453bfb2b38b05a965bcf67727243e0cbf19/lib_v5/vr_network/nets_new.py#L41) |
| Ultimate Vocal Remover (UVR) | Hybrid transformer | [demucs/htdemucs.py:27](https://github.com/Anjok07/ultimatevocalremovergui/blob/a5f88453bfb2b38b05a965bcf67727243e0cbf19/demucs/htdemucs.py#L27) |
| Ultimate Vocal Remover (UVR) | Audio output | [separate.py:386](https://github.com/Anjok07/ultimatevocalremovergui/blob/a5f88453bfb2b38b05a965bcf67727243e0cbf19/separate.py#L386) |
| Ultimate Vocal Remover (UVR) | License statement | [README.md:272](https://github.com/Anjok07/ultimatevocalremovergui/blob/a5f88453bfb2b38b05a965bcf67727243e0cbf19/README.md#L272) |

## Complete 84-file acquisition manifest

Full SHA-256/text sizes and normalization matches are in [the JSON manifest](evidence/source-manifest.json).

| Repository | File | Git blob SHA-1 | Source |
|---|---|---|---|
| muscriptor/muscriptor | `README.md` | `eb6cd7cba6495096ebe71ab7728de38f3357603d` | [Pinned file](https://github.com/muscriptor/muscriptor/blob/8a1ef88672cc23c26619adaff37ec48d82c0b906/README.md) |
| muscriptor/muscriptor | `pyproject.toml` | `e5e144441a2971326ac83601da7ddb15305d858d` | [Pinned file](https://github.com/muscriptor/muscriptor/blob/8a1ef88672cc23c26619adaff37ec48d82c0b906/pyproject.toml) |
| muscriptor/muscriptor | `muscriptor/transcription_model.py` | `1ac031e95a0cefeae9cee750a1920e45c2592035` | [Pinned file](https://github.com/muscriptor/muscriptor/blob/8a1ef88672cc23c26619adaff37ec48d82c0b906/muscriptor/transcription_model.py) |
| muscriptor/muscriptor | `muscriptor/models/lm.py` | `7ece36255786fa087a37f56919f256cbefb38058` | [Pinned file](https://github.com/muscriptor/muscriptor/blob/8a1ef88672cc23c26619adaff37ec48d82c0b906/muscriptor/models/lm.py) |
| muscriptor/muscriptor | `muscriptor/modules/conditioners.py` | `8efb5c3d294a9e418e07ea239bd86bbf6cebc71a` | [Pinned file](https://github.com/muscriptor/muscriptor/blob/8a1ef88672cc23c26619adaff37ec48d82c0b906/muscriptor/modules/conditioners.py) |
| muscriptor/muscriptor | `muscriptor/tokenizer/mt3.py` | `c056a483e652759cefd96d393ebe9171a65d2793` | [Pinned file](https://github.com/muscriptor/muscriptor/blob/8a1ef88672cc23c26619adaff37ec48d82c0b906/muscriptor/tokenizer/mt3.py) |
| muscriptor/muscriptor | `muscriptor/utils/beats.py` | `02359cc8d4dda65e17200cdfda2c612c6f61cb03` | [Pinned file](https://github.com/muscriptor/muscriptor/blob/8a1ef88672cc23c26619adaff37ec48d82c0b906/muscriptor/utils/beats.py) |
| muscriptor/muscriptor | `muscriptor/utils/sheets.py` | `4aa0925677ad3a2507e2dd2e98eb4eb18495fc82` | [Pinned file](https://github.com/muscriptor/muscriptor/blob/8a1ef88672cc23c26619adaff37ec48d82c0b906/muscriptor/utils/sheets.py) |
| muscriptor/muscriptor | `muscriptor/server.py` | `fc7dba612b07f9dfbb8262d1688a581f8093e5fa` | [Pinned file](https://github.com/muscriptor/muscriptor/blob/8a1ef88672cc23c26619adaff37ec48d82c0b906/muscriptor/server.py) |
| muscriptor/muscriptor | `muscriptor/main.py` | `5f3237eca784c052a65ddf4febb024decd990b4e` | [Pinned file](https://github.com/muscriptor/muscriptor/blob/8a1ef88672cc23c26619adaff37ec48d82c0b906/muscriptor/main.py) |
| DamRsn/NeuralNote | `README.md` | `86c28390061c51a196b38b6538293741f1af0095` | [Pinned file](https://github.com/DamRsn/NeuralNote/blob/ae7fd808d2879a5ca32f93bf9666310ceeb6a9ed/README.md) |
| DamRsn/NeuralNote | `CMakeLists.txt` | `3d360690389c5f933be3b73beeff5287075ee64b` | [Pinned file](https://github.com/DamRsn/NeuralNote/blob/ae7fd808d2879a5ca32f93bf9666310ceeb6a9ed/CMakeLists.txt) |
| DamRsn/NeuralNote | `Lib/Model/MuscriptorEngine.cpp` | `bc0bdf29c4cc9ac005cdc34a1f3e670a1abfbb27` | [Pinned file](https://github.com/DamRsn/NeuralNote/blob/ae7fd808d2879a5ca32f93bf9666310ceeb6a9ed/Lib/Model/MuscriptorEngine.cpp) |
| DamRsn/NeuralNote | `Lib/Model/ModelManifest.h` | `b2da2a825f619cdd6a98ae497353ac7fff6e0a62` | [Pinned file](https://github.com/DamRsn/NeuralNote/blob/ae7fd808d2879a5ca32f93bf9666310ceeb6a9ed/Lib/Model/ModelManifest.h) |
| DamRsn/NeuralNote | `NeuralNote/Source/TranscriptionManager.cpp` | `5bb5cd9004d83fccc2526cd735a1211cedb1f05c` | [Pinned file](https://github.com/DamRsn/NeuralNote/blob/ae7fd808d2879a5ca32f93bf9666310ceeb6a9ed/NeuralNote/Source/TranscriptionManager.cpp) |
| DamRsn/NeuralNote | `NeuralNote/Source/MidiFile/MidiFileWriter.cpp` | `ed4e7e66407cb5cecdcc6276d6a02eaddbdc5e19` | [Pinned file](https://github.com/DamRsn/NeuralNote/blob/ae7fd808d2879a5ca32f93bf9666310ceeb6a9ed/NeuralNote/Source/MidiFile/MidiFileWriter.cpp) |
| spotify/basic-pitch | `README.md` | `97f122a9a1d27417553f7c25c6dd4683b0172e30` | [Pinned file](https://github.com/spotify/basic-pitch/blob/fa5997af0a8210982619003269994a1be25eddf3/README.md) |
| spotify/basic-pitch | `basic_pitch/models.py` | `867d9b3ca2cdb52f3fad35d43b87d1fd3bcd583c` | [Pinned file](https://github.com/spotify/basic-pitch/blob/fa5997af0a8210982619003269994a1be25eddf3/basic_pitch/models.py) |
| spotify/basic-pitch | `basic_pitch/inference.py` | `06fa54f0c3e1bdda4fa60bca1374d81c57cd7b84` | [Pinned file](https://github.com/spotify/basic-pitch/blob/fa5997af0a8210982619003269994a1be25eddf3/basic_pitch/inference.py) |
| spotify/basic-pitch | `basic_pitch/note_creation.py` | `753f5a18aa616012372c5e4cc641d47b023c2a9e` | [Pinned file](https://github.com/spotify/basic-pitch/blob/fa5997af0a8210982619003269994a1be25eddf3/basic_pitch/note_creation.py) |
| spotify/basic-pitch | `basic_pitch/constants.py` | `c2b717aa14ffa4e5cfa463dd8879b12e13a6f3e8` | [Pinned file](https://github.com/spotify/basic-pitch/blob/fa5997af0a8210982619003269994a1be25eddf3/basic_pitch/constants.py) |
| spotify/basic-pitch | `setup.py` | `005210bf3e2a888b9e53ec9967525eddc5486b2e` | [Pinned file](https://github.com/spotify/basic-pitch/blob/fa5997af0a8210982619003269994a1be25eddf3/setup.py) |
| magenta/mt3 | `README.md` | `b839ffe1015e025414f0528d640f86cd9f16497e` | [Pinned file](https://github.com/magenta/mt3/blob/7ecf19d75f5d5863ef46c5b47aceba0ab3bcbff9/README.md) |
| magenta/mt3 | `mt3/inference.py` | `0e8bf2c9f8b59adfb0bef858d1cadd8b5ac76139` | [Pinned file](https://github.com/magenta/mt3/blob/7ecf19d75f5d5863ef46c5b47aceba0ab3bcbff9/mt3/inference.py) |
| magenta/mt3 | `mt3/network.py` | `55a6a94a779b8e717f28569b8e610617ff477e2a` | [Pinned file](https://github.com/magenta/mt3/blob/7ecf19d75f5d5863ef46c5b47aceba0ab3bcbff9/mt3/network.py) |
| magenta/mt3 | `mt3/note_sequences.py` | `b5ec8624a224643c30bbd0873bdf36f1ea3e99b6` | [Pinned file](https://github.com/magenta/mt3/blob/7ecf19d75f5d5863ef46c5b47aceba0ab3bcbff9/mt3/note_sequences.py) |
| magenta/mt3 | `mt3/spectrograms.py` | `06e179d1a1ec6d7a8a9cfc7d05b21b5a02ec9bb1` | [Pinned file](https://github.com/magenta/mt3/blob/7ecf19d75f5d5863ef46c5b47aceba0ab3bcbff9/mt3/spectrograms.py) |
| magenta/mt3 | `mt3/vocabularies.py` | `8a787c0a685db30d042099ad28aab19bbaa306a7` | [Pinned file](https://github.com/magenta/mt3/blob/7ecf19d75f5d5863ef46c5b47aceba0ab3bcbff9/mt3/vocabularies.py) |
| magenta/mt3 | `mt3/gin/mt3.gin` | `e7b44f4913a5c4a51310ab2c208e311d8639f1f2` | [Pinned file](https://github.com/magenta/mt3/blob/7ecf19d75f5d5863ef46c5b47aceba0ab3bcbff9/mt3/gin/mt3.gin) |
| magenta/mt3 | `setup.py` | `ac1c17dab0721bc5aaa8c8f10ec4f968e6585148` | [Pinned file](https://github.com/magenta/mt3/blob/7ecf19d75f5d5863ef46c5b47aceba0ab3bcbff9/setup.py) |
| Music-and-Culture-Technology-Lab/omnizart | `README.md` | `4ef28a6d1f900324b917c3e0f473af3d41f7460f` | [Pinned file](https://github.com/Music-and-Culture-Technology-Lab/omnizart/blob/bcd8cb44d4da66ce87df10b6abee5c35a8cc2886/README.md) |
| Music-and-Culture-Technology-Lab/omnizart | `pyproject.toml` | `510c1a679e07611f6c9597080f84ddb1639b002e` | [Pinned file](https://github.com/Music-and-Culture-Technology-Lab/omnizart/blob/bcd8cb44d4da66ce87df10b6abee5c35a8cc2886/pyproject.toml) |
| Music-and-Culture-Technology-Lab/omnizart | `omnizart/music/app.py` | `6e896791388c237be970f1d333811d592e71b838` | [Pinned file](https://github.com/Music-and-Culture-Technology-Lab/omnizart/blob/bcd8cb44d4da66ce87df10b6abee5c35a8cc2886/omnizart/music/app.py) |
| Music-and-Culture-Technology-Lab/omnizart | `omnizart/music/inference.py` | `bfb71869a498b3db4cd43178e0ecdb8c3fdffbf5` | [Pinned file](https://github.com/Music-and-Culture-Technology-Lab/omnizart/blob/bcd8cb44d4da66ce87df10b6abee5c35a8cc2886/omnizart/music/inference.py) |
| Music-and-Culture-Technology-Lab/omnizart | `omnizart/models/u_net.py` | `0b7a1db32d2e876f85a6a339a2a50c33ceb8ada0` | [Pinned file](https://github.com/Music-and-Culture-Technology-Lab/omnizart/blob/bcd8cb44d4da66ce87df10b6abee5c35a8cc2886/omnizart/models/u_net.py) |
| Music-and-Culture-Technology-Lab/omnizart | `omnizart/transcribe_all.py` | `1dc1bc8a26238d0ed03f995b269f6232955a068f` | [Pinned file](https://github.com/Music-and-Culture-Technology-Lab/omnizart/blob/bcd8cb44d4da66ce87df10b6abee5c35a8cc2886/omnizart/transcribe_all.py) |
| Music-and-Culture-Technology-Lab/omnizart | `omnizart/cli/transcribe.py` | `14ea852cbeca36c9fb95f1969352b773d6c97f0a` | [Pinned file](https://github.com/Music-and-Culture-Technology-Lab/omnizart/blob/bcd8cb44d4da66ce87df10b6abee5c35a8cc2886/omnizart/cli/transcribe.py) |
| Music-and-Culture-Technology-Lab/omnizart | `omnizart/feature/hcfp.py` | `cfd5d318799a7c14d55d91a92d2b0b50e2dab8c5` | [Pinned file](https://github.com/Music-and-Culture-Technology-Lab/omnizart/blob/bcd8cb44d4da66ce87df10b6abee5c35a8cc2886/omnizart/feature/hcfp.py) |
| MuseScore/MuseScore | `README.md` | `a6384192b3a8607b423a183b363506265f65a7d7` | [Pinned file](https://github.com/musescore/MuseScore/blob/82ba7e5736f7e5a3466de77c07cba0950c86606b/README.md) |
| MuseScore/MuseScore | `LICENSE.txt` | `6d802f72be583b9df9102f85815f5c1e6cac2222` | [Pinned file](https://github.com/musescore/MuseScore/blob/82ba7e5736f7e5a3466de77c07cba0950c86606b/LICENSE.txt) |
| chrisdonahue/sheetsage | `README.md` | `bffff8ac5fe81bb9e5f029edd62e061325103349` | [Pinned file](https://github.com/chrisdonahue/sheetsage/blob/bbdd7b7b6a5fb845828f82790acdceb03a197779/README.md) |
| chrisdonahue/sheetsage | `LICENSE` | `b5d6b5b79fe1e642bb3cf5e7d4ff45228d3d8e53` | [Pinned file](https://github.com/chrisdonahue/sheetsage/blob/bbdd7b7b6a5fb845828f82790acdceb03a197779/LICENSE) |
| chrisdonahue/sheetsage | `sheetsage/infer.py` | `ef0bb17ac98fdaa5b1f029611f460ebf03078b58` | [Pinned file](https://github.com/chrisdonahue/sheetsage/blob/bbdd7b7b6a5fb845828f82790acdceb03a197779/sheetsage/infer.py) |
| chrisdonahue/sheetsage | `sheetsage/beat_track.py` | `c4ffc4eb40dbde3b940351e0f6d0867fe5581400` | [Pinned file](https://github.com/chrisdonahue/sheetsage/blob/bbdd7b7b6a5fb845828f82790acdceb03a197779/sheetsage/beat_track.py) |
| chrisdonahue/sheetsage | `sheetsage/representations/jukebox.py` | `135ded93ad7ae7a8ceb671a48dbf9c7c1e869e7a` | [Pinned file](https://github.com/chrisdonahue/sheetsage/blob/bbdd7b7b6a5fb845828f82790acdceb03a197779/sheetsage/representations/jukebox.py) |
| chrisdonahue/sheetsage | `sheetsage/theory/lead_sheet.py` | `8a60628ad3448d2e97dae903e1c97144a1e66ea6` | [Pinned file](https://github.com/chrisdonahue/sheetsage/blob/bbdd7b7b6a5fb845828f82790acdceb03a197779/sheetsage/theory/lead_sheet.py) |
| Anjok07/ultimatevocalremovergui | `README.md` | `93746d4b4f06f301257c1ee5045e914fee23c974` | [Pinned file](https://github.com/Anjok07/ultimatevocalremovergui/blob/a5f88453bfb2b38b05a965bcf67727243e0cbf19/README.md) |
| Anjok07/ultimatevocalremovergui | `requirements.txt` | `49c235c12f75d6c5d9c4ac8d3e3c9506e37e9770` | [Pinned file](https://github.com/Anjok07/ultimatevocalremovergui/blob/a5f88453bfb2b38b05a965bcf67727243e0cbf19/requirements.txt) |
| Anjok07/ultimatevocalremovergui | `separate.py` | `864473e638306c83d9e3eafd5b448f477e66f869` | [Pinned file](https://github.com/Anjok07/ultimatevocalremovergui/blob/a5f88453bfb2b38b05a965bcf67727243e0cbf19/separate.py) |
| Anjok07/ultimatevocalremovergui | `demucs/htdemucs.py` | `bad6b113102c959c72d4c47387c2cc2f48a17e85` | [Pinned file](https://github.com/Anjok07/ultimatevocalremovergui/blob/a5f88453bfb2b38b05a965bcf67727243e0cbf19/demucs/htdemucs.py) |
| Anjok07/ultimatevocalremovergui | `lib_v5/tfc_tdf_v3.py` | `eba006c98249c1730c50fae2ac8dcd42a9be3453` | [Pinned file](https://github.com/Anjok07/ultimatevocalremovergui/blob/a5f88453bfb2b38b05a965bcf67727243e0cbf19/lib_v5/tfc_tdf_v3.py) |
| muscriptor/muscriptor | `muscriptor/utils/midi.py` | `3504218fc8ee5d849eb944be7e21967d641ab760` | [Pinned file](https://github.com/muscriptor/muscriptor/blob/8a1ef88672cc23c26619adaff37ec48d82c0b906/muscriptor/utils/midi.py) |
| muscriptor/muscriptor | `muscriptor/tokenizer/notes.py` | `77061b68e6df0d1a8d517616ba5dc40eb3e1313f` | [Pinned file](https://github.com/muscriptor/muscriptor/blob/8a1ef88672cc23c26619adaff37ec48d82c0b906/muscriptor/tokenizer/notes.py) |
| muscriptor/muscriptor | `muscriptor/modules/transformer.py` | `c119422b8a78f64c7e9c087dfc86362e31912a41` | [Pinned file](https://github.com/muscriptor/muscriptor/blob/8a1ef88672cc23c26619adaff37ec48d82c0b906/muscriptor/modules/transformer.py) |
| DamRsn/NeuralNote | `.gitmodules` | `e9ab252a26db80edfd018b28df6c8c55dbedd07c` | [Pinned file](https://github.com/DamRsn/NeuralNote/blob/ae7fd808d2879a5ca32f93bf9666310ceeb6a9ed/.gitmodules) |
| DamRsn/NeuralNote | `NeuralNote/Source/SourceAudioManager.cpp` | `181afe3db7d69963408707f134b4fbb98fb18d39` | [Pinned file](https://github.com/DamRsn/NeuralNote/blob/ae7fd808d2879a5ca32f93bf9666310ceeb6a9ed/NeuralNote/Source/SourceAudioManager.cpp) |
| DamRsn/NeuralNote | `Lib/Model/ModelDownloader.cpp` | `559817a141ec1f08106ad8b9434f73a9b2f1e668` | [Pinned file](https://github.com/DamRsn/NeuralNote/blob/ae7fd808d2879a5ca32f93bf9666310ceeb6a9ed/Lib/Model/ModelDownloader.cpp) |
| DamRsn/muscriptor.cpp | `README.md` | `ce9317d66fa8a1511d422578bc1b8e109bdf4330` | [Pinned file](https://github.com/DamRsn/muscriptor.cpp/blob/8589219cc3b584bce970f95aec2ec4a04e53b280/README.md) |
| DamRsn/muscriptor.cpp | `docs/MODEL.md` | `fd2ab45016c1c42471ceb0746282cd6a66706983` | [Pinned file](https://github.com/DamRsn/muscriptor.cpp/blob/8589219cc3b584bce970f95aec2ec4a04e53b280/docs/MODEL.md) |
| DamRsn/muscriptor.cpp | `docs/TOKENIZER.md` | `049812e7ae309a84ed89151b06e27ab1ebb7fa56` | [Pinned file](https://github.com/DamRsn/muscriptor.cpp/blob/8589219cc3b584bce970f95aec2ec4a04e53b280/docs/TOKENIZER.md) |
| DamRsn/muscriptor.cpp | `cpp/src/transcriber.cpp` | `7aaf2600808207e2472bf27d56eb88adc2bb3251` | [Pinned file](https://github.com/DamRsn/muscriptor.cpp/blob/8589219cc3b584bce970f95aec2ec4a04e53b280/cpp/src/transcriber.cpp) |
| DamRsn/muscriptor.cpp | `cpp/CMakeLists.txt` | `55aaa6ffc045ca2e85e0ddcb459d71e56cdcbe3e` | [Pinned file](https://github.com/DamRsn/muscriptor.cpp/blob/8589219cc3b584bce970f95aec2ec4a04e53b280/cpp/CMakeLists.txt) |
| magenta/mt3 | `mt3/gin/model.gin` | `e5d18efdadb2f4c61a5ae28650eb86eca4d282c2` | [Pinned file](https://github.com/magenta/mt3/blob/7ecf19d75f5d5863ef46c5b47aceba0ab3bcbff9/mt3/gin/model.gin) |
| magenta/mt3 | `mt3/datasets.py` | `039c8fc8f1b3aa34f91e136be6b2871f0d57bb9f` | [Pinned file](https://github.com/magenta/mt3/blob/7ecf19d75f5d5863ef46c5b47aceba0ab3bcbff9/mt3/datasets.py) |
| magenta/mt3 | `mt3/colab/music_transcription_with_transformers.ipynb` | `4e71a7da504d178fc1ca51e3a18705317fc9b3ca` | [Pinned file](https://github.com/magenta/mt3/blob/7ecf19d75f5d5863ef46c5b47aceba0ab3bcbff9/mt3/colab/music_transcription_with_transformers.ipynb) |
| Music-and-Culture-Technology-Lab/omnizart | `omnizart/feature/wrapper_func.py` | `94a97935a62826ef27907918d80d6d812a42531a` | [Pinned file](https://github.com/Music-and-Culture-Technology-Lab/omnizart/blob/bcd8cb44d4da66ce87df10b6abee5c35a8cc2886/omnizart/feature/wrapper_func.py) |
| Music-and-Culture-Technology-Lab/omnizart | `omnizart/drum/app.py` | `aed3da3056256358ea8b3fac4772da6ae8a3bc98` | [Pinned file](https://github.com/Music-and-Culture-Technology-Lab/omnizart/blob/bcd8cb44d4da66ce87df10b6abee5c35a8cc2886/omnizart/drum/app.py) |
| Music-and-Culture-Technology-Lab/omnizart | `omnizart/vocal/app.py` | `99bda3867f0189b1193d16fc42922d6992efbae0` | [Pinned file](https://github.com/Music-and-Culture-Technology-Lab/omnizart/blob/bcd8cb44d4da66ce87df10b6abee5c35a8cc2886/omnizart/vocal/app.py) |
| Music-and-Culture-Technology-Lab/omnizart | `omnizart/chord/app.py` | `0514c1a589d07b2810464bd83a07bc6a61ce6f4d` | [Pinned file](https://github.com/Music-and-Culture-Technology-Lab/omnizart/blob/bcd8cb44d4da66ce87df10b6abee5c35a8cc2886/omnizart/chord/app.py) |
| Music-and-Culture-Technology-Lab/omnizart | `omnizart/beat/app.py` | `8f850b81319d368674f3620d20d35c3a40c12a4b` | [Pinned file](https://github.com/Music-and-Culture-Technology-Lab/omnizart/blob/bcd8cb44d4da66ce87df10b6abee5c35a8cc2886/omnizart/beat/app.py) |
| Music-and-Culture-Technology-Lab/omnizart | `omnizart/defaults/music.yaml` | `572612b301f28cec987fb08aa48c227e89de4c02` | [Pinned file](https://github.com/Music-and-Culture-Technology-Lab/omnizart/blob/bcd8cb44d4da66ce87df10b6abee5c35a8cc2886/omnizart/defaults/music.yaml) |
| Music-and-Culture-Technology-Lab/omnizart | `omnizart/checkpoints/music/music_pop/configurations.yaml` | `7f504c5ca64634c89926d54b1e35ed308f95dbdb` | [Pinned file](https://github.com/Music-and-Culture-Technology-Lab/omnizart/blob/bcd8cb44d4da66ce87df10b6abee5c35a8cc2886/omnizart/checkpoints/music/music_pop/configurations.yaml) |
| MuseScore/MuseScore | `src/importexport/midi/internal/notationmidireader.cpp` | `e5a92013a73831d3920638c5d0aa42a60765aeb5` | [Pinned file](https://github.com/musescore/MuseScore/blob/82ba7e5736f7e5a3466de77c07cba0950c86606b/src/importexport/midi/internal/notationmidireader.cpp) |
| MuseScore/MuseScore | `src/importexport/midi/internal/midiimport/importmidi.cpp` | `ae25793cbf5b5f7ccae7f53267c72e3ed215f1f5` | [Pinned file](https://github.com/musescore/MuseScore/blob/82ba7e5736f7e5a3466de77c07cba0950c86606b/src/importexport/midi/internal/midiimport/importmidi.cpp) |
| MuseScore/MuseScore | `src/importexport/midi/internal/midiimport/importmidi_quant.cpp` | `d7958c1c721e036d3ec7f615f2c87a1027b27d5c` | [Pinned file](https://github.com/musescore/MuseScore/blob/82ba7e5736f7e5a3466de77c07cba0950c86606b/src/importexport/midi/internal/midiimport/importmidi_quant.cpp) |
| MuseScore/MuseScore | `src/importexport/imagesexport/internal/pdfwriter.cpp` | `551333fe0655d4d3ebf9679744721b897ed79952` | [Pinned file](https://github.com/musescore/MuseScore/blob/82ba7e5736f7e5a3466de77c07cba0950c86606b/src/importexport/imagesexport/internal/pdfwriter.cpp) |
| MuseScore/MuseScore | `src/importexport/musicxml/internal/musicxmlwriter.cpp` | `f69d847b078bf0ff5112e128f44169524748539c` | [Pinned file](https://github.com/musescore/MuseScore/blob/82ba7e5736f7e5a3466de77c07cba0950c86606b/src/importexport/musicxml/internal/musicxmlwriter.cpp) |
| MuseScore/MuseScore | `src/importexport/audioexport/audioexportmodule.cpp` | `08bba8e321947e056cb57194a9e11e21d3769f0a` | [Pinned file](https://github.com/musescore/MuseScore/blob/82ba7e5736f7e5a3466de77c07cba0950c86606b/src/importexport/audioexport/audioexportmodule.cpp) |
| chrisdonahue/sheetsage | `sheetsage/modules/modules.py` | `ba35c529191bdf5f8312ddd8ad1e7e2793e907a1` | [Pinned file](https://github.com/chrisdonahue/sheetsage/blob/bbdd7b7b6a5fb845828f82790acdceb03a197779/sheetsage/modules/modules.py) |
| chrisdonahue/sheetsage | `sheetsage/representations/handcrafted.py` | `495272b39b4d08dd9299ff8f99c95e82c83226e9` | [Pinned file](https://github.com/chrisdonahue/sheetsage/blob/bbdd7b7b6a5fb845828f82790acdceb03a197779/sheetsage/representations/handcrafted.py) |
| chrisdonahue/sheetsage | `sheetsage/theory/utils.py` | `0fa654b60a93eb6eb9e817bb94894c0a966fea25` | [Pinned file](https://github.com/chrisdonahue/sheetsage/blob/bbdd7b7b6a5fb845828f82790acdceb03a197779/sheetsage/theory/utils.py) |
| chrisdonahue/sheetsage | `sheetsage/assets/sheetsage.json` | `42f8c2ccb25e1902dee18db3a27f95ac6589c403` | [Pinned file](https://github.com/chrisdonahue/sheetsage/blob/bbdd7b7b6a5fb845828f82790acdceb03a197779/sheetsage/assets/sheetsage.json) |
| Anjok07/ultimatevocalremovergui | `lib_v5/vr_network/nets_new.py` | `67772745126d05ade18fb713282469352c5bdd30` | [Pinned file](https://github.com/Anjok07/ultimatevocalremovergui/blob/a5f88453bfb2b38b05a965bcf67727243e0cbf19/lib_v5/vr_network/nets_new.py) |
| Anjok07/ultimatevocalremovergui | `demucs/apply.py` | `be6d930035a4748192b96d7baee6e80772a02f6e` | [Pinned file](https://github.com/Anjok07/ultimatevocalremovergui/blob/a5f88453bfb2b38b05a965bcf67727243e0cbf19/demucs/apply.py) |

## Earlier MuseScore source trace

These six source files belong to the earlier installer investigation, pinned separately; they were not extracted from MuseHub.

| File | Commit | Blob SHA-1 | Source |
|---|---|---|---|
| `notationmidireader.cpp` | `701d557996fb0da981bc20e567d4c8efbe2433c7` | `e5a92013a73831d3920638c5d0aa42a60765aeb5` | [Source](https://github.com/musescore/MuseScore/blob/701d557996fb0da981bc20e567d4c8efbe2433c7/src/importexport/midi/internal/notationmidireader.cpp) |
| `midimodule.cpp` | `701d557996fb0da981bc20e567d4c8efbe2433c7` | `911ba365120fc162d858d6b52d6eabd1cc6c4dd9` | [Source](https://github.com/musescore/MuseScore/blob/701d557996fb0da981bc20e567d4c8efbe2433c7/src/importexport/midi/midimodule.cpp) |
| `importmidi.cpp` | `701d557996fb0da981bc20e567d4c8efbe2433c7` | `ae25793cbf5b5f7ccae7f53267c72e3ed215f1f5` | [Source](https://github.com/musescore/MuseScore/blob/701d557996fb0da981bc20e567d4c8efbe2433c7/src/importexport/midi/internal/midiimport/importmidi.cpp) |
| `pdfwriter.cpp` | `701d557996fb0da981bc20e567d4c8efbe2433c7` | `551333fe0655d4d3ebf9679744721b897ed79952` | [Source](https://github.com/musescore/MuseScore/blob/701d557996fb0da981bc20e567d4c8efbe2433c7/src/importexport/imagesexport/internal/pdfwriter.cpp) |
| `audioexportmodule.cpp` | `701d557996fb0da981bc20e567d4c8efbe2433c7` | `08bba8e321947e056cb57194a9e11e21d3769f0a` | [Source](https://github.com/musescore/MuseScore/blob/701d557996fb0da981bc20e567d4c8efbe2433c7/src/importexport/audioexport/audioexportmodule.cpp) |
| `musicxmlmodule.cpp` | `701d557996fb0da981bc20e567d4c8efbe2433c7` | `61b9b43d2fb789eede0f3f74479224f79a7f54c5` | [Source](https://github.com/musescore/MuseScore/blob/701d557996fb0da981bc20e567d4c8efbe2433c7/src/importexport/musicxml/musicxmlmodule.cpp) |

## Supplementary primary-source inspection

This later planning inspection has narrower scope than the eight-project review. Immutable Git object URLs identify observed document contents even where an original page used a branch/tag.

| Subject | Observed source | Git blob |
|---|---|---|
| MuseScore/MuseScore / `version.cmake` | [Page](https://github.com/musescore/MuseScore/blob/96480d58445e3b24b230a3fe7d4725d639aa2eb3/version.cmake) | [f8c8e1e5e4e7c5bac3aaf0411fa44475f80bfd9c](https://api.github.com/repos/MuseScore/MuseScore/git/blobs/f8c8e1e5e4e7c5bac3aaf0411fa44475f80bfd9c) |
| CPJKU/beat_this / `README.md` | [Page](https://github.com/CPJKU/beat_this/blob/b95c8ab0c58c2d9fcfd40508ae8dffbc05ac4f5c/README.md) | [955931cf33881364dc0fa27e30825d1c83d25adb](https://api.github.com/repos/CPJKU/beat_this/git/blobs/955931cf33881364dc0fa27e30825d1c83d25adb) |
| ggml-org/whisper.cpp / `README.md` | [Page](https://github.com/ggml-org/whisper.cpp/blob/v1.9.5/README.md) | [e58c4ba1061221bd295e08eea5a021dd7178189f](https://api.github.com/repos/ggml-org/whisper.cpp/git/blobs/e58c4ba1061221bd295e08eea5a021dd7178189f) |
| openai/whisper / `README.md` | [Page](https://github.com/openai/whisper/blob/main/README.md) | [196b48f62d3b6f0b77bac2b7dbc2df5e4cfb070b](https://api.github.com/repos/openai/whisper/git/blobs/196b48f62d3b6f0b77bac2b7dbc2df5e4cfb070b) |
| sevagh/demucs.cpp / `README.md` | [Page](https://github.com/sevagh/demucs.cpp/blob/4edae497a114de1ccb17ac9b4a2b8fc0144714d7/README.md) | [1d8969de9c777319af67b2fb5a79b106f39e4c08](https://api.github.com/repos/sevagh/demucs.cpp/git/blobs/1d8969de9c777319af67b2fb5a79b106f39e4c08) |
| facebookresearch/demucs / `README.md` | [Page](https://github.com/facebookresearch/demucs/blob/main/README.md) | [fe7e77b992b7918eba9491119d313abf5bc3eff1](https://api.github.com/repos/facebookresearch/demucs/git/blobs/fe7e77b992b7918eba9491119d313abf5bc3eff1) |

## Planning-source acquisition identities

The full fetched-byte hashes and sizes are in [planning provenance](evidence/planning-sources.json). These public texts/metadata were read without downloading weights or running models.

| Record | Source | SHA-256 |
|---|---|---|
| yourmt3-model-metadata | [Source](https://huggingface.co/api/models/mimbres/YourMT3/revision/e45ebd70398682d54b7bb1901a5216e18f3b1824) | `787328c55de319b10f6966d2ad61c2053561ccaba3a4825b16d5a6832470fc88` |
| yourmt3-model-card | [Source](https://huggingface.co/mimbres/YourMT3/raw/e45ebd70398682d54b7bb1901a5216e18f3b1824/README.md) | `b66c7743f197a0424b05185b353bfad714a26af90551b8a9306a1a7c4dc3d1bd` |
| yourmt3-author-space-card | [Source](https://huggingface.co/spaces/mimbres/YourMT3/raw/5e66c1ea173a8186e0d20432b841d3180cc015b5/README.md) | `9a8468bd685eb0e9084566c5b6cca230481ea4e1c0a6212b4388c4b4618400b4` |
| yourmt3-author-app | [Source](https://huggingface.co/spaces/mimbres/YourMT3/raw/5e66c1ea173a8186e0d20432b841d3180cc015b5/app.py) | `16d46c61399723079ce9606d28b50720336c51475e6a36cbaca861a41fd274e2` |
| yourmt3-author-config | [Source](https://huggingface.co/spaces/mimbres/YourMT3/raw/5e66c1ea173a8186e0d20432b841d3180cc015b5/amt/src/config/config.py) | `6803e1479c77a9c5f5ddec145291ee9b17cd9a15fbcd5f1bcf7ba39297218838` |
| yourmt3-author-inference | [Source](https://huggingface.co/spaces/mimbres/YourMT3/raw/5e66c1ea173a8186e0d20432b841d3180cc015b5/model_helper.py) | `47706291e10a0d25aef768ef276de3bfcdf98175141d57802b571917c6de4d3a` |
| tsumugi-discovery-readme | [Source](https://raw.githubusercontent.com/anime-song/tsumugi/main/README.md) | `b41f9179da6bb0faa02df35d535dbe742d205e08e52a23525a60abb4676fffdb` |
| tuxguitar-formats | [Source](https://www.tuxguitar.app/files/1.6.0/desktop/help/file_formats.html) | `f8a34ce507d63c1c3a28509fbe461a92784c2273fcaa3ec467a1a416f3b45e3c` |
| directml-runtime | [Source](https://onnxruntime.ai/docs/execution-providers/DirectML-ExecutionProvider.html) | `bcb90fa28ebc2b01ddf0db09c19d2e2499c592fe7a64f646572b06adac96e0c1` |

## Product documentation and contextual references

- [AudioScore official manual](https://www.neuratron.com/downloads/NASHelp.pdf): relevant bundled/manual findings concern recognition limits and corrections; full-edition descriptions do not prove demo entitlements.
- [AnthemScore documentation](https://lunaverus.com/documentation): product workflow/context. Historical supplied-artifact evidence remains separately versioned.
- [AnthemScore desktop/web distinction](https://lunaverus.com/transcribe/pricing): vendor describes the desktop offline product separately from its web service.
- [Klangio file inputs](https://klang.io/help/file-limitations/) and [service terms](https://klang.io/terms/): context for hosted processing; API behavior was not exercised.
- [MuseScore stable v4.7.6](https://github.com/musescore/MuseScore/releases/tag/v4.7.6): proposed editor base, distinct from the reviewed unstable main source.
- [MuScriptor official medium model card](https://huggingface.co/MuScriptor/muscriptor-medium): access terms and CC BY-NC weight label.
- [YourMT3+ author checkpoint repository](https://huggingface.co/mimbres/YourMT3): separate Apache-2.0 metadata; do not generalize to original Magenta MT3.
- [Tsumugi author repository](https://github.com/anime-song/tsumugi): supplementary discovery only.
- [TuxGuitar format documentation](https://www.tuxguitar.app/files/1.6.0/desktop/help/file_formats.html): GP5/LilyPond interoperability reference.

Vendor pages can change. Pinned source commits and recorded artifact/report identities preserve what this dossier actually concluded.
