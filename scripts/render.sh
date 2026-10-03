#!/usr/bin/env bash
set -euo pipefail

# Render a Markmap Markdown file to a standalone HTML file using markmap-cli.
# Usage: ./render.sh <input.md> [output.html]

INPUT="${1:-}"
if [[ -z "$INPUT" ]]; then
  echo "Usage: $0 <input.md> [output.html]" >&2
  exit 1
fi

if [[ ! -f "$INPUT" ]]; then
  echo "Error: Input file '$INPUT' does not exist." >&2
  exit 1
fi

OUTPUT="${2:-${INPUT%.*}.html}"

if ! command -v npx &>/dev/null; then
  echo "Error: 'npx' is required for CLI rendering. Please install Node.js/npx, or use the zero-dependency autoloader template." >&2
  exit 3
fi

# Use '--' to terminate flag parsing and prevent CLI argument injection
npx --yes markmap-cli -- "$INPUT" -o "$OUTPUT" --no-open
echo "Rendered: $OUTPUT"
