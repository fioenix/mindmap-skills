# Release Readiness Dossier

Tracking document and release verification dossier for `mindmap-skills` conforming to the marketplace readiness standards defined in `04-PROCEDURAL/Workflows/skill-plugin-marketplace-readiness.md`.

---

## 1. Release Dossier

### Claude Code Release Profile
```yaml
project: mindmap-skills
platform: claude
target: self-install (and directory submission ready)
version: 0.1.2
source_ref: v0.1.2 (annotated tag)
source_sha: e8c0636
artifact_sha256: not-applicable (git-sourced)
tool_versions:
  claude_cli: 2.1.281+
  ci_claude_cli: 2.1.292 (pinned in package-lock.json)
  bash: 3.2+ / zsh 5.9
  jq: 1.7+
automated_checks:  # run 2026-10-10 on e8c0636
  - CI run 38028811072 on main @ e8c0636 (Claude Code CLI 2.1.292) -> ALL 8 GATES PASSED, CLI strict gate PASSED
  - local claude plugin validate --strict . (CLI 2.1.296) -> PASSED
  - local claude plugin validate --strict .claude-plugin/plugin.json (CLI 2.1.296) -> PASSED
  - local bash tests/validate.sh -> ALL 8 GATES PASSED
native_checks:  # last run on 0.1.0 (87b6e8f); not repeated for 0.1.1 or 0.1.2, see not_run
  - client: Claude Code CLI v2.1.281
    version: 0.1.0
    evidence: plugin loaded via marketplace add / plugin install and tested invocation
  - client: Antigravity IDE (macOS)
    version: 0.1.0
    evidence: symlinked to ~/.gemini/config/skills/markmap, loaded successfully
not_run:
  - scope: Directory automated ingestion
    reason: Requires owner manual web portal submission on claude.com/directory
  - scope: Native install + invocation of 0.1.2 (Claude Code, Antigravity), including icon rendering in client UI
    reason: Requires owner to reinstall the plugin in local clients; 0.1.0 evidence does not carry over
portal_findings: none (all schema & manifest constraints satisfied)
publisher: Fioenix (https://github.com/fioenix)
status: pending-native-recheck
live_verification:
  url: https://github.com/fioenix/mindmap-skills
  version: 0.1.2
  evidence: origin/main @ e8c0636 and tag v0.1.2 report 0.1.2 in all 6 versioned manifests and package-lock.json
  date: 2026-10-10
```

### OpenAI Codex Release Profile
```yaml
project: mindmap-skills
platform: openai
target: self-install (and marketplace ready)
version: 0.1.2
source_ref: v0.1.2 (annotated tag)
source_sha: e8c0636
artifact_sha256: not-applicable (git-sourced)
tool_versions:
  jq: 1.7+
  python: 3.12+
automated_checks:  # run 2026-10-10 on e8c0636
  - CI run 38028811072 on main @ e8c0636 -> ALL 8 GATES PASSED
  - local bash tests/validate.sh -> ALL 8 GATES PASSED
  - metadata string lengths verified:
      displayName: 14 chars (<= 30)
      shortDescription: 28 chars (<= 30)
      developerName: 7 chars (<= 80)
      defaultPrompt: 3 prompts (each <= 128 chars, no @mentions)
      brandColor: "#9750C4" (contrast ratio 4.54:1 with white >= 2:1)
      brandColorDark: "#7FE2CE" (contrast ratio 11.53:1 with #212121 >= 2:1)
native_checks:  # last run on 0.1.0 (87b6e8f); not repeated for 0.1.1 or 0.1.2, see not_run
  - client: Codex CLI / Agents SDK
    version: 0.1.0
    evidence: discovered from .agents/skills/markmap and .agents/plugins/marketplace.json
not_run:
  - scope: OpenAI Directory manual ZIP upload
    reason: Awaiting owner portal action
  - scope: Native discovery of 0.1.2 (Codex CLI / Agents SDK), including icon rendering in client UI
    reason: Requires owner to reload the plugin in the local client; 0.1.0 evidence does not carry over
portal_findings: none
publisher: Fioenix (https://github.com/fioenix)
status: pending-native-recheck
live_verification:
  url: https://github.com/fioenix/mindmap-skills
  version: 0.1.2
  evidence: origin/main @ e8c0636 and tag v0.1.2 report 0.1.2 in all 6 versioned manifests and package-lock.json
  date: 2026-10-10
```

---

## 2. Compliance Checklist

| Audit Category | Status | Evidence / Verification Notes |
|---|---|---|
| **Purpose & Scope** | PASSED | Clear activation boundaries, trigger/do-not-trigger, clarification, and stop conditions in `SKILL.md` |
| **Cognitive Structuring** | PASSED | Enforces Miller's Law (4–7 main branches), MECE taxonomy, depth 3–4, brevity ≤ 8 words/node |
| **Zero Daemon / Token Tax** | PASSED | 0 background daemons, no headless Chromium dependency, 0 idle token overhead |
| **Zero Dependency Core** | PASSED | Core workflow runs purely on Markdown + static HTML template, zero npm/CLI requirements; the only `devDependency` (`@anthropic-ai/claude-code`) is CI tooling and is not in the `package.json` `files` list |
| **Graceful Fallback** | PASSED | Transparent fallback to static HTML artifact if `markmap-cli` is absent |
| **Manifests Parity** | PASSED | Version 0.1.2 unified across all 6 versioned manifests and both version fields of `package-lock.json`, enforced by `scripts/sync_version.sh --check` (gate [2/8]); `.agents/plugins/marketplace.json` carries no version field |
| **Listing URLs** | PASSED | `documentationUrl`, `supportUrl`, `privacyPolicyUrl`, `termsOfServiceUrl` declared in full |
| **OpenAI String Limits** | PASSED | `displayName` (14 ≤ 30), `shortDescription` (28 ≤ 30), `defaultPrompt` (≤ 128 chars) |
| **Brand Colors & Contrast** | PASSED | `#9750C4` (4.54:1 on white) & `#7FE2CE` (11.53:1 on dark) adhering to FINOLABS tokens |
| **Vector Assets** | PASSED | Monoline mark (hollow root + 3 branches), one brand color per theme on a transparent canvas: `icon.svg` (`#9750C4`), `icon-dark.svg` (`#7FE2CE`), `logo.svg`, and `icon.png` (512x512 RGBA, transparent); all generated by `scripts/build_icon.py` |
| **Legal & Privacy** | PASSED | `LICENSE`, `PRIVACY.md`, `TERMS.md`, `CONTRIBUTING.md` complete in 100% English |
| **Claude CLI Strict** | PASSED | `claude plugin validate --strict .` passes with zero warnings |
| **Git Index Hygiene** | PASSED | `git ls-files -ci --exclude-standard` returns empty |
| **CI Supply Chain** | PASSED | `actions/checkout` (v7.0.1) and `actions/setup-node` (v7.1.0) pinned by commit SHA; repository setting `sha_pinning_required: true`; Claude CLI pinned in `package-lock.json` and installed with `npm ci`; CI fails if `claude` is missing from `PATH` |
| **Dependency Updates** | PASSED | Dependabot tracks `github-actions` and `npm` weekly with a 7-day `cooldown`; security updates enabled |
| **Default Branch Protection** | PASSED | Ruleset "Default branch protection" (no bypass): PR required, `Validate Manifests & Test Suite` must pass on an up-to-date branch, linear history, no force-push or deletion. Ruleset "Require review for non-admins": 1 approval, stale approvals dismissed; admins may bypass only through a PR |
| **Secret Protection** | PASSED | Secret scanning and push protection enabled; default workflow token is read-only |
