# 🧠 mindmap-skills

**Universal, lightweight Markmap mindmap plugin for AI Agents (Claude Code, Codex, Antigravity).**

Structured for full compliance with the plugin & marketplace standards of **Claude Code**, **Codex**, and **Antigravity**.

---

## ⚡ Why mindmap-skills?

Most AI mindmap solutions suffer from two fatal extremes:
1. **Bloated MCP Servers**: Running persistent background daemons, dragging in Playwright and a 300MB Chromium headless browser just to render an image, while permanently burning 1,000+ tokens of schema definitions in every conversation turn.
2. **Unstructured Output**: Dumping raw, paragraph-length text into node trees, producing illegible walls of text.

**`mindmap-skills` solves this cleanly:**
* **Zero Daemon & Zero Token Tax**: 0 background processes, 0 permanent token overhead when idle.
* **Strict Cognitive Structuring**: Enforces single-root, 4–7 branches (Miller's Law), depth 3–4, and concise nodes (≤ 8 words) with keyword-first punchlines.
* **100% Official Markmap Syntax**: Supports `title` frontmatter, `colorFreezeLevel: 2`, `<!-- markmap: fold -->`, checkboxes, code blocks, and KaTeX math.
* **Zero-Dependency Rendering**: Emits portable `.mindmap.md` (native in Obsidian / VS Code) and instant standalone `.mindmap.html` via client-side Markmap Autoloader.

---

## 📦 Canonical Installation

### 1. Google Antigravity

#### Machine-Global (Available across all projects):
Symlink or copy into your global customization root:
```bash
# Clone the repository
git clone https://github.com/fioenix/mindmap-skills.git ~/Projects/mindmap-skills

# Symlink to global skills
mkdir -p ~/.gemini/config/skills
ln -s ~/Projects/mindmap-skills/skills/markmap ~/.gemini/config/skills/markmap
```

#### Workspace-Local (Project-scoped):
Place in `.agents/skills` or `.agents/plugins` at the root of your project:
```bash
mkdir -p .agents/skills
cp -r ~/Projects/mindmap-skills/skills/markmap .agents/skills/
```

---

### 2. Claude Code

Install via the Skills CLI or register as a local plugin:

```bash
# Via Skills CLI
npx skills add fioenix/mindmap-skills

# Or register local path
claude plugin add ~/Projects/mindmap-skills
```

---

### 3. OpenAI Codex

Codex automatically discovers skills placed in `.agents/skills/` or `.codex/plugins/`:

```bash
mkdir -p ~/.agents/skills
ln -s ~/Projects/mindmap-skills/skills/markmap ~/.agents/skills/markmap
```

---

## 🛠️ Repository Layout

```text
mindmap-skills/
├── .claude-plugin/
│   └── plugin.json             # Claude Code plugin manifest (with icon, tags, category)
├── .codex/
│   └── plugin.json             # Codex plugin manifest
├── plugin.json                 # Antigravity plugin manifest
├── package.json                # npm / skills.sh package descriptor
├── assets/
│   ├── icon.svg                # Vector SVG icon
│   └── icon.png                # 512x512 PNG marketplace icon
├── logo.svg                    # Root vector logo
├── LICENSE                     # MIT License
├── README.md                   # Documentation & installation guide
├── skills/
│   └── markmap/
│       ├── SKILL.md            # Canonical skill instructions & prompt constraints
│       └── assets/
│           └── template.html   # Standalone HTML artifact template (CSP hardened)
├── scripts/
│   └── render.sh               # Hardened CLI helper (markmap-cli wrapper)
└── tests/
    └── validate.sh             # Automated validation & test suite
```

---

## 🔒 Security Posture & Guardrails

* **Zero-Privilege Execution**: By default, no subshell, process spawning, or CLI is executed. The agent emits pure Markdown and client-side HTML.
* **XSS & Parser Breakout Protection**: The template enforces Content Security Policy (CSP) headers and documents strict escaping of `</script` as `<\/script` to prevent premature script termination and DOM injection.
* **CLI Option Injection Guard**: `scripts/render.sh` terminates argument parsing with `--` (`markmap-cli -- "$INPUT"`) to prevent malicious filenames from triggering CLI flags.

---

## 📋 Official Markmap Syntax Reference

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

## 📄 License

MIT © [Fioenix](https://github.com/fioenix)
