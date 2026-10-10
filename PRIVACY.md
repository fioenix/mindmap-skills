# Privacy Policy

`mindmap-skills` is engineered with an offline-first, decentralized posture that respects user privacy and data sovereignty:

## 1. Backend, Network Requests & Telemetry

- **Zero-Backend Architecture**: The skill and plugin operate with no backend servers, no analytics ingestion endpoints, and no telemetry services owned by maintainers.
- **Local & In-Agent Execution**: Concept extraction, cognitive structuring, and Markdown generation (`.mindmap.md`) occur strictly within the user's active AI agent runtime context (Claude Code, OpenAI Codex, Google Antigravity).
- **Rendering requests**: The alternative HTML template downloads pinned Markmap and D3 assets from jsDelivr, which receives ordinary network request metadata. Offline compilation uses Node.js/npx; first use may download pinned markmap-cli and dependencies from npm. The resulting `--offline` HTML embeds assets. Neither mode intentionally uploads document contents to maintainers.
- **Installer telemetry**: The third-party Skills CLI has separate install telemetry used by skills.sh. Set `DISABLE_TELEMETRY=1` to opt out, as shown in the README. Host agent processing follows its own policy.

## 2. Input Data Governance

- The skill processes only documents, notes, architecture briefs, or source code explicitly provided by the user in the prompt turn.
- **Sensitive Data Handling**: Users should never submit payment card data (PCI DSS), protected health information (PHI), passwords, private keys, API secrets, or confidential credentials. If such data is encountered, the skill terminates processing immediately and requests an anonymized prompt.

## 3. Host Platform Data Policies

- Prompt execution, context retention, and file storage are governed by the respective terms of service and privacy policies of your chosen AI agent host (Anthropic Claude, OpenAI Codex, Google Antigravity).
- The repository maintainers possess no access, insight, or control over host-level conversation logs or user workspaces.

## 4. Issue Reporting & Community Contributions

When reporting bugs or opening pull requests on GitHub, contributors must ensure that all test cases, prompt snippets, and diagrams are thoroughly anonymized and stripped of proprietary identifiers.

For privacy-related inquiries, open an issue on [GitHub Issues](https://github.com/fioenix/mindmap-skills/issues).
