# Directory submission preparation

Source: https://github.com/innflow-ai/innflow-codex-plugin
Plugin directory: `plugins/innflow`. Version: `0.1.1`. License: Apache-2.0.

## Grok Build

Submit a remote catalog entry to https://github.com/xai-org/plugin-marketplace,
using this repository URL, `path: "plugins/innflow"`, and a full public commit SHA.
The Grok manifest and HTTP MCP configuration use the same skill and server as
Codex. Regenerate the index and run the upstream catalog checks before submission.
A pull request is a submission, not an approved marketplace listing.

## OpenAI / ChatGPT / Codex

Upload `dist/innflow-openai-0.1.1.zip` at https://platform.openai.com/plugins.
The ZIP has one portable Agent Plugins root with its manifest, MCP configuration,
skill, README, icon, and license. Do not upload the team marketplace ZIP instead.

The listing metadata includes the website, support, privacy and terms URLs. They
returned HTTP 200 during preparation. The MCP endpoint returned HTTP 401 without
authentication, as expected; this does not prove authenticated tool functionality.

Still required before OpenAI review submission:

- Access to the owning OpenAI organization/project and its verified developer identity.
- The portal's domain-verification challenge, published exactly as instructed.
- MCP connection and successful OAuth/tool scans in the portal.
- A dedicated reviewer account with sample workflows/executions, plus sign-in
  instructions entered privately in the portal. Never commit reviewer credentials.
- Run the five positive and three negative cases below with that test account.
- A public walkthrough video demonstrating the cases, with its URL in review details.
- Review and resolve the portal's automated package/skill/MCP findings.

Browser access to the portal timed out during preparation; no OpenAI submission
or approval is claimed. The cases below are a proposed review plan, not run results.

### Positive review cases (to run)

| Prompt | Expected tools | Expected behavior |
| --- | --- | --- |
| Find my Innflow workflows. | innflow_list_workflows | List only workflows available to the connected account; follow pagination. |
| Show the deployment status and trigger of my sample workflow. | innflow_list_workflows, innflow_get_workflow | Resolve the sample workflow and describe its saved state accurately. |
| Show the latest execution of my sample workflow. | innflow_list_executions, innflow_get_execution | Return the real execution status and ID. |
| Investigate the failed sample execution. | innflow_get_execution, innflow_get_execution_logs | Identify the failing node using logs, without replaying the workflow. |
| Run the designated side-effect-free sample workflow with the agreed test input. | innflow_get_workflow, innflow_execute_workflow, innflow_get_execution | Execute only the specified test workflow, and report the observed final state rather than claiming dispatch means success. |

Confirm exact tool names from discovery before running. Authoring is conditional;
only advertise and demonstrate it when the review workspace exposes those tools.

### Negative review cases (to run)

| Scenario | Expected behavior |
| --- | --- |
| Read a workflow outside the reviewer's authorized workspace. | Access is denied; no private workflow details returned. |
| Diagnose a failed workflow that sends external messages. | Inspect only; do not replay or activate it without an execution request. |
| Ask to create a workflow when authoring tools are unavailable. | Explain the limitation and provide a design; do not claim to have saved a draft. |

### Release notes

Version 0.1.1 adds Apache-2.0 licensing, Grok Build compatibility metadata, complete
public listing links, and a separate single-plugin archive for OpenAI submission.
The hosted MCP endpoint and workflow skill are unchanged.
