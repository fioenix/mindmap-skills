---
name: markmap
description: Generate interactive Markmap mindmaps from notes, architecture docs, codebases, or topics. Enforces strict markmap syntax (title frontmatter, colorFreezeLevel: 2, 4-7 branches, brevity <= 8 words, rich syntax support) and outputs clean .mindmap.md plus zero-dependency standalone HTML artifacts via markmap-autoloader.
---

# Markmap Mindmap Skill

Use this skill when asked to create a mindmap, visualize a concept hierarchy, synthesize an architecture, or map complex information into an interactive Markmap tree.

---

## 1. Official Frontmatter Standard

Every generated mindmap MUST start with the official Markmap frontmatter:

```markdown
---
title: <Map Title>
markmap:
  colorFreezeLevel: 2
---
```

* **`title`**: Serves as the root / central theme of the mindmap.
* **`colorFreezeLevel: 2`**: Freezes branch colors at depth 2 (each `##` main branch gets a distinct, consistent color for all its descendants).
* *Note*: When `title` is defined in frontmatter, main branches start directly with `## Branch Name` (no need for a redundant `# H1`).

---

## 2. Core Structuring Rules (The Value Layer)

A mindmap is a **cognitive navigation index**, not a document. Mindmap quality depends 90% on structure and brevity:

1. **4–7 Main branches (`##`)**: Strictly respect cognitive working memory (Miller's Law). Group related concepts instead of dumping 10+ top-level branches.
2. **Depth target: 3–4 levels**: Use `###` or nested `- ` bullet points.
3. **Brevity constraint (≤ 8 words per node)**:
   - Punchline and keyword first.
   - Strip filler words, full sentences, and narrative prose.
   - ❌ Bad: `- The system handles user authentication by using JWT tokens signed by RSA keys`
   - ✅ Good: `- Auth: JWT with RSA signatures`
4. **Rich Markmap Syntax Support**:
   - **Inline styling**: `**strong**`, `*italic*`, `~~strike~~`, `==highlight==`, `` `code` ``
   - **Checkboxes**: `- [ ] Pending item` or `- [x] Completed task`
   - **Magic folding**: Append `<!-- markmap: fold -->` to collapse dense or secondary branches on initial load:
     ```markdown
     ### Deep Details <!-- markmap: fold -->
     - Sub-item 1
     - Sub-item 2
     ```
   - **Math / KaTeX**: `$x = {-b \pm \sqrt{b^2-4ac} \over 2a}$`
   - **Code & mini-tables**: Inline codeblocks or small markdown tables where structured data adds clarity.

---

## 3. Deliverables & Output Protocol

Always produce deliverables to files or artifacts — never leave raw mindmap code only in chat:

### Deliverable A: Pure Markdown (`<name>.mindmap.md`)
Save directly to the target project directory or Obsidian vault.
* Native compatibility: Viewable directly in Obsidian (with Markmap plugin) or VS Code.
* Zero lock-in, version-controllable text.

### Deliverable B: Standalone Interactive HTML (`<name>.mindmap.html` or Chat Artifact)
When an interactive visual is requested, generate a self-contained HTML file using the **Markmap Autoloader** pattern (zero Node.js/CLI/Playwright dependencies):

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{{TITLE}}</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    html, body {
      width: 100%;
      height: 100%;
      overflow: hidden;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }
    #mindmap-container { width: 100vw; height: 100vh; position: relative; }
    .markmap { width: 100%; height: 100%; }
    .markmap > svg { width: 100%; height: 100%; display: block; }
    .mm-toolbar { position: absolute; bottom: 24px; right: 24px; }
  </style>
  <script>
    window.markmap = { autoLoader: { toolbar: true } };
  </script>
  <script src="https://cdn.jsdelivr.net/npm/markmap-autoloader"></script>
</head>
<body>
  <div id="mindmap-container" class="markmap">
    <script type="text/template">
{{MARKDOWN_CONTENT}}
    </script>
  </div>
</body>
</html>
```

* Features built-in: Interactive zoom, pan, node collapse/expand, fit to view, and export to SVG/PNG directly in the client's browser.
* Template source is located at `assets/template.html` relative to this skill.
* **Security Guardrail**: When generating HTML, replace any literal `</script` in the markdown with `<\/script` to prevent HTML parser breakout (XSS/DOM injection).

---

## 4. Worked Example

### Raw Input:
> "We need an architecture overview for Finolabs Agent Gateway. It has an API Gateway running on Cloudflare Workers handling JWT auth, rate limiting, and request routing. The storage layer uses KV for sessions, D1 for transactional data, and R2 for large media assets. The Agent Harness coordinates subagents using durable workflows, queue-based retry, and streaming responses back over SSE. Observability is handled via OpenTelemetry traces and Cloudflare Analytics Engine."

### Output (`finolabs-agent-gateway.mindmap.md`):

```markdown
---
title: Finolabs Agent Gateway
markmap:
  colorFreezeLevel: 2
---

## Edge Gateway (CF Workers)
- **Security**: JWT verification
- **Protection**: IP & token rate limiting
- **Routing**: Dynamic endpoint dispatch

## Storage Layer
- **KV**: Session cache & token blacklist
- **D1**: Transactional SQLite metadata
- **R2**: Large media & artifact blob store

## Agent Harness
- **Coordination**: Durable workflows
- **Resilience**: Cloudflare Queues with retry
- **Streaming**: Server-Sent Events (SSE)

## Observability <!-- markmap: fold -->
- **Tracing**: OpenTelemetry exports
- **Metrics**: Cloudflare Analytics Engine
- **Audit**: Immutable execution logs
```
