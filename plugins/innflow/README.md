# Innflow for Codex and Grok Build

One plugin for inspecting workflows, diagnosing failed executions, running authorized automations, and creating drafts when Innflow authoring is enabled.

## Install from this checkout

Requires a Codex client supporting plugins and an Innflow account.

From the repository root:

```sh
codex plugin marketplace add .
codex plugin add innflow@innflow-plugins
```

Restart or open a new Codex session, enable the Innflow plugin, and complete the Innflow OAuth connection when prompted. In clients without CLI installation, select the Innflow marketplace in the Plugins directory and install Innflow there. The MCP endpoint is `https://mcp.innflow.ai/mcp`; credentials are managed by the client, not bundled in this package.

Try “Find my Innflow workflows” or “Investigate the latest failed run of my workflow.” For creation, try “Create a draft that receives a webhook and summarizes its text.”

## Capabilities and permissions

The connected MCP server determines which tools are available. Read tools require `mcp:read`, execution requires `mcp:execute`, and management requires `mcp:manage`. Existing account and workspace permissions still apply.

Draft creation, node discovery, graph editing, and validation require the authoring preview on both Innflow services. Installation does not enable that preview. If those tools are unavailable, the skill provides an editor implementation plan and reports that nothing was saved.

The package contains one skill, one remote MCP connection, and a brand icon. It installs no lifecycle hooks, dependencies, local server, or embedded credentials.

## Package for team distribution

Run from the standalone plugin repository root:

```sh
python3 scripts/package-innflow-plugin.py --output /tmp/innflow-plugin-0.1.1.zip
```

Extract the archive into a new directory, then run `codex plugin marketplace add /path/to/extracted-directory` and `codex plugin add innflow@innflow-plugins`. The archive includes only the plugin and its marketplace catalog, not the application repository.

## Release verification

Before advertising a public release, authenticate in a fresh Codex session and check workflow discovery and a real execution inspection. If advertising authoring, create and validate a disposable draft in a workspace with that capability enabled. Run/deploy checks need an explicitly chosen test workflow with understood side effects.

Public directory publication additionally requires submission and review through OpenAI; a local marketplace install is not a directory listing. See [plugin packaging](https://developers.openai.com/plugins/build/plugins) and [public submission](https://developers.openai.com/plugins/deploy/submission).

## Grok Build compatibility

`.grok-plugin/plugin.json` and `.mcp.json` expose the same skill and remote MCP
connection to Grok Build. The plugin directory is `plugins/innflow` in the source
repository. It contains no agents, hooks, shell commands, or local dependencies.

## License

Plugin files are licensed under Apache-2.0; see [LICENSE](LICENSE). This does not
license the hosted Innflow service or the separate application source.
