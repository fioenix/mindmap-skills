# Privacy Policy

`mindmap-skills` is engineered with an offline-first, decentralized posture that respects user privacy and data sovereignty:

## 1. Zero Backend & No External Egress

- **Zero-Backend Architecture**: The skill and plugin operate with no backend servers, no analytics ingestion endpoints, and no telemetry services owned by maintainers.
- **Local & In-Agent Execution**: Concept extraction, cognitive structuring, and Markdown generation (`.mindmap.md`) occur strictly within the user's active AI agent runtime context (Claude Code, OpenAI Codex, Google Antigravity).
- **Zero-Dependency Rendering**: Standalone HTML mindmaps utilize pre-packaged static client templates, public open-source CDNs (Markmap / D3 via jsDelivr), or local offline compilation via `scripts/render.sh` without external network dependencies.

## 2. Input Data Governance

- The skill processes only documents, notes, architecture briefs, or source code explicitly provided by the user in the prompt turn.
- **Sensitive Data Handling**: Users should never submit payment card data (PCI DSS), protected health information (PHI), passwords, private keys, API secrets, or confidential credentials. If such data is encountered, the skill terminates processing immediately and requests an anonymized prompt.

## 3. Host Platform Data Policies

- Prompt execution, context retention, and file storage are governed by the respective terms of service and privacy policies of your chosen AI agent host (Anthropic Claude, OpenAI Codex, Google Antigravity).
- The repository maintainers possess no access, insight, or control over host-level conversation logs or user workspaces.

## 4. Issue Reporting & Community Contributions

When reporting bugs or opening pull requests on GitHub, contributors must ensure that all test cases, prompt snippets, and diagrams are thoroughly anonymized and stripped of proprietary identifiers.

For privacy-related inquiries, open an issue on [GitHub Issues](https://github.com/fioenix/mindmap-skills/issues).
