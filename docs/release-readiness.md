# Release Readiness Dossier

Tracking document and release verification dossier for `mindmap-skills` conforming to the marketplace readiness standards defined in `04-PROCEDURAL/Workflows/skill-plugin-marketplace-readiness.md`.

---

## 1. Release Dossier

### Claude Code Release Profile
```yaml
project: mindmap-skills
platform: claude
target: self-install (and directory submission ready)
version: 0.1.1
source_sha: 822afa5
artifact_sha256: not-applicable (git-sourced)
tool_versions:
  claude_cli: 2.1.281+
  bash: 3.2+ / zsh 5.9
  jq: 1.7+
automated_checks:  # re-run 2026-10-10 on 0.1.1 manifests, Claude Code CLI 2.1.296
  - claude plugin validate --strict . -> PASSED
  - claude plugin validate --strict .claude-plugin/plugin.json -> PASSED
  - bash tests/validate.sh -> ALL 8 GATES PASSED
native_checks:  # last run on 0.1.0 (87b6e8f); not repeated for 0.1.1, see not_run
  - client: Claude Code CLI v2.1.281
    version: 0.1.0
    evidence: plugin loaded via marketplace add / plugin install and tested invocation
  - client: Antigravity IDE (macOS)
    version: 0.1.0
    evidence: symlinked to ~/.gemini/config/skills/markmap, loaded successfully
not_run:
  - scope: Directory automated ingestion
    reason: Requires owner manual web portal submission on claude.com/directory
  - scope: Native install + invocation of 0.1.1 (Claude Code, Antigravity)
    reason: Requires owner to reinstall the plugin in local clients; 0.1.0 evidence does not carry over
portal_findings: none (all schema & manifest constraints satisfied)
publisher: Fioenix (https://github.com/fioenix)
status: pending-native-recheck
live_verification:
  url: https://github.com/fioenix/mindmap-skills
  version: 0.1.1
  evidence: origin/main @ 822afa5 reports 0.1.1 in all 6 versioned manifests
  date: 2026-10-10
```

### OpenAI Codex Release Profile
```yaml
project: mindmap-skills
platform: openai
target: self-install (and marketplace ready)
version: 0.1.1
source_sha: 822afa5
artifact_sha256: not-applicable (git-sourced)
tool_versions:
  jq: 1.7+
  python: 3.12+
automated_checks:  # re-run 2026-10-10 on 0.1.1 manifests
  - bash tests/validate.sh -> ALL 8 GATES PASSED
  - metadata string lengths verified:
      displayName: 14 chars (<= 30)
      shortDescription: 28 chars (<= 30)
      developerName: 7 chars (<= 80)
      defaultPrompt: 3 prompts (each <= 128 chars, no @mentions)
      brandColor: "#9750C4" (contrast ratio 4.54:1 with white >= 2:1)
      brandColorDark: "#7FE2CE" (contrast ratio 11.53:1 with #212121 >= 2:1)
native_checks:  # last run on 0.1.0 (87b6e8f); not repeated for 0.1.1, see not_run
  - client: Codex CLI / Agents SDK
    version: 0.1.0
    evidence: discovered from .agents/skills/markmap and .agents/plugins/marketplace.json
not_run:
  - scope: OpenAI Directory manual ZIP upload
    reason: Awaiting owner portal action
  - scope: Native discovery of 0.1.1 (Codex CLI / Agents SDK)
    reason: Requires owner to reload the plugin in the local client; 0.1.0 evidence does not carry over
portal_findings: none
publisher: Fioenix (https://github.com/fioenix)
status: pending-native-recheck
live_verification:
  url: https://github.com/fioenix/mindmap-skills
  version: 0.1.1
  evidence: origin/main @ 822afa5 reports 0.1.1 in all 6 versioned manifests
  date: 2026-10-10
```

---

## 2. Compliance Checklist

| Audit Category | Status | Evidence / Verification Notes |
|---|---|---|
| **Purpose & Scope** | PASSED | Clear activation boundaries, trigger/do-not-trigger, clarification, and stop conditions in `SKILL.md` |
| **Cognitive Structuring** | PASSED | Enforces Miller's Law (4–7 main branches), MECE taxonomy, depth 3–4, brevity ≤ 8 words/node |
| **Zero Daemon / Token Tax** | PASSED | 0 background daemons, no headless Chromium dependency, 0 idle token overhead |
| **Zero Dependency Core** | PASSED | Core workflow runs purely on Markdown + static HTML template, zero npm/CLI requirements |
| **Graceful Fallback** | PASSED | Transparent fallback to static HTML artifact if `markmap-cli` is absent |
| **Manifests Parity** | PASSED | Version 0.1.1 unified across all 6 versioned manifests, enforced by `scripts/sync_version.sh --check` (gate [2/8]); `.agents/plugins/marketplace.json` carries no version field |
| **Listing URLs** | PASSED | `documentationUrl`, `supportUrl`, `privacyPolicyUrl`, `termsOfServiceUrl` declared in full |
| **OpenAI String Limits** | PASSED | `displayName` (14 ≤ 30), `shortDescription` (28 ≤ 30), `defaultPrompt` (≤ 128 chars) |
| **Brand Colors & Contrast** | PASSED | `#9750C4` (4.54:1 on white) & `#7FE2CE` (11.53:1 on dark) adhering to FINOLABS tokens |
| **Vector Assets** | PASSED | `icon.svg`, `icon-dark.svg`, `icon.png` (512x512), and `logo.svg` valid and verified |
| **Legal & Privacy** | PASSED | `LICENSE`, `PRIVACY.md`, `TERMS.md`, `CONTRIBUTING.md` complete in 100% English |
| **Claude CLI Strict** | PASSED | `claude plugin validate --strict .` passes with zero warnings |
| **Git Index Hygiene** | PASSED | `git ls-files -ci --exclude-standard` returns empty |
