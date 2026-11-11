"""Focused integrity checks for the self-contained SMPL Tones dossier.

Run with Python 3.10+ from any directory. Uses only the standard library;
does not download anything or test/build the future music application.
SPDX-License-Identifier: GPL-3.0-only
"""
from __future__ import annotations

import json
import re
import sys
import unicodedata
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
EV = ROOT / 'docs' / 'evidence'

def heading_ids(text):
    ids = set()
    counts = {}
    fenced = False
    for line in text.splitlines():
        if line.startswith('```'):
            fenced = not fenced
        if fenced:
            continue
        match = re.match(r'^#{1,6}\s+(.+?)\s*#*$', line)
        if not match:
            continue
        heading = match.group(1).lower().replace('`', '')
        heading = ''.join(c for c in heading if c in ' -_' or unicodedata.category(c)[0] in 'LN')
        slug = heading.replace(' ', '-')
        repeat = counts.get(slug, 0)
        counts[slug] = repeat + 1
        ids.add(slug if not repeat else f'{slug}-{repeat}')
    return ids

def main():
    failures = []
    files = [p for p in ROOT.rglob('*') if p.is_file() and '.git' not in p.relative_to(ROOT).parts]
    excluded = {'.exe', '.dll', '.msi', '.ckpt', '.safetensors', '.gguf', '.onnx', '.7z', '.zip', '.pdf', '.wav', '.mp3'}
    for path in files:
        rel = path.relative_to(ROOT).as_posix()
        if path.suffix.lower() in excluded:
            failures.append(f'Excluded payload in publication: {rel}')
        if path.stat().st_size > 1_000_000:
            failures.append(f'Unexpectedly large publication file: {rel}')
        if path.suffix.lower() not in {'.md', '.json', '.py', '.yml', '.yaml', '.txt', ''}:
            continue
        content = path.read_text(encoding='utf-8')
        if re.search(r'[A-Za-z]:[\\/]+Users[\\/]+', content, re.I):
            failures.append(f'Personal Windows path in {rel}')
        if re.search(r'\b(?:gh[pousr]_[A-Za-z0-9]{25,}|github_pat_[A-Za-z0-9_]{20,}|hf_[A-Za-z0-9]{20,})\b', content):
            failures.append(f'Credential-like value in {rel}')
        if re.search(r'@(gmail|hotmail|outlook|yahoo)\.', content, re.I):
            failures.append(f'Personal email domain in {rel}')
        if path.suffix == '.json':
            try:
                json.loads(content)
            except json.JSONDecodeError as error:
                failures.append(f'Invalid JSON {rel}: {error}')
        if path.suffix != '.md':
            continue
        for raw_target in re.findall(r'\[[^\]\n]*\]\(([^)\n]+)\)', content):
            target = raw_target.strip().strip('<>')
            split = urlsplit(target)
            if split.scheme or split.netloc:
                if split.scheme not in {'http', 'https', 'mailto'}:
                    failures.append(f'Nonportable link in {rel}: {target}')
                continue
            linked = (path.parent / unquote(split.path)).resolve() if split.path else path
            try:
                linked.relative_to(ROOT)
            except ValueError:
                failures.append(f'Link escapes repository in {rel}: {target}')
                continue
            if not linked.is_file():
                failures.append(f'Missing local link in {rel}: {target}')
            elif split.fragment and linked.suffix == '.md':
                if unquote(split.fragment) not in heading_ids(linked.read_text(encoding='utf-8')):
                    failures.append(f'Missing anchor in {rel}: {target}')

    def load(name):
        return json.loads((EV / name).read_text(encoding='utf-8'))

    sources = load('source-manifest.json')['files']
    refs = load('code-references.json')['references']
    models = load('anthemscore-models.json')['models']
    routes = load('klangio-client-api.json')['routes']
    roadmap = load('roadmap.json')['milestones']
    expected = [('source files', len(sources), 84), ('selected code references', len(refs), 59),
                ('model records', len(models), 6), ('API declarations', len(routes), 30), ('roadmap milestones', len(roadmap), 12)]
    for label, actual, count in expected:
        if actual != count:
            failures.append(f'{label}: expected {count}, got {actual}')
    source_keys = {(s['repository'].lower(), s['path'], s['commit']) for s in sources}
    for ref in refs:
        parts = urlsplit(ref['url']).path.strip('/').split('/')
        if len(parts) < 5 or parts[2] != 'blob':
            failures.append(f'Unpinned code reference: {ref["url"]}')
            continue
        key = ('/'.join(parts[:2]).lower(), '/'.join(parts[4:]), parts[3])
        if key not in source_keys:
            failures.append(f'Code reference absent from source manifest: {ref["url"]}')
    for source in sources:
        if not re.fullmatch(r'[0-9a-f]{40}', source['commit']) or not re.fullmatch(r'[0-9a-f]{40}', source['git_blob_sha1']):
            failures.append(f'Invalid source identity: {source["path"]}')
        if not source['git_blob_normalization_matches']:
            failures.append(f'Unmatched source provenance: {source["path"]}')
    for model in models:
        if not re.fullmatch(r'[0-9a-f]{64}', model['sha256']) or model['bytes'] <= 0:
            failures.append('Invalid embedded model identity')
    if len({m['sha256'] for m in models}) != 6:
        failures.append('Embedded model identities are not distinct')
    if [m['step'] for m in roadmap] != list(range(1, 13)):
        failures.append('Roadmap steps are not ordered 1..12')
    for milestone in roadmap:
        if any(dep >= milestone['step'] or dep < 1 for dep in milestone['depends_on_steps']):
            failures.append(f'Invalid dependency at step {milestone["step"]}')
        if not milestone['deliverables'] or not milestone['tests'] or not milestone['completion_gate']:
            failures.append(f'Incomplete milestone {milestone["step"]}')
    research = (ROOT / 'docs' / 'RESEARCH.md').read_text(encoding='utf-8')
    for subject in ['MuseHub', 'AudioScore', 'AnthemScore', 'Klangio', 'MuScriptor', 'NeuralNote', 'Basic Pitch',
                    'MT3', 'Omnizart', 'Sheet Sage', 'Ultimate Vocal Remover', 'YourMT3+', 'Beat This', 'Whisper',
                    'Demucs', 'DirectML', 'Tsumugi', 'TuxGuitar']:
        if subject not in research:
            failures.append(f'Missing research subject: {subject}')
    if 'No working SMPL Tones application' not in (ROOT / 'README.md').read_text(encoding='utf-8'):
        failures.append('README lacks the planned-only implementation boundary')
    if failures:
        print('\n'.join('FAIL: ' + f for f in failures))
        return 1
    print(json.dumps({'status': 'PASS', 'publication_files': len(files),
                      'evidence_counts': {label: actual for label, actual, _ in expected},
                      'checks': ['local Markdown links/anchors', 'JSON parsing and evidence relationships',
                                 'artifact/source identities', 'milestone dependencies', 'subject coverage',
                                 'private-path/credential scan', 'excluded-payload scan'],
                      'not_tested': ['external URL reachability', 'future app build', 'model inference', 'installer behavior']}, indent=2))
    return 0

if __name__ == '__main__':
    sys.exit(main())
