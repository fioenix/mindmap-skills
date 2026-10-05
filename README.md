<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/icon-dark.svg">
    <img src="assets/icon.svg" width="96" height="96" alt="mindmap-skills icon">
  </picture>
</p>

<h1 align="center">mindmap-skills</h1>

<p align="center">
  <b>Universal, lightweight Markmap mindmap plugin for AI Agents (Claude Code, OpenAI Codex, Google Antigravity).</b><br>
  Cognitive structuring with Miller's Law & MECE · 0 daemon · 0 token tax · Standalone HTML rendering.
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

Most AI mindmap solutions suffer from two fatal architectural pitfalls:
1. **Bloated MCP Servers & Idle Token Tax**: Running persistent background server processes, dragging in Playwright and a 300MB Chromium headless browser just to take a screenshot, while permanently burning 1,000+ tokens of schema definitions in every conversation turn.
2. **Cognitive Sprawl**: Dumping raw paragraph-length prose into node trees, producing unreadable walls of text that defeat the visual purpose of a mindmap.

### Architecture Comparison

| Capability | Heavyweight MCP / Headless | Raw LLM Output | **mindmap-skills** |
|---|---|---|---|
| **Runtime Footprint** | 300MB+ Headless Chrome daemon | 0 MB | **0 MB (Zero daemon)** |
| **Idle Token Tax** | 1,000+ tokens burned per turn | 0 tokens | **0 token overhead when idle** |
| **Cognitive Structuring** | None (unfiltered text dump) | Unstructured | **Miller's Law (4–7 branches, depth 3–4, ≤ 8 words)** |
| **Output Artifacts** | Static raster image (PNG) | Raw text | **Portable `.mindmap.md` + Standalone `.html`** |
| **Multi-Agent Parity** | Platform-specific | Inconsistent | **Claude Code · OpenAI Codex · Google Antigravity** |
| **Security Posture** | Subprocess execution risk | Safe | **Zero-privilege core + CSP-hardened template** |

---

## 🔍 Before vs. After Comparison

| Scenario | Default LLM Output (Before) | Structured with `mindmap-skills` (After) |
|---|---|---|
| **Gateway Architecture** | `- The system uses an API Gateway running on Cloudflare Workers to handle user requests, authenticating users via JWT tokens signed with RSA encryption...` (32 words, verbose narrative) | `- **Auth**: JWT with RSA signatures`<br>`- **Rate Limit**: Token bucket at edge`<br>`- ~~Kong Gateway: Excessive idle cost~~` (Concise, keyword-first, tracks rejected alternatives) |
| **Branch Structure** | Dumps 14 flat sibling bullet points on the root, exceeding human working memory capacity. | Clusters into 4 MECE categories (Ingress, Compute, Storage, Telemetry); deep specs fold automatically with `<!-- markmap: fold -->`. |
| **Decision Tracking** | Static descriptive text with no sense of milestone completion or pending trade-offs. | `- [x] State snapshot serialization`<br>`- [ ] WebSocket reconnection backoff`<br>`+ Low latency / - Stale read risk` |

---

## 📦 Quick Installation

### 1. Claude Code

#### Via Public Marketplace (Recommended):
In your Claude Code terminal session:
```text
/plugin marketplace add fioenix/mindmap-skills
/plugin install mindmap-skills@fioenix-plugins
```
Invoke the skill directly in any conversation:
```text
/mindmap-skills:markmap Create an architecture mindmap for this microservices system
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

#### Via Skills CLI:
```bash
npx --yes skills@1.5.20 add fioenix/mindmap-skills --global
```

#### Via Workspace Catalog or Agent Skills Directory:
```bash
# In a specific project
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

## 📋 Cognitive Structuring Invariants

Every generated mindmap adheres strictly to official Markmap standards and information architecture principles:

* **Miller's Law (4–7 Main Branches `##`)**: Limits top-level branches to match human working memory capacity. Always cluster related concepts into umbrella categories rather than dumping flat lists.
* **MECE Taxonomy (Mutually Exclusive, Collectively Exhaustive)**: Sibling branches at the same depth share a single logical classification axis (e.g. system layers, data lifecycle stages, or user personas) without semantic overlap.
* **Branch Density Equilibrium**: Automatically partitions lop-sided branches (> 7 children) into intermediate sub-groups (`###`) to maintain visual balance.
* **Progressive Disclosure (`<!-- markmap: fold -->`)**: High-level branches (Tiers 1–2) remain open for 5-second scanning, while deep implementation nodes (depth ≥ 3) or dense technical parameters fold by default to prevent visual fatigue.
* **Decision & Status Encoding**:
  - `- [x]` Completed / Confirmed milestone
  - `- [ ]` Open Question / Pending decision
  - `~~Discarded Alternative~~`: Documents why an option was rejected
  - `==Critical Path / Bottleneck==`: Highlights focal architectural risks
  - `+ Advantage / - Cost Dyads`: Explicitly states who pays the trade-off

```markdown
---
title: Finolabs Agent Gateway Architecture
markmap:
  colorFreezeLevel: 2
---

## Ingress Gateway (MECE: Ingress)
- **Runtime**: Cloudflare Workers
- **Security**: JWT with RSA signatures
- ~~Alternative: Self-hosted Kong (High idle cost)~~

## Storage Tier (MECE: Persistence)
- **Metadata**: Cloudflare D1 (SQLite)
  - `+ Low latency, zero cold starts`
  - `- Single-writer concurrency ceiling`
- **Blobs**: Cloudflare R2 object store
- ~~Alternative: AWS S3 (High egress fees)~~

## Telemetry (MECE: Observability) <!-- markmap: fold -->
- **Traces**: OpenTelemetry collector
- **Metrics**: Cloudflare Analytics Engine
- **Pending Tasks**:
  - - [ ] Benchmark 5% trace sampling rate
  - - [x] Enable tail-based sampling
```

---

## 🔄 Opportunistic Multi-Skill Synergy

`mindmap-skills` is built on a **Zero-Coercion, Zero-Hard-Dependency** model: it works 100% standalone out of the box. However, when paired with complementary skills inside an agent harness, it acts as a high-value **Visual Converger**:

| Skill in Harness | Upstream Role | `markmap` Downstream Role |
|---|---|---|
| **`grilling`** | Stress-tests ideas, exposes hidden assumptions, challenges trade-offs. | **Visual Decision Tree**: Synthesizes grilled decisions, struck-out options (`~~...~~`), and confirmed invariants. |
| **`brainstorming`** | Divergent thinking, exploratory ideation, sprawling idea generation. | **Convergent Affinity Map**: Gathers unstructured ideas into 4–7 MECE categories with actionable checkboxes. |
| **Spec Kit (`.specify/`)** | Defines formal functional specifications (`spec.md`). | **Functional Decomposition**: Visually maps user stories, data entities, and acceptance criteria. |

### Practical Synergy Scenarios:

#### Scenario 1: Paired with `grilling`
> **User Prompt:** *"Use grilling to stress-test this architecture proposal, then synthesize the decisions into a mindmap."*
> 
> **Agent Execution:**
> 1. Runs `grilling` to probe boundary conditions, unearth trade-offs, and challenge assumptions.
> 2. Finalizes core architectural agreements.
> 3. Handoff to `markmap` to emit `.mindmap.md`: highlighting confirmed paths, crossing out discarded alternatives (`~~...~~`), and flagging remaining open loops (`- [ ]`).

#### Scenario 2: Paired with `brainstorming`
> **User Prompt:** *"Brainstorm 10 growth features for this product, then organize them into a clean mindmap."*
> 
> **Agent Execution:**
> 1. Runs `brainstorming` for divergent ideation.
> 2. Invokes `markmap` to converge ideas into 4–7 MECE clusters (e.g. Acquisition, Activation, Retention, Monetization).
> 3. Applies `<!-- markmap: fold -->` to secondary branches and emits an interactive HTML artifact.

#### Scenario 3: Standalone Execution
> When auxiliary skills are absent from the harness, `markmap` processes user requests directly, **never prompting or nagging the user to install additional packages**.

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
* **CLI Option Injection Guard**: `scripts/render.sh` terminates argument parsing with `--` (`markmap-cli --offline -o "$OUTPUT" --no-open -- "$INPUT"`) to prevent untrusted input from triggering CLI flags.
* **Sensitive Data Policy**: See [PRIVACY.md](PRIVACY.md) and [TERMS.md](TERMS.md).

---

## 📄 License & Community

* **License**: [MIT License](LICENSE) © [Fioenix](https://github.com/fioenix)
* **Contributing**: Read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting pull requests.
* **Issues & Feedback**: [GitHub Issues](https://github.com/fioenix/mindmap-skills/issues)
