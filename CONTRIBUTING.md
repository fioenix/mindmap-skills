# Contributing to mindmap-skills

Thank you for contributing to `mindmap-skills`! Contributions aimed at refining cognitive structuring, enhancing Markmap syntax support, reinforcing visual reliability, or hardening security are welcome.

## 1. Core Principles

1. **Cognitive First**: Any modification to structuring rules (`SKILL.md`) must preserve core human cognitive bandwidth principles (MECE taxonomy, Miller's Law: 4–7 main branches, depth 3–4, brevity ≤ 8 words per node).
2. **Zero-Daemon & Zero-Token-Tax**: Do not introduce persistent background daemons (such as headless Chromium/Playwright) or schemas that incur token tax during idle conversation turns.
3. **Multi-Agent Parity**: Maintain simultaneous compliance across Claude Code, OpenAI Codex, and Google Antigravity.
4. **Security & Content Isolation**: Standalone HTML templates must maintain strict Content Security Policy (CSP) headers and escape `</script` tokens safely against XSS/DOM injection.

## 2. Offline Validation

Before committing or opening a pull request, run the complete validation test suite locally:

```bash
# Run the 8-gate automated test suite
npm test
# or
bash tests/validate.sh

# If the Claude CLI is installed, verify strict plugin compliance
claude plugin validate --strict .
```

The test suite validates:
- JSON integrity across all manifest descriptors (`package.json`, `plugin.json`, `.claude-plugin/`, `.codex-plugin/`, `.agents/`).
- Version parity across every versioned manifest via `scripts/sync_version.sh --check`. To bump, run `bash scripts/sync_version.sh <new-version>` instead of editing manifests by hand.
- String length constraints for marketplace listings (`displayName` ≤ 30, `shortDescription` ≤ 30, `defaultPrompt` ≤ 128 characters).
- Image and SVG asset format compliance (`assets/icon.svg`, `assets/icon-dark.svg`, `assets/icon.png`, `logo.svg`).
- Shell script syntax and executable permissions.
- Git index hygiene ensuring no ignored files are tracked (`git ls-files -ci --exclude-standard`).

## 3. Git Tracking & Exclusion Rules

- **Distribution Catalogs**: `.agents/plugins/marketplace.json` and `.claude-plugin/marketplace.json` are public distribution catalogs and **must be tracked**.
- **Local Tooling**: Local install directories (such as `.agents/skills/`), test caches, `.specify/`, `specs/`, or temporary files (`*.mindmap.html`) **must remain untracked**.
- Never commit private credentials, personal access tokens, or `.env` files.

## 4. Pull Request Workflow

1. Fork the repository and create a dedicated branch (`feature/...` or `fix/...`).
2. Make atomic, surgical changes aligned with the problem scope.
3. Ensure all 8 validation gates in `tests/validate.sh` pass cleanly (`PASS`).
4. Write clear commit messages starting with an action verb (Add, Fix, Update, Refactor, Docs).
5. Open a Pull Request on GitHub describing the motivation, test evidence, and affected surface.
