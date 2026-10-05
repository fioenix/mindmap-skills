#!/usr/bin/env bash
set -euo pipefail

# Automated validation & test suite for mindmap-skills
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

echo "=========================================================="
echo "   🧠 MINDMAP-SKILLS MARKETPLACE READINESS VALIDATOR      "
echo "=========================================================="

echo ""
echo "=== [1/8] Manifest Integrity & JSON Syntax ==="
MANIFEST_FILES=(
  "package.json"
  "plugin.json"
  ".claude-plugin/plugin.json"
  ".claude-plugin/marketplace.json"
  ".codex-plugin/plugin.json"
  ".codex/plugin.json"
  ".agents/plugins/marketplace.json"
)

for file in "${MANIFEST_FILES[@]}"; do
  if [[ ! -f "$file" ]]; then
    echo "❌ Missing manifest file: $file" >&2
    exit 1
  fi
  jq . "$file" >/dev/null
  echo "  ✓ Valid JSON: $file"
done

echo ""
echo "=== [2/8] Version Parity Across Manifests ==="
PKG_VER=$(jq -r '.version' package.json)
ROOT_VER=$(jq -r '.version' plugin.json)
CLAUDE_VER=$(jq -r '.version' .claude-plugin/plugin.json)
CODEX_VER=$(jq -r '.version' .codex-plugin/plugin.json)
LEGACY_CODEX_VER=$(jq -r '.version' .codex/plugin.json)

echo "  Versions detected: pkg=$PKG_VER, root=$ROOT_VER, claude=$CLAUDE_VER, codex=$CODEX_VER"
if [[ "$PKG_VER" != "$ROOT_VER" || "$PKG_VER" != "$CLAUDE_VER" || "$PKG_VER" != "$CODEX_VER" || "$PKG_VER" != "$LEGACY_CODEX_VER" ]]; then
  echo "❌ Version mismatch detected across manifests!" >&2
  exit 1
fi
echo "  ✓ All manifests share unified version: $PKG_VER"

echo ""
echo "=== [3/8] OpenAI / Codex Marketplace Metadata Limits ==="
DISPLAY_NAME=$(jq -r '.interface.displayName // empty' .codex-plugin/plugin.json)
SHORT_DESC=$(jq -r '.interface.shortDescription // empty' .codex-plugin/plugin.json)
DEV_NAME=$(jq -r '.interface.developerName // empty' .codex-plugin/plugin.json)

if [[ ${#DISPLAY_NAME} -gt 30 || ${#DISPLAY_NAME} -eq 0 ]]; then
  echo "❌ displayName must be 1-30 chars. Got: '${DISPLAY_NAME}' (${#DISPLAY_NAME})" >&2
  exit 1
fi
echo "  ✓ displayName (${#DISPLAY_NAME} chars <= 30): '$DISPLAY_NAME'"

if [[ ${#SHORT_DESC} -gt 30 || ${#SHORT_DESC} -eq 0 ]]; then
  echo "❌ shortDescription must be 1-30 chars. Got: '${SHORT_DESC}' (${#SHORT_DESC})" >&2
  exit 1
fi
echo "  ✓ shortDescription (${#SHORT_DESC} chars <= 30): '$SHORT_DESC'"

if [[ ${#DEV_NAME} -gt 80 || ${#DEV_NAME} -eq 0 ]]; then
  echo "❌ developerName must be 1-80 chars. Got: '${DEV_NAME}' (${#DEV_NAME})" >&2
  exit 1
fi
echo "  ✓ developerName (${#DEV_NAME} chars <= 80): '$DEV_NAME'"

PROMPT_COUNT=$(jq '.interface.defaultPrompt | length' .codex-plugin/plugin.json)
if [[ "$PROMPT_COUNT" -gt 3 || "$PROMPT_COUNT" -eq 0 ]]; then
  echo "❌ defaultPrompt must have 1-3 prompts. Got: $PROMPT_COUNT" >&2
  exit 1
fi
for i in $(seq 0 $((PROMPT_COUNT - 1))); do
  p=$(jq -r ".interface.defaultPrompt[$i]" .codex-plugin/plugin.json)
  if [[ ${#p} -gt 128 ]]; then
    echo "❌ defaultPrompt[$i] exceeds 128 characters (${#p} chars): $p" >&2
    exit 1
  fi
  if [[ "$p" =~ @ ]]; then
    echo "❌ defaultPrompt[$i] must not contain @mention: $p" >&2
    exit 1
  fi
  echo "  ✓ defaultPrompt[$i] (${#p} chars <= 128): '$p'"
done

BRAND_COLOR=$(jq -r '.interface.brandColor // empty' .codex-plugin/plugin.json)
BRAND_DARK=$(jq -r '.interface.brandColorDark // empty' .codex-plugin/plugin.json)
if [[ -z "$BRAND_COLOR" || -z "$BRAND_DARK" ]]; then
  echo "❌ Missing brandColor or brandColorDark in .codex-plugin/plugin.json" >&2
  exit 1
fi
echo "  ✓ Brand colors configured: light=$BRAND_COLOR, dark=$BRAND_DARK"

echo ""
echo "=== [4/8] Claude Code Listing Compliance ==="
if command -v claude &>/dev/null; then
  claude plugin validate --strict . >/dev/null
  claude plugin validate --strict .claude-plugin/plugin.json >/dev/null
  echo "  ✓ Claude Code CLI strict validation passed"
else
  echo "  ⚠️ claude CLI not found in PATH; skipping CLI-level check"
fi

CLAUDE_DOCS=$(jq -r '.documentationUrl // empty' .claude-plugin/plugin.json)
CLAUDE_SUPPORT=$(jq -r '.supportUrl // empty' .claude-plugin/plugin.json)
CLAUDE_PRIVACY=$(jq -r '.privacyPolicyUrl // empty' .claude-plugin/plugin.json)
CLAUDE_TERMS=$(jq -r '.termsOfServiceUrl // empty' .claude-plugin/plugin.json)

if [[ -z "$CLAUDE_DOCS" || -z "$CLAUDE_SUPPORT" || -z "$CLAUDE_PRIVACY" || -z "$CLAUDE_TERMS" ]]; then
  echo "❌ Missing one or more required listing URLs in .claude-plugin/plugin.json" >&2
  exit 1
fi
echo "  ✓ Claude listing URLs verified (docs, support, privacy, terms)"

echo ""
echo "=== [5/8] Assets, Branding & Dark Mode Icons ==="
ASSET_FILES=(
  "assets/icon.svg"
  "assets/icon-dark.svg"
  "assets/icon.png"
  "logo.svg"
)
for asset in "${ASSET_FILES[@]}"; do
  if [[ ! -f "$asset" ]]; then
    echo "❌ Missing asset: $asset" >&2
    exit 1
  fi
done

file assets/icon.png | grep -q "PNG image data"
echo "  ✓ assets/icon.png is valid PNG"

grep -q "<svg" assets/icon.svg
echo "  ✓ assets/icon.svg is valid SVG"

grep -q "<svg" assets/icon-dark.svg
echo "  ✓ assets/icon-dark.svg is valid SVG"

grep -q "<svg" logo.svg
echo "  ✓ logo.svg is valid SVG"

echo ""
echo "=== [6/8] Legal, Privacy & Community Documents ==="
DOC_FILES=(
  "LICENSE"
  "README.md"
  "CONTRIBUTING.md"
  "PRIVACY.md"
  "TERMS.md"
)
for doc in "${DOC_FILES[@]}"; do
  if [[ ! -s "$doc" ]]; then
    echo "❌ Missing or empty documentation file: $doc" >&2
    exit 1
  fi
  echo "  ✓ Document verified: $doc"
done

echo ""
echo "=== [7/8] Skill Specification & Security Guardrails ==="
SKILL_SPEC="skills/markmap/SKILL.md"
if [[ ! -f "$SKILL_SPEC" ]]; then
  echo "❌ Missing $SKILL_SPEC" >&2
  exit 1
fi

REQUIRED_SECTIONS=(
  "Scope & Activation Boundaries"
  "When NOT to Trigger"
  "Official Frontmatter Standard"
  "Cognitive Structuring Rules"
  "Dependency Contract & Graceful Fallback"
  "Security Posture & Privacy Guardrails"
)
for sec in "${REQUIRED_SECTIONS[@]}"; do
  if ! grep -q "$sec" "$SKILL_SPEC"; then
    echo "❌ Missing section '$sec' in $SKILL_SPEC" >&2
    exit 1
  fi
done
echo "  ✓ All architectural sections present in SKILL.md"

TEMPLATE="skills/markmap/assets/template.html"
if ! grep -q "Content-Security-Policy" "$TEMPLATE"; then
  echo "❌ Missing Content-Security-Policy in $TEMPLATE" >&2
  exit 1
fi
echo "  ✓ Content-Security-Policy verified in template.html"

bash -n scripts/render.sh
if [[ ! -x scripts/render.sh ]]; then
  echo "❌ scripts/render.sh is not executable" >&2
  exit 1
fi
echo "  ✓ scripts/render.sh syntax OK and executable"

echo ""
echo "=== [8/8] Git Index Hygiene & Untracked Exclusions ==="
TRACKED_IGNORED=$(git ls-files -ci --exclude-standard)
if [[ -n "$TRACKED_IGNORED" ]]; then
  echo "❌ Tracked files exist that match .gitignore rules:" >&2
  echo "$TRACKED_IGNORED" >&2
  exit 1
fi
echo "  ✓ Zero tracked ignored files (git ls-files -ci is clean)"

echo ""
echo "=========================================================="
echo " 🎉 ALL 8 VALIDATION GATES PASSED! READY FOR SUBMISSION.   "
echo "=========================================================="
