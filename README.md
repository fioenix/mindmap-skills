# 🧠 mindmap-skills

**Universal, lightweight Markmap mindmap plugin for AI Agents (Claude Code, OpenAI Codex, Google Antigravity).**

Designed and structured for 100% compliance with the marketplace & distribution standards of **Claude Code**, **Codex**, and **Antigravity**.

---

## ⚡ Why mindmap-skills?

Most AI mindmap solutions suffer from two fatal pitfalls:
1. **Bloated Daemon / Token Tax**: Running persistent background server processes, dragging in Playwright and a 300MB Chromium headless browser just to take a screenshot, while permanently burning 1,000+ tokens of schema definitions in every conversation turn.
2. **Cognitive Sprawl**: Dumping raw paragraph-length prose into node trees, producing unreadable walls of text that defeat the visual purpose of a mindmap.

**`mindmap-skills` solves this cleanly:**
* **Zero Daemon & Zero Token Tax**: 0 background processes, 0 permanent token overhead when idle.
* **Strict Cognitive Structuring**: Enforces single-root, 4–7 branches (Miller's Law), depth 3–4, and concise nodes (≤ 8 words) with keyword-first punchlines.
* **100% Official Markmap Syntax**: Supports `title` frontmatter, `colorFreezeLevel: 2`, `<!-- markmap: fold -->`, checkboxes, code blocks, and KaTeX math.
* **Zero-Dependency Rendering**: Emits portable `.mindmap.md` (native in Obsidian / VS Code) and instant standalone `.mindmap.html` via robust client-side template or offline CLI rendering.

---

## 📦 Quick Installation

### 1. Claude Code

#### Via Public Marketplace (Recommended):
In your Claude Code terminal session:
```text
/plugin marketplace add fioenix/mindmap-skills
/plugin install mindmap-skills@fioenix-plugins
```
Then invoke the skill directly:
```text
/mindmap-skills:markmap Tạo sơ đồ tư duy cho kiến trúc microservices này
```

#### On Claude Desktop / Web UI:
1. Open **Customize** → **Plugins** → **Add** → **Add marketplace** → **Add from a repository**.
2. Enter repository: `fioenix/mindmap-skills`.
3. In Discover, locate **mindmap-skills** and click **Add**.
4. Invoke in chat with `/markmap` or the `+` menu.

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

## 🛠️ Repository Architecture

```text
mindmap-skills/
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
    └── validate.sh             # Automated validation & test suite
```

---

## 📋 Cognitive Structuring & Markmap Syntax

Every generated mindmap adheres strictly to the official Markmap schema:

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

### Key Elements:
* `title`: Frontmatter root node. Main branches start directly at `##`.
* `colorFreezeLevel: 2`: Freezes branch colors at depth 2 (each `##` gets a consistent distinct color).
* `<!-- markmap: fold -->`: Automatically collapses dense or secondary sub-trees on load.
* `- [x]` / `- [ ]`: Interactive checklists.
* `$formula$`: Native math rendering via KaTeX.

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
