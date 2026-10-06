# Innflow for Codex

Connect Codex to your Innflow workspace to inspect workflows, diagnose failed runs, execute authorized automations, and create workflow drafts when authoring is available.

This is the standalone source repository for the Innflow Codex plugin. It contains the plugin, its workflow skill, a remote MCP connection, and the installable marketplace catalog.

## Install

Requires an Innflow account and a Codex client that supports plugins.

```sh
codex plugin marketplace add innflow-ai/innflow-codex-plugin
codex plugin add innflow@innflow-plugins
```

Start a new Codex session, enable Innflow, and complete the Innflow OAuth connection when prompted. Credentials are managed by the client and are not included in this repository.

Try:

- “Find my Innflow workflows and show their deployment status.”
- “Investigate the latest failed run of my workflow.”
- “Create an Innflow workflow draft from this automation idea.”

Draft authoring depends on the tools enabled for your workspace. See the [plugin documentation](plugins/innflow/README.md) for capabilities, permissions, and release checks.

## Repository layout

```text
.agents/plugins/marketplace.json           Marketplace catalog
plugins/innflow/plugin.json                Plugin manifest and directory metadata
plugins/innflow/mcp.json                   Remote MCP connection
plugins/innflow/skills/innflow-workflows/   Workflow skill
plugins/innflow/assets/icon.png            Innflow icon
scripts/package-innflow-plugin.py          Distribution archive builder
```

The plugin connects to `https://mcp.innflow.ai/mcp`. It installs no local server, lifecycle hooks, or runtime dependencies.

## Build a distribution archive

From the repository root, using Python 3:

```sh
python3 scripts/package-innflow-plugin.py --output dist/innflow-plugin-0.1.0.zip
```

The packager includes only the explicitly listed plugin files and marketplace catalog.

## Submission details

- Repository: https://github.com/innflow-ai/innflow-codex-plugin
- Plugin directory: `plugins/innflow`
- Manifest: `plugins/innflow/plugin.json`
- Marketplace: `.agents/plugins/marketplace.json`
- Plugin version: `0.1.0`
- Website: https://innflow.ai

This repository provides the installable plugin source. An OpenAI directory listing requires a separate submission and review.
