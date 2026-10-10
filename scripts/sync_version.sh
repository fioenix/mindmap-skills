#!/usr/bin/env bash
set -euo pipefail

# Keep every manifest's version aligned with package.json (the single source of truth).
# Usage: ./sync_version.sh [<new-version> | --check]
#   (no argument)   copy package.json's version into every other manifest
#   <new-version>   set package.json to <new-version>, then sync
#   --check         list every version and exit 1 on any mismatch (no writes)

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

PLUGIN_NAME="mindmap-skills"

# Parallel arrays: manifest file and the jq path of its version field.
# .agents/plugins/marketplace.json carries no version field and is intentionally absent.
VERSIONED_FILES=(
  "plugin.json"
  ".claude-plugin/plugin.json"
  ".claude-plugin/marketplace.json"
  ".codex-plugin/plugin.json"
  ".codex/plugin.json"
  "package-lock.json"
  "package-lock.json"
)
VERSION_PATHS=(
  ".version"
  ".version"
  "(.plugins[] | select(.name == \$name) | .version)"
  ".version"
  ".version"
  ".version"
  ".packages[\"\"].version"
)

read_version() {
  jq -r --arg name "$PLUGIN_NAME" "$2 // empty" "$1"
}

write_version() {
  local tmp
  tmp="$(mktemp)"
  jq --arg name "$PLUGIN_NAME" --arg v "$3" "$2 = \$v" "$1" >"$tmp"
  # Overwrite in place so the file keeps its permissions.
  cat "$tmp" >"$1"
  rm -f "$tmp"
}

MODE="sync"
case "${1:-}" in
  "") ;;
  --check) MODE="check" ;;
  *)
    if [[ ! "$1" =~ ^[0-9]+\.[0-9]+\.[0-9]+(-[0-9A-Za-z.-]+)?$ ]]; then
      echo "Error: '$1' is not a semantic version (expected X.Y.Z[-pre])." >&2
      exit 1
    fi
    write_version "package.json" ".version" "$1"
    ;;
esac

PKG_VER="$(read_version package.json .version)"
if [[ -z "$PKG_VER" ]]; then
  echo "Error: package.json has no version." >&2
  exit 1
fi
echo "  package.json: $PKG_VER"

MISMATCH=0
for i in "${!VERSIONED_FILES[@]}"; do
  file="${VERSIONED_FILES[$i]}"
  path="${VERSION_PATHS[$i]}"
  ver="$(read_version "$file" "$path")"
  if [[ "$ver" == "$PKG_VER" ]]; then
    echo "  $file: $ver"
  elif [[ "$MODE" == "check" ]]; then
    echo "  $file: ${ver:-<missing>}  ← expected $PKG_VER" >&2
    MISMATCH=1
  else
    write_version "$file" "$path" "$PKG_VER"
    echo "  $file: ${ver:-<missing>} → $PKG_VER"
  fi
done

if [[ "$MISMATCH" -ne 0 ]]; then
  echo "❌ Version mismatch detected across manifests! Run scripts/sync_version.sh to align them." >&2
  exit 1
fi
