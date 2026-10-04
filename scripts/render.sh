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
  echo "Error: 'npx' is required for CLI rendering. Please install Node.js/npx, or use the zero-dependency HTML template." >&2
  exit 3
fi

# Use --offline for self-contained HTML (immune to Safari file:// restrictions and offline usage)
# Flags must come BEFORE '--' so they are not treated as positional files
npx --yes markmap-cli --offline -o "$OUTPUT" --no-open -- "$INPUT"
echo "Rendered: $OUTPUT"
