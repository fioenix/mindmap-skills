# OpenAI Plugin and skills.sh Readiness

Reviewed 2026-10-10 against current primary sources. Local base: `main` at `7a2fdc0`, initially clean. This document describes an unpublished working-tree candidate for 0.1.3. Earlier dossier evidence is historical. Local checks do not establish portal acceptance, directory approval, native client behavior, or a skills.sh listing.

## Official requirements and checklist

| Item | Local result / evidence |
| --- | --- |
| Supported OpenAI manifest | `.codex-plugin/plugin.json` is a supported compatibility layout. Portable root migration is unnecessary. The legacy root `plugin.json` is excluded from the upload ZIP. |
| Skill discovery | `skills: "./skills/"`; `skills/markmap/SKILL.md` is an immediate child with `name` and `description` frontmatter. |
| Directory metadata | Display name 14 characters, subtitle 28, developer 7; description includes rendering limitations. Three example prompts fit 128 characters. Category `Productivity`, empty capabilities list. |
| Icons / presentation | Existing square 512×512 SVGs and light/dark assets retained. Owner reports the plugin icon is visible and accepts its appearance; client and installed version were not specified. This is presentation acceptance only. |
| Legal and support | MIT license, author, repository, privacy, terms and support URLs already present. Privacy now discloses CDN/npm requests and third-party installer telemetry. |
| Installable skill resources | Renderer and optional `agents/openai.yaml` now live inside the skill. All referenced resources resolve from its directory. No credentials or MCP required. |
| ZIP packaging | `scripts/package_plugin.py` uses an explicit file allowlist and one archive root; excludes caches, local configuration, compatibility catalogs, development dependencies and unsupported root descriptor. Refuses symlinks and overwriting existing files. Prints SHA-256. |
| npm packaging | Explicit `files` includes canonical Codex manifest, skill, scripts and this document; npm dry-run checked locally without running lifecycle scripts. npm publication is not required for skills.sh. Root `package.json` and `package-lock.json` declare no dependencies, so installers that run `npm install` on the plugin fetch nothing. The CI-only Claude CLI pin lives in the private `.github/ci/` package and is excluded from ZIP and npm contents. |
| Content safety | Template JSON payload escapes every `<`; titles must be HTML-escaped. Source HTML, links and images are stripped from displayed nodes. CSP restricts network destinations. CLI-generated HTML is a separate renderer; use trusted content. |
| Dependency handling | `markmap-cli@0.18.12` pinned in bundled renderer; first use can contact npm. CDN libraries already version-pinned. Host authorization controls command execution. |
| skills.sh discovery | Conventional `skills/markmap/SKILL.md` and README install command with `--skill markmap --agent codex`. A custom marketplace file does not register a skills.sh listing. |
| Approval/listing | Pending owner actions and platform review; no upload, submission, push, credentials, or telemetry-enabled install performed. |

Sources: [OpenAI packaging](https://developers.openai.com/plugins/build/plugins), [submission validation](https://developers.openai.com/plugins/deploy/submission-errors), [submission flow and field limits](https://developers.openai.com/plugins/deploy/submission), [skill resources](https://developers.openai.com/plugins/build/skills), [plugin guidelines](https://developers.openai.com/plugins/plugin-guidelines). Skills-only plugins are supported but may face additional directory eligibility review; usefulness and originality remain reviewer decisions.

Codex local discovery uses `.agents/skills` for projects and `~/.agents/skills` for users, as documented in [Build skills](https://learn.chatgpt.com/docs/build-skills). Optional UI metadata belongs in each skill's `agents/openai.yaml`.

[skills.sh FAQ](https://skills.sh/docs/faq) describes automatic listing through install telemetry. [CLI docs](https://skills.sh/docs/cli) document `DISABLE_TELEMETRY=1`; [CLI source documentation](https://github.com/vercel-labs/skills) documents `--list` and selective install options. These are separate distribution systems.

## Verification and limitations

- `bash tests/validate.sh`: all eight local gates passed, including strict Claude manifest validation and the new distribution regression checks.
- `python3 tests/distribution.py`: ZIP allowlist and integrity, root skill path, metadata lengths, extracted skill resources, Bash syntax, stubbed npx argument boundary, and HTML parser breakout checks passed. Uses temporary files; no network or install telemetry.
- `npm pack --dry-run --ignore-scripts --json --cache /tmp/mindmap-npm-cache`: package contents checked; no publish.
- Independent read-only code/security review completed: no blocking findings. Its missing-dossier-link finding was fixed by including this document in source, ZIP and npm package; follow-up confirmed resolution.
- Follow-up: official npm-cached Skills CLI 1.5.20 discovered exactly one skill and copied it into a temporary project with `DISABLE_TELEMETRY=1 DO_NOT_TRACK=1`. All four skill resource files matched the candidate ZIP byte for byte. An approved bounded official registry lookup confirmed the cached tarball URL and integrity.
- Cached markmap-cli 0.18.12 compiled an actual 337 KB offline smoke-test HTML file; its five script elements had no external script or stylesheet references. An update-check configuration warning did not fail compilation; no global configuration was changed.
- Native Codex 0.162.0 prompt assembly discovered the isolated project skill. After a narrow approved permission request, an ephemeral invocation with existing login, read-only child sandbox, ignored user configuration and disabled analytics read SKILL.md and returned four branches with valid Markmap frontmatter. No new credentials, trust grants, or global config edits were made.
- Browser automation rejected the local-file URL protocol and explicitly prohibited alternate-route workarounds. Native UI initially reported a locked Mac; the later supported inventory recheck succeeded and returned running native apps without a lock error. The local-file denial remains in force: it explicitly prohibits alternate browser surfaces, so native browser navigation to the same files was not attempted. That denial was honored. The owner subsequently reported successful generation/rendering but a theme/contrast defect (see below). Runtime sanitization/CSP behavior and portal ingestion remain unverified; parser and compilation checks do not establish end-to-end browser security.
- Direct retrieval of the expected skills.sh listing URL failed in the web tool; absence or presence of a live listing is unconfirmed. Real `skills@1.5.20 add . --list` was attempted with telemetry disabled and a temporary npm cache: offline mode returned `ENOTCACHED`, online mode returned `ENOTFOUND registry.npmjs.org`. These initial failures were resolved for local discovery through the official cached CLI and for package provenance through an approved bounded registry lookup; they were not treated as proof all routes were unavailable.
- Session inventory showed this task as the only active Codex task for the checkout. OS process inspection was blocked (`ps: operation not permitted`); other processes could not be independently ruled out. The supplied parent thread ID was not resolvable for a coordination message. No heavy workload was launched.

## Owner icon / presentation acceptance

The owner reported that the plugin icon is visible and its appearance is satisfactory. The report does not specify the client or installed version and does not establish mindmap rendering, runtime sanitization or CSP enforcement.

## Owner usage report and theme correction

The owner reported successful generation with the installed 0.1.3 CDN template, but a dark background with poor contrast in light mode. Read-only inspection of that output confirmed its stylesheet matched the pre-fix template. The owner's input and output stay private and are not part of this repository, package or ZIP.

Root cause: the template selected a dark canvas from OS `prefers-color-scheme`, which can disagree with the embedding client's theme, and tried to lighten SVG `text`. Pinned Markmap 0.18.12 actually renders HTML `foreignObject` labels with its own `--markmap-text-color: #333`; the template never synchronized Markmap's dark class or toolbar with the canvas. This diagnosis is supported by source inspection, not a browser screenshot.

The CDN template now defaults to light independently of OS/app settings. An accessible **Dark mode** toggle synchronizes the canvas, Markmap text/circle variables, toolbar, theme attribute and pressed state. Explicit initial dark requests use `data-theme="dark"`. Theme selection stays in memory; no storage, network destinations or permissions were added. The duplicate library dark toggle is excluded to keep one state owner. The bundled CLI renderer is unchanged: the reported output used the CDN template, and the CLI's own toolbar uses Markmap's native dark class.

`node tests/theme.cjs` passes offline checks for light defaults, explicit dark/invalid initial states, repeated toggling, CSS label/toolbar contracts, and at least 4.5:1 foreground contrast on declared canvas/panel/hover palettes. The test first failed against the old template. These are source/state checks, not browser CSS cascade, accessibility or visual validation. Both inline scripts pass `node --check`; all eight local validation gates pass with release metadata still 0.1.3. An independent read-only review of the template patch, including the pinned `markmap-toolbar@0.18.12` stylesheet cascade, found no text-contrast or theme-state blocker; the toolbar border keeps the library's neutral gray in dark mode, which is cosmetic.

**Owner visual acceptance:** the owner opened a single generated HTML demo built from the corrected template and accepted its light/dark toggle. This is owner presentation acceptance for theme behavior only. The agent did not open a browser, so no agent-side visual, zoom/fit, folding, runtime sanitization or CSP check exists. Prior ZIP/immutable risk snapshots predate this correction and must not be presented as covering it.

## Owner actions requiring approval

1. The owner approved preparing `0.1.3`; all source manifests and lockfile version fields now use 0.1.3. Existing public tags remain `v0.1.0`, `v0.1.1`, and `v0.1.2`. After the theme demo acceptance, the owner authorized committing and merging the reviewed source; that Git step is performed separately and is not recorded here as done. One genuine telemetry-enabled skills.sh install remains a separate owner-approved action that has not occurred. Tagging, releases, OpenAI ZIP upload/submission and presented terms are not approved by that conditional approval.
2. Build a fresh local ZIP: `python3 scripts/package_plugin.py /tmp/mindmap-skills-candidate.zip`. Keep its reported hash with the chosen source revision. Do not ZIP the whole checkout.
3. For OpenAI, approve uploading that exact ZIP to [Platform Plugins](https://platform.openai.com/plugins), select the owning organization/project and verified developer identity, resolve ingestion findings, and submit for review. Organization owner or Apps Management Write access is required. Complete identity verification and accept any presented terms as the owner. Approve publication separately after acceptance. No additional persistent access is needed for the skills-only package.
4. For skills.sh, publish the reviewed GitHub source only after the above conditions pass, then perform at most the one genuine telemetry-enabled install approved by the owner. The README's opt-out command installs without intentionally registering telemetry. Do not fabricate installs or rankings. Recheck the public skill page before claiming listing.
5. Remaining manual checks before claiming runtime security: the agent cannot initiate the blocked local-file route through another browser surface. Perform client smoke tests with a small non-sensitive input: direct and indirect mindmap requests should activate; a process flow should not; an ambiguous topic should ask for context; embedded script/HTML must not execute in template output. Confirm zoom, folding, light/dark appearance and offline output after compilation.
