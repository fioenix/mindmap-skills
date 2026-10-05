# Hồ sơ sẵn sàng phát hành (Release Readiness Dossier)

Tài liệu kiểm chứng và theo dõi trạng thái phát hành của `mindmap-skills` theo chuẩn quy định tại `04-PROCEDURAL/Workflows/skill-plugin-marketplace-readiness.md`.

---

## 1. Release Dossier

### Hồ sơ phát hành Claude Code
```yaml
project: mindmap-skills
platform: claude
target: self-install (and directory submission ready)
version: 1.0.0
source_sha: 95b9efe
artifact_sha256: not-applicable (git-sourced)
tool_versions:
  claude_cli: 2.1.281+
  bash: 3.2+ / zsh 5.9
  jq: 1.7+
automated_checks:
  - claude plugin validate --strict . -> PASSED
  - claude plugin validate --strict .claude-plugin/plugin.json -> PASSED
  - bash tests/validate.sh -> ALL 8 GATES PASSED
native_checks:
  - client: Claude Code CLI v2.1.281
    evidence: plugin loaded via marketplace add / plugin install and tested invocation
  - client: Antigravity IDE (macOS)
    evidence: symlinked to ~/.gemini/config/skills/markmap, loaded successfully
not_run:
  - scope: Directory automated ingestion
    reason: Requires owner manual web portal submission on claude.com/directory
portal_findings: none (all schema & manifest constraints satisfied)
publisher: Fioenix (https://github.com/fioenix)
status: ready-to-submit
live_verification:
  url: https://github.com/fioenix/mindmap-skills
  version: 1.0.0
  date: 2026-10-05
```

### Hồ sơ phát hành OpenAI Codex
```yaml
project: mindmap-skills
platform: openai
target: self-install (and marketplace ready)
version: 1.0.0
source_sha: 95b9efe
artifact_sha256: not-applicable (git-sourced)
tool_versions:
  jq: 1.7+
  python: 3.12+
automated_checks:
  - bash tests/validate.sh -> ALL 8 GATES PASSED
  - metadata string lengths verified:
      displayName: 14 chars (<= 30)
      shortDescription: 28 chars (<= 30)
      developerName: 7 chars (<= 80)
      defaultPrompt: 3 prompts (each <= 128 chars, no @mentions)
      brandColor: "#9750C4" (contrast ratio 4.54:1 with white >= 2:1)
      brandColorDark: "#7FE2CE" (contrast ratio 11.53:1 with #212121 >= 2:1)
native_checks:
  - client: Codex CLI / Agents SDK
    evidence: discovered from .agents/skills/markmap and .agents/plugins/marketplace.json
not_run:
  - scope: OpenAI Directory manual ZIP upload
    reason: Awaiting owner portal action
portal_findings: none
publisher: Fioenix (https://github.com/fioenix)
status: ready-to-submit
live_verification:
  url: https://github.com/fioenix/mindmap-skills
  version: 1.0.0
  date: 2026-10-05
```

---

## 2. Checklist đối chiếu chi tiết

| Hạng mục kiểm tra | Trạng thái | Bằng chứng / Ghi chú |
|---|---|---|
| **Công dụng & Phạm vi** | ĐẠT | Quy định rõ điều kiện gọi, không gọi, hỏi lại, điều kiện dừng trong `SKILL.md` |
| **Cognitive Structuring** | ĐẠT | Enforce 4–7 nhánh chính (Miller's Law), depth 3–4, brevity ≤ 8 từ |
| **Zero Daemon / Token Tax** | ĐẠT | 0 background daemons, không phụ thuộc headless Chromium |
| **Zero Dependency Core** | ĐẠT | Core chạy thuần markdown + template HTML, không yêu cầu npm/CLI |
| **Graceful Fallback** | ĐẠT | Khi không có `markmap-cli`, fallback tự động sang static template |
| **Manifests Parity** | ĐẠT | Phiên bản 1.0.0 đồng nhất trên tất cả 7 file manifests |
| **Listing URLs** | ĐẠT | `documentationUrl`, `supportUrl`, `privacyPolicyUrl`, `termsOfServiceUrl` khai báo đầy đủ |
| **OpenAI String Limits** | ĐẠT | `displayName` (14 ≤ 30), `shortDescription` (28 ≤ 30), `defaultPrompt` (≤ 128) |
| **Brand Colors & Contrast** | ĐẠT | `#9750C4` (4.54:1 với trắng) & `#7FE2CE` (11.53:1 với dark) theo FINOLABS Design System |
| **Vector Assets** | ĐẠT | `icon.svg`, `icon-dark.svg`, `icon.png` (512x512) và `logo.svg` hợp lệ |
| **Legal & Privacy** | ĐẠT | `LICENSE`, `PRIVACY.md`, `TERMS.md`, `CONTRIBUTING.md` đầy đủ |
| **Claude CLI Strict** | ĐẠT | `claude plugin validate --strict .` vượt qua không cảnh báo |
| **Git Index Hygiene** | ĐẠT | `git ls-files -ci --exclude-standard` rỗng |
