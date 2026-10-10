#!/usr/bin/env python3
"""Offline regression checks for submission packaging and isolated skill resources."""
import html.parser
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import zipfile
import sys
sys.dont_write_bytecode = True

ROOT = Path(__file__).resolve().parent.parent
manifest = json.loads((ROOT / '.codex-plugin/plugin.json').read_text())
assert manifest['skills'] == './skills/', 'Submission expects the root skills directory'
interface = manifest['interface']
for field, limit in [('displayName', 30), ('shortDescription', 30), ('developerName', 80), ('longDescription', 4000)]:
    assert isinstance(interface[field], str) and 0 < len(interface[field]) <= limit
for field in ['composerIcon', 'composerIconDark', 'logo', 'logoDark']:
    assert interface[field].startswith('./assets/')
    assert (ROOT / interface[field]).is_file()

# Installers (Claude Code included) install package.json dependencies; the plugin must stay dependency-free.
DEPENDENCY_KEYS = ('dependencies', 'devDependencies', 'optionalDependencies', 'peerDependencies', 'bundleDependencies')
root_package = json.loads((ROOT / 'package.json').read_text())
assert not any(key in root_package for key in DEPENDENCY_KEYS), 'Root package.json must declare no dependencies'
root_lock = json.loads((ROOT / 'package-lock.json').read_text())
assert list(root_lock['packages']) == [''], 'Root lockfile must not resolve any packages'
assert not any(key in root_lock['packages'][''] for key in DEPENDENCY_KEYS)
assert not any(entry.startswith('.github') for entry in root_package['files'])
ci_package = json.loads((ROOT / '.github/ci/package.json').read_text())
ci_lock = json.loads((ROOT / '.github/ci/package-lock.json').read_text())
assert ci_package.get('private') is True, 'CI tooling package must never be publishable'
ci_pin = ci_package['devDependencies']['@anthropic-ai/claude-code']
assert ci_lock['packages']['']['devDependencies'] == ci_package['devDependencies']
assert ci_lock['packages']['node_modules/@anthropic-ai/claude-code']['version'] == ci_pin

spec = importlib.util.spec_from_file_location('package_plugin', ROOT / 'scripts/package_plugin.py')
package = importlib.util.module_from_spec(spec)
spec.loader.exec_module(package)
with tempfile.TemporaryDirectory() as temp:
    output = package.build(Path(temp) / 'plugin.zip')
    with zipfile.ZipFile(output) as archive:
        assert set(archive.namelist()) == set(package.FILES)
        assert 'plugin.json' not in archive.namelist(), 'Do not upload unsupported legacy root descriptor'
        assert all(not name.startswith(('.git/', '.agents/', '.codex/')) for name in archive.namelist())
        assert archive.testzip() is None
        archive.extractall(Path(temp) / 'isolated')
    isolated = Path(temp) / 'isolated/skills/markmap'
    assert (isolated / 'agents/openai.yaml').is_file()
    assert (isolated / 'assets/template.html').is_file()
    renderer = isolated / 'scripts/render.sh'
    assert renderer.is_file()
    subprocess.run(['bash', '-n', str(renderer)], check=True)
    assert 'markmap-cli@0.18.12' in renderer.read_text()
    # Stub npx to verify adversarial filenames stay positional; no network or installs.
    stub = Path(temp) / 'npx'
    stub.write_text('#!/usr/bin/env python3\nimport json,sys\nprint(json.dumps(sys.argv[1:]))\n')
    stub.chmod(0o755)
    malicious = Path(temp) / '--help.md'
    malicious.write_text('# Safe fixture')
    import os
    env = dict(os.environ, PATH=f'{temp}:' + os.environ['PATH'])
    result = subprocess.run(['bash', str(renderer), str(malicious), str(Path(temp)/'map.html')], env=env, text=True, capture_output=True, check=True)
    args = json.loads(result.stdout.splitlines()[0])
    assert args[-2:] == ['--', str(malicious)]
    try:
        package.build(output)
        raise AssertionError('Existing output must not be overwritten')
    except ValueError:
        pass

# HTML parser regression: mixed-case script endings and markup cannot exit JSON data.
class Scripts(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.count = 0
    def handle_starttag(self, tag, attrs):
        if tag == 'script': self.count += 1

source = (ROOT / 'skills/markmap/assets/template.html').read_text()
payload = '</ScRiPt><script>alert(1)</script><img src=x onerror=alert(2)> & \\ "'
encoded = json.dumps(payload).replace('<', '\\u003c')
assert json.loads(encoded) == payload
baseline = Scripts(); baseline.feed(source.replace('{{MARKDOWN_JSON}}', '"safe"'))
attack = Scripts(); attack.feed(source.replace('{{MARKDOWN_JSON}}', encoded))
assert baseline.count == attack.count
assert '{{MARKDOWN_CONTENT}}' not in source
assert 'JSON.parse(mdEl.textContent)' in source
print('PASS: submission paths, ZIP allowlist, isolated resources, CLI argument boundary, JSON parser breakout')
