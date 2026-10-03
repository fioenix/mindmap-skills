#!/usr/bin/env bash
set -euo pipefail

# Automated validation & test suite for mindmap-skills
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

echo "=== [1/5] Validating JSON Manifests ==="
for file in package.json plugin.json .claude-plugin/plugin.json .claude-plugin/marketplace.json .codex/plugin.json; do
  if [[ ! -f "$file" ]]; then
    echo "❌ Missing manifest: $file" >&2
    exit 1
  fi
  jq . "$file" >/dev/null
  echo "  ✓ Valid JSON: $file"
done

if command -v claude &>/dev/null; then
  claude plugin validate --strict . >/dev/null
  claude plugin validate --strict .claude-plugin/plugin.json >/dev/null
  echo "  ✓ Official Claude Code CLI strict validation passed"
fi

echo ""
echo "=== [2/5] Validating Manifest Metadata & Icons ==="
CLAUDE_ICON=$(jq -r '.icon // empty' .claude-plugin/plugin.json)
CODEX_ICON=$(jq -r '.icon // empty' .codex/plugin.json)
UNIVERSAL_ICON=$(jq -r '.icon // empty' plugin.json)

if [[ -z "$CLAUDE_ICON" || ! -f "$CLAUDE_ICON" ]]; then
  echo "❌ Claude Code icon missing or path invalid: $CLAUDE_ICON" >&2
  exit 1
fi
echo "  ✓ Claude Code icon resolved: $CLAUDE_ICON"

if [[ -z "$CODEX_ICON" || ! -f "$CODEX_ICON" ]]; then
  echo "❌ Codex icon missing or path invalid: $CODEX_ICON" >&2
  exit 1
fi
echo "  ✓ Codex icon resolved: $CODEX_ICON"

if [[ -z "$UNIVERSAL_ICON" || ! -f "$UNIVERSAL_ICON" ]]; then
  echo "❌ Universal icon missing or path invalid: $UNIVERSAL_ICON" >&2
  exit 1
fi
echo "  ✓ Universal icon resolved: $UNIVERSAL_ICON"

echo ""
echo "=== [3/5] Validating Assets & File Formats ==="
file assets/icon.png | grep -q "PNG image data"
echo "  ✓ assets/icon.png is valid PNG"

grep -q "<svg" assets/icon.svg
echo "  ✓ assets/icon.svg is valid SVG"

grep -q "<svg" logo.svg
echo "  ✓ logo.svg is valid SVG"

echo ""
echo "=== [4/5] Checking Scripts & Syntax ==="
bash -n scripts/render.sh
if [[ ! -x scripts/render.sh ]]; then
  echo "❌ scripts/render.sh is not executable" >&2
  exit 1
fi
echo "  ✓ scripts/render.sh syntax OK and executable"

echo ""
echo "=== [5/5] Security & Template Posture ==="
TEMPLATE="skills/markmap/assets/template.html"
if ! grep -q "Content-Security-Policy" "$TEMPLATE"; then
  echo "❌ Missing CSP header in $TEMPLATE" >&2
  exit 1
fi
echo "  ✓ Content-Security-Policy present in template"

if ! grep -q "markmap-autoloader" "$TEMPLATE"; then
  echo "❌ Missing markmap-autoloader script in $TEMPLATE" >&2
  exit 1
fi
echo "  ✓ Markmap autoloader CDN present in template"

SKILL_SPEC="skills/markmap/SKILL.md"
if ! grep -q "Security Guardrail" "$SKILL_SPEC"; then
  echo "❌ Missing Security Guardrail in $SKILL_SPEC" >&2
  exit 1
fi
echo "  ✓ Security Guardrail documented in SKILL.md"

echo ""
echo "🎉 ALL VALIDATION CHECKS PASSED SUCCESSFULLY!"
