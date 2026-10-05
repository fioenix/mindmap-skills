<p align="center">
  <img src="assets/icon.svg" width="96" height="96" alt="mindmap-skills icon" />
</p>

<h1 align="center">mindmap-skills</h1>

<p align="center">
  <b>Universal, lightweight Markmap mindmap plugin for AI Agents (Claude Code, OpenAI Codex, Google Antigravity).</b>
</p>

<p align="center">
  <a href="https://github.com/fioenix/mindmap-skills/actions/workflows/ci.yml"><img src="https://github.com/fioenix/mindmap-skills/actions/workflows/ci.yml/badge.svg" alt="CI Status" /></a>
  <a href="https://github.com/fioenix/mindmap-skills"><img src="https://img.shields.io/badge/Marketplace-Ready-7FE2CE?logo=anthropic&logoColor=0B0B17" alt="Marketplace Ready" /></a>
  <a href="https://github.com/fioenix/mindmap-skills"><img src="https://img.shields.io/badge/Runtime-Zero--Daemon-9750C4" alt="Zero Daemon" /></a>
  <a href="https://github.com/fioenix/mindmap-skills"><img src="https://img.shields.io/badge/Agents-Claude%20%7C%20Codex%20%7C%20Antigravity-18181b" alt="Agent Support" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT" /></a>
  <a href="CONTRIBUTING.md"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="PRs Welcome" /></a>
</p>

---

## ⚡ The Solution

Most AI mindmap solutions suffer from two fatal pitfalls:
1. **Bloated Daemon & Token Tax**: Running persistent background server processes, dragging in Playwright and a 300MB Chromium headless browser just to take a screenshot, while permanently burning 1,000+ tokens of schema definitions in every conversation turn.
2. **Cognitive Sprawl**: Dumping raw paragraph-length prose into node trees, producing unreadable walls of text that defeat the visual purpose of a mindmap.

### Architecture Comparison

| Capability | Heavyweight MCP / Headless | Raw LLM Text | **mindmap-skills** |
|---|---|---|---|
| **Runtime Footprint** | 300MB+ Headless Chrome daemon | 0 MB | **0 MB (Zero daemon)** |
| **Idle Token Tax** | 1,000+ tokens burned per turn | 0 tokens | **0 token overhead** |
| **Cognitive Structuring** | None (unfiltered text dump) | Unstructured | **Miller's Law (4–7 branches, depth 3–4, ≤ 8 words)** |
| **Output Artifacts** | Static raster image (PNG) | Raw text | **Portable `.mindmap.md` + Interactive `.html`** |
| **Multi-Agent Parity** | Platform-specific | Inconsistent | **Claude Code · OpenAI Codex · Google Antigravity** |
| **Security Posture** | Process execution / Subshells | Safe | **Zero-privilege core + CSP-hardened template** |

---

## 📦 Quick Installation

### 1. Claude Code

#### Via Public Marketplace (Recommended):
In your Claude Code terminal session:
```text
/plugin marketplace add fioenix/mindmap-skills
/plugin install mindmap-skills@fioenix-plugins
```
Then invoke the skill directly in any conversation:
```text
/mindmap-skills:markmap Tạo sơ đồ tư duy cho kiến trúc microservices này
```

#### On Claude Desktop / Web UI:
1. Navigate to **Customize** → **Plugins** → **Add** → **Add marketplace** → **Add from a repository**.
2. Enter repository: `fioenix/mindmap-skills`.
3. In Discover, select **mindmap-skills** and click **Add**.
4. Invoke in chat using `/markmap` or via the `+` menu.

#### Local Development / Manual Link:
```bash
claude plugin add ~/Projects/mindmap-skills
```

---

### 2. OpenAI Codex & Agents SDK

#### Personal / Repository Catalog:
Codex discovers plugins from `.agents/plugins/marketplace.json` or skills placed in `.agents/skills/`:
```bash
# Workspace local
mkdir -p .agents/skills
cp -r ~/Projects/mindmap-skills/skills/markmap .agents/skills/

# Or machine-global
mkdir -p ~/.codex/skills
ln -s ~/Projects/mindmap-skills/skills/markmap ~/.codex/skills/markmap
```

---

### 3. Google Antigravity

#### Machine-Global:
```bash
mkdir -p ~/.gemini/config/skills
ln -s ~/Projects/mindmap-skills/skills/markmap ~/.gemini/config/skills/markmap
```

#### Workspace-Local:
```bash
mkdir -p .agents/skills
cp -r ~/Projects/mindmap-skills/skills/markmap .agents/skills/
```

---

## 📋 Cognitive Structuring & Markmap Syntax

Every generated mindmap adheres strictly to official Markmap standards:

```markdown
---
title: System Architecture
markmap:
  colorFreezeLevel: 2
---

## Core Gateway
- **Auth**: JWT verification with RSA
- **Rate Limit**: Token bucket at edge
- **Routing**: Dynamic endpoint dispatch

## Storage Layer
- **KV**: Session cache & token blacklist
- **D1**: SQLite transactional metadata
- **R2**: Blob and artifact storage

## Observability <!-- markmap: fold -->
- **Traces**: OpenTelemetry collectors
- **Metrics**: Cloudflare Analytics Engine
- **Audit**: Immutable append-only logs
```

### Cognitive Invariants:
* `title`: Frontmatter root node. Main branches start directly at `##`.
* `colorFreezeLevel: 2`: Freezes branch colors at depth 2 (each `##` gets a consistent distinct color for all descendants).
* **4–7 Main Branches**: Strictly enforces Miller's Law for working memory retention.
* **Concise Nodes (≤ 8 words)**: Punchline and keyword first. Strips narrative filler prose.
* `<!-- markmap: fold -->`: Automatically collapses dense or secondary sub-trees on load.
* `- [x]` / `- [ ]`: Interactive checklists.
* `$formula$`: Native math rendering via KaTeX.

---

## 🛠️ Repository Architecture

```text
mindmap-skills/
├── .github/
│   ├── workflows/
│   │   └── ci.yml              # Automated GitHub Actions CI workflow
│   ├── ISSUE_TEMPLATE/         # Structured bug & feature request templates
│   └── PULL_REQUEST_TEMPLATE.md# Pull request validation checklist
├── .claude-plugin/
│   ├── marketplace.json        # Claude Code marketplace catalog definition
│   └── plugin.json             # Claude Code plugin manifest (with URLs & icons)
├── .codex-plugin/
│   └── plugin.json             # OpenAI Codex plugin manifest (interface & translations)
├── .codex/
│   └── plugin.json             # Legacy Codex compatibility manifest
├── .agents/
│   └── plugins/
│       └── marketplace.json    # Agent ecosystem distribution catalog
├── agents/
│   └── openai.yaml             # Agent interface specification
├── plugin.json                 # Universal / Antigravity plugin descriptor
├── package.json                # npm / skills.sh package descriptor
├── assets/
│   ├── icon.svg                # Vector SVG icon (FINOLABS Design System)
│   ├── icon-dark.svg           # Dark mode vector SVG icon
│   └── icon.png                # 512x512 PNG marketplace icon
├── logo.svg                    # Root vector logo
├── LICENSE                     # MIT License
├── README.md                   # Product documentation & usage guide
├── CONTRIBUTING.md             # Contribution guidelines & offline testing
├── PRIVACY.md                  # Privacy policy & data governance
├── TERMS.md                    # Terms of service
├── skills/
│   └── markmap/
│       ├── SKILL.md            # Canonical skill instructions & prompt constraints
│       └── assets/
│           └── template.html   # Standalone HTML artifact template (CSP hardened)
├── scripts/
│   ├── build_icon.py           # Portable vector icon renderer
│   └── render.sh               # Hardened CLI helper (markmap-cli wrapper)
└── tests/
    └── validate.sh             # Automated validation & test suite (8 gates)
```

---

## 🔒 Security Posture & Privacy

* **Zero Backend & No Telemetry**: The skill does not communicate with any external backend or analytics service. Data remains strictly within the user's host environment.
* **XSS & Parser Breakout Protection**: The standalone template enforces Content Security Policy (CSP) headers and documents strict escaping of `</script` as `<\/script` to prevent premature script termination and DOM injection.
* **CLI Option Injection Guard**: `scripts/render.sh` passes flags before terminating argument parsing with `--` (`markmap-cli --offline -o "$OUTPUT" --no-open -- "$INPUT"`) to prevent malicious filenames from triggering CLI flags.
* **Sensitive Data Policy**: See [PRIVACY.md](PRIVACY.md) and [TERMS.md](TERMS.md).

---

## 📄 License & Community

* **License**: [MIT License](LICENSE) © [Fioenix](https://github.com/fioenix)
* **Contributing**: Read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting pull requests.
* **Issues & Feedback**: [GitHub Issues](https://github.com/fioenix/mindmap-skills/issues)
