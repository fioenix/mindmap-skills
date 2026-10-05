---
name: markmap
description: Generate interactive Markmap mindmaps from notes, architecture docs, codebases, or topics. Enforces strict cognitive structuring (MECE, Miller's Law 4–7 branches, depth 3–4, brevity <= 8 words, progressive disclosure, decision encoding) and outputs clean .mindmap.md plus zero-dependency standalone HTML artifacts.
---

# Markmap Mindmap Skill

Use this skill to convert notes, architecture specifications, brainstorming sessions, or complex topics into an interactive, visually structured Markmap mindmap tree.

---

## 1. Scope & Activation Boundaries

### When to Trigger:
- User asks for a "mindmap", "concept hierarchy", "mental model", "knowledge tree", or visual taxonomy.
- Synthesizing broad architecture components or system designs into clean high-level branches.
- Deconstructing research documents, book notes, or strategy documents into hierarchical clusters.
- Acting as a **Visual Converger** after a brainstorming or grilling session.

### When NOT to Trigger:
- **Sequential workflows / Process flows**: Use Mermaid `flowchart` or `sequenceDiagram` instead.
- **Quantitative data / Statistical tables**: Use Markdown tables or data charts instead.
- **Relational data models**: Use Entity-Relationship Diagrams (ERD) or SQL schemas instead.

### Clarification Conditions (When to Ask):
- Input is an isolated phrase or title without sufficient context to synthesize 4–7 meaningful branches.
- Input contains multiple completely divergent domains without an explicit central root topic.

### Stop Condition:
- Stop once the `.mindmap.md` file and corresponding standalone `.mindmap.html` (or chat artifact) are generated and delivered. Summarize the branch hierarchy concisely in the response.

---

## 2. Official Frontmatter Standard

Every generated mindmap MUST start with the official Markmap frontmatter:

```markdown
---
title: <Map Title>
markmap:
  colorFreezeLevel: 2
---
```

* **`title`**: Serves as the central root node.
* **`colorFreezeLevel: 2`**: Freezes branch colors at depth 2 (each `##` main branch gets a distinct, consistent color for all its descendants).
* *Rule*: When `title` is defined in frontmatter, main branches start directly with `## Branch Name` (no redundant `# H1`).

---

## 3. Cognitive Structuring Rules (The Value Layer)

A mindmap is a **cognitive navigation index**, not a narrative essay. Mindmap utility is defined by strict adherence to human cognitive bandwidth and information architecture:

1. **4–7 Main branches (`##`)**: Strictly observe Miller's Law (cognitive working memory limit). Group related concepts under umbrella categories rather than dumping 10+ top-level nodes.
2. **MECE Categorization (Mutually Exclusive, Collectively Exhaustive)**:
   - Sibling branches at the same depth must share a single logical classification axis (e.g., system layers, data lifecycle stages, or user personas) without semantic overlap.
   - Never mix functional components with non-functional traits on the same tier (e.g., don't place "Security" as a peer to "Frontend" if Frontend has its own security).
3. **Depth target: 3–4 levels**: Use `###` or nested `- ` bullet points. Avoid flat trees (depth 1) or unwieldy sprawl (depth > 5).
4. **Branch Density Equilibrium**:
   - Maintain visual balance across branches.
   - If any branch exceeds 7 direct child nodes, partition them into 2 or more intermediate sub-categories (`###`) rather than creating a lop-sided cluster.
5. **Brevity constraint (≤ 8 words per node)**:
   - Keyword and punchline first.
   - Strip filler phrases, auxiliary verbs, and narrative prose.
   - ❌ Bad: `- The system handles user authentication by using JWT tokens signed by RSA keys`
   - ✅ Good: `- **Auth**: JWT with RSA signatures`
6. **Progressive Disclosure (`<!-- markmap: fold -->`)**:
   - Root node and primary branches (Tiers 1–2) remain **open by default** for rapid scanning.
   - Deep branches (Tier 3+) or sections containing dense technical specifications, edge cases, or implementation appendices **MUST append `<!-- markmap: fold -->`**.
   - Allows users to drill down on demand without visual fatigue.
7. **Decision & Status Encoding**:
   - **Actionability**: `- [x] Completed / Confirmed` vs `- [ ] Open Question / Pending`.
   - **Key Bottlenecks**: `==Critical Path / Bottleneck==`.
   - **Discarded Alternatives**: `~~Rejected Option: reason~~` (documents historical decision boundaries).
   - **Trade-off Dyads**: `+ Gain / - Cost/Trade-off` (who pays the price).
8. **Rich Syntax Support**:
   - Math / KaTeX: `$x = {-b \pm \sqrt{b^2-4ac} \over 2a}$`.
   - Compact mini-tables and code blocks where structured representation adds clarity.

---

## 4. Opportunistic Skill Synergy (Harness Coordination)

When other complementary skills are present in the active agent harness, coordinate with them organically as a **Visual Converger**. When absent, execute stand-alone with zero friction.

### Coordination Matrix:

| Active Skill in Harness | Upstream Role | `markmap` Downstream Role |
|---|---|---|
| **`grilling`** | Stress-tests half-formed ideas, surfaces hidden assumptions, challenges trade-offs. | **Visual Decision & Risk Tree**: Harvests confirmed decisions, struck-out alternatives (`~~Option~~`), invariants, and open questions (`- [ ]`). |
| **`brainstorming`** | Divergent ideation, creative exploration, sprawling idea lists. | **Convergent Affinity Map**: Gathers sprawling ideas into 4–7 MECE clusters, assigns status checkmarks, and folds detail nodes. |
| **Spec Kit (`.specify/`)** | Defines formal functional specifications (`spec.md`). | **Functional Decomposition Tree**: Maps user stories, entity hierarchies, and acceptance scenarios visually. |

### The Zero-Coercion Rule:
- **Inspect Dynamically**: Check if `grilling` or `brainstorming` exist in active tools/skills.
- **Never Prompt to Install**: If auxiliary skills are NOT in the harness, **never** complain, ask the user to install them, or halt execution. Execute directly and completely using standard user prompts.

---

## 5. Deliverables & Output Protocol

Always produce deliverables to files or artifacts — never leave raw mindmap code only in chat:

### Deliverable A: Pure Markdown (`<name>.mindmap.md`)
Save directly to the target project directory or Obsidian vault.
* Native compatibility: Viewable directly in Obsidian (with Markmap plugin) or VS Code.
* Zero lock-in, version-controllable text.

### Deliverable B: Standalone Interactive HTML (`<name>.mindmap.html` or Chat Artifact)

There are two primary ways to produce interactive HTML deliverables:

#### Method 1: Local Standalone Offline HTML (Recommended for Local Files)
Run the bundled render script to compile directly using `markmap-cli --offline`:
```bash
./scripts/render.sh <path/to/mindmap.md> [path/to/output.html]
```
* **Offline Ready**: All JS and CSS are inlined (zero external CDN requests, works 100% offline).
* **Cross-Browser & Local File Safe**: Bypasses browser `file:///` CORS restrictions (e.g. Safari Local File Restrictions).

#### Method 2: Zero-Dependency HTML Artifact / Template (Direct File Generation)
When generating HTML directly without executing CLI commands, use the robust static CDN pattern (`assets/template.html`):

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="Content-Security-Policy" content="default-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net; img-src 'self' data: https:; font-src 'self' https://cdn.jsdelivr.net; style-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net;">
  <title>{{TITLE}}</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    html, body {
      width: 100%; height: 100%; overflow: hidden;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      background: #ffffff;
    }
    #mindmap { width: 100vw; height: 100vh; display: block; }
    @media (prefers-color-scheme: dark) {
      html, body { background: #18181b; color: #f4f4f5; }
      #mindmap text { fill: #f4f4f5; }
    }
    .mm-toolbar { position: absolute; bottom: 24px; right: 24px; }
  </style>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/markmap-toolbar@0.18.12/dist/style.css">
  <script src="https://cdn.jsdelivr.net/npm/d3@7.9.0/dist/d3.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/markmap-view@0.18.12/dist/browser/index.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/markmap-lib@0.18.12/dist/browser/index.iife.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/markmap-toolbar@0.18.12/dist/index.js"></script>
</head>
<body>
  <svg id="mindmap"></svg>
  <script type="text/template" id="markdown-source">
{{MARKDOWN_CONTENT}}
  </script>
  <script>
    window.addEventListener("DOMContentLoaded", () => {
      try {
        const mdEl = document.getElementById("markdown-source");
        const md = mdEl.textContent.trim();
        const { Transformer, Markmap, Toolbar } = window.markmap;
        const transformer = new Transformer();
        const { root, frontmatter } = transformer.transform(md);
        const options = markmap.deriveOptions(frontmatter?.markmap);
        const mm = Markmap.create("#mindmap", options, root);
        if (Toolbar) {
          const toolbar = new Toolbar();
          toolbar.attach(mm);
          const el = toolbar.render();
          el.setAttribute("style", "position:absolute;bottom:20px;right:20px");
          document.body.append(el);
        }
        mm.fit();
      } catch (err) {
        console.error("Markmap render failed:", err);
      }
    });
  </script>
</body>
</html>
```

---

## 6. Dependency Contract & Graceful Fallback

- **Core Capability (Zero-Dependency)**: Markdown generation (`.mindmap.md`) and static HTML templating (`assets/template.html`) require **zero** external CLI tools or npm packages.
- **Auxiliary Tooling (`scripts/render.sh`)**: Relies on `npx` or a global `markmap-cli` installation.
- **Graceful Fallback**: If `markmap-cli` is not available in the environment, fallback transparently to Method 2 (Template HTML artifact) without failing the task or hallucinating execution outputs.

---

## 7. Security Posture & Privacy Guardrails

- **Zero-Network Egress**: The skill does not transmit document contents to external servers or telemetry collectors.
- **DOM & Script Injection Guard**: When generating HTML artifacts, escape literal `</script` occurrences within the Markdown content as `<\/script` to prevent HTML parser breakout.
- **Sensitive Data Handling**: If user input contains payment card data (PCI DSS), protected health information (PHI), authentication tokens, or private credentials, halt processing immediately and request an anonymized draft.

---

## 8. Worked Example (Cognitive & Decision Synthesis)

### Raw Input:
> "We just finished a grilling session on Finolabs Agent Gateway architecture. We decided on Cloudflare Workers at the edge with RSA JWT auth. We rejected self-hosted Kong because idle infrastructure costs are too high. For storage, we use D1 for transactions and R2 for blobs, while Postgres on AWS was discarded due to egress cost. Durable Objects coordinate agents, but WebSocket reconnection retry logic is still pending review. OpenTelemetry exports traces to Cloudflare Analytics."

### Output (`finolabs-agent-gateway.mindmap.md`):

```markdown
---
title: Finolabs Agent Gateway Architecture
markmap:
  colorFreezeLevel: 2
---

## Edge Gateway (MECE: Ingress)
- **Runtime**: Cloudflare Workers at edge
- **Security**: JWT with RSA signatures
- ~~Alternative: Self-hosted Kong (High idle cost)~~

## Storage Tier (MECE: Persistence)
- **Metadata**: Cloudflare D1 (SQLite)
  - `+ Low latency, zero cold starts`
  - `- Single-writer concurrency ceiling`
- **Blobs**: Cloudflare R2 object store
- ~~Alternative: AWS RDS Postgres (Egress cost)~~

## Agent Harness (MECE: Coordination)
- **Engine**: Cloudflare Durable Objects
- **Streaming**: Server-Sent Events (SSE)
- **Pending Tasks**: <!-- markmap: fold -->
  - - [ ] WebSocket reconnection backoff
  - - [ ] Durable queue DLQ threshold
  - - [x] State snapshot serialization

## Observability (MECE: Telemetry) <!-- markmap: fold -->
- **Traces**: OpenTelemetry collector export
- **Metrics**: Cloudflare Analytics Engine
- **Audit**: Immutable append-only hash chain
```
