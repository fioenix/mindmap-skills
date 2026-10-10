#!/usr/bin/env python3
"""Build an allowlisted skills-only OpenAI ZIP; never uploads or publishes."""
import hashlib
from pathlib import Path
import sys
import zipfile

ROOT = Path(__file__).resolve().parent.parent
FILES = (
    '.codex-plugin/plugin.json', 'LICENSE', 'README.md', 'PRIVACY.md', 'TERMS.md',
    'assets/icon.svg', 'assets/icon-dark.svg', 'docs/openai-skills-readiness.md',
    'skills/markmap/SKILL.md', 'skills/markmap/agents/openai.yaml',
    'skills/markmap/assets/template.html', 'skills/markmap/scripts/render.sh',
)

def build(output):
    output = Path(output).resolve()
    sources = [ROOT / name for name in FILES]
    for source in sources:
        if source.is_symlink() or not source.is_file() or source.resolve() != source:
            raise ValueError(f'Expected regular, non-symlink package resource: {source}')
    if output in sources or output.exists():
        raise ValueError('Choose a new output path; existing files are never overwritten')
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED) as archive:
        for name, source in zip(FILES, sources):
            info = zipfile.ZipInfo(name, (2026, 1, 1, 0, 0, 0))
            info.external_attr = (0o100755 if name.endswith('.sh') else 0o100644) << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(info, source.read_bytes())
    print(f'{output}\nSHA256 {hashlib.sha256(output.read_bytes()).hexdigest()}')
    return output

if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit('Usage: python3 scripts/package_plugin.py <new-output.zip>')
    build(sys.argv[1])
