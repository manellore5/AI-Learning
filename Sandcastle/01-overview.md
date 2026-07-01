# Sandcastle — Overview & Quick Revision

A one-page skim of **[`@ai-hero/sandcastle`](https://github.com/mattpocock/sandcastle)** — enough to grok it (or re-grok it) in a few minutes. For install, full detail, diagrams, and recipes, go to **[Detailed Notes](02-detailed-notes.md)**.

---

## In one paragraph

Sandcastle is a **TypeScript library that runs an AI coding agent against a copy of your repo, inside an isolated sandbox, then merges the good commits back**. One call — `run()` — does the whole loop: copy code in → run the agent on a prompt → collect commits → merge home. It's **provider-agnostic** (Docker, Podman, Vercel, or your own) and **unopinionated** about workflow. You get **safety** (agents can't wreck your working tree), **parallelism** (many agents/branches at once), and **pipelines** (implement → verify → review → merge) — identically local or in CI.

```typescript
import { run, claudeCode } from "@ai-hero/sandcastle";
import { docker } from "@ai-hero/sandcastle/sandboxes/docker";

await run({
  agent: claudeCode("claude-opus-4-8"), // WHO
  sandbox: docker(),                      // WHERE (isolated)
  promptFile: ".sandcastle/prompt.md",   // WHAT
});
```

---

## Mental model (the part to actually remember)

**① Walled construction site.** Your real repo is your **house** (the *Host*). You'd never let a contractor swing a hammer in your live house — you give them a **fenced site** with a copy of the plans (the *Sandbox*). The contractor is the *Agent*. **Sandcastle is the site manager**: fences the site, hands over the blueprint (*prompt*), lets them build, inspects, and **merges the finished work back home** (*branch strategy*). → build in a sandbox, bring the good parts home.

**② Three pluggable slots + one data flow.** Everything is one of three slots or config around them:

![Sandcastle's three pluggable slots feeding run()](diagrams/01-overview-1.svg)

<!-- Mermaid source: diagrams/01-overview-1.mmd — edit then re-render via scripts/render_mermaid.py -->

![Host-to-sandbox data flow: code in, commits out](diagrams/01-overview-2.svg)

<!-- Mermaid source: diagrams/01-overview-2.mmd — edit then re-render via scripts/render_mermaid.py -->

Hold **agent (who) · sandbox (where) · branchStrategy (how) · prompt→commits (flow)** and everything else slots in.

---

## The repo / package at a glance

- **Package:** `@ai-hero/sandcastle` — install as a dev dependency; scaffold with `npx @ai-hero/sandcastle init`.
- **`.sandcastle/` (scaffolded in your repo):** `Dockerfile` (sandbox image), `prompt.md` + `implement`/`plan`/`review`/`merge` templates, `main.ts` (entry calling `run()`), `.env` (tokens).
- **Main exports:** `run`, `interactive`, `createSandbox`, `createWorktree`, `Output` (structured output), agent providers (`claudeCode`, `codex`, `copilot`, `cursor`, `opencode`), and session helpers.
- **Sandbox providers (separate import paths):** `docker`, `podman`, `vercel`, `no-sandbox` (+ `createBindMountSandboxProvider` / `createIsolatedSandboxProvider` for custom).
- **Auth:** your **Claude Pro/Max subscription** via `CLAUDE_CODE_OAUTH_TOKEN` (`claude setup-token`), or `ANTHROPIC_API_KEY`; plus `GH_TOKEN`.

---

## The three slots (cheat-sheet)

**Agents (`agent`)** — `claudeCode` ⭐ · `codex` · `copilot` · `cursor` · `opencode` · custom. Swappable.

**Sandboxes (`sandbox`)**

| Provider | Type | Use for |
|---|---|---|
| **docker** ⭐ | Bind-mount | Local dev (default) |
| podman | Bind-mount | Rootless / secure hosts |
| vercel | Isolated (microVM) | CI / no local Docker |
| no-sandbox | None | Trusted interactive only |

**Branch strategies (`branchStrategy`)**

| Strategy | Commits land… | Default for |
|---|---|---|
| `head` | your current working dir | bind-mount (docker/podman) |
| `merge-to-head` | temp branch → merged into HEAD | isolated (vercel) |
| `branch` | a named branch (reviewable/PR) | — |

---

## A tiny end-to-end example (implement → verify → review)

One warm sandbox, a test gate between two agents:

```typescript
import { createSandbox, claudeCode } from "@ai-hero/sandcastle";
import { docker } from "@ai-hero/sandcastle/sandboxes/docker";

await using sandbox = await createSandbox({
  branch: "agent/fix-42",
  sandbox: docker(),
  hooks: { sandbox: { onSandboxReady: [{ command: "npm install" }] } },
});

await sandbox.run({ agent: claudeCode("claude-opus-4-8"), promptFile: ".sandcastle/implement.md", maxIterations: 5 });

const tests = await sandbox.exec("npm test");       // exitCode returned, not thrown
if (tests.exitCode !== 0) throw new Error(tests.stderr);

await sandbox.run({ agent: claudeCode("claude-sonnet-4-6"), prompt: "Review the changes and fix any issues." });
```

---

## Quick-revision checklist (the things people forget)

- **Iteration = one agent invocation = ≤ 1 commit.** `run()` loops up to `maxIterations` (default **1**).
- **Stop early** with the **completion signal** (default `<promise>COMPLETE</promise>`) — tell the agent to emit it.
- **Two timeouts:** `idleTimeoutSeconds` (600) → silence **fails** the run; `completionTimeoutSeconds` (60) → grace after the signal, expiry **succeeds** with a warning.
- **Prompts:** `prompt` (inline, literal) **or** `promptFile` (supports `{{KEY}}` args + `` !`shell` `` expansion). Not both.
- **`head` has no worktree** → `copyToWorktree` and worktree hooks need `merge-to-head` or `branch`.
- **Reuse a sandbox** with `createSandbox()` (warm deps, `sandbox.exec()` for test gates); `await using` auto-closes.
- **Structured output** (`Output.object({tag,schema})`) needs `maxIterations === 1` and the tag in the prompt.
- **Same code, any provider** — only the `sandbox:` argument changes across docker/podman/vercel.
- **Secrets:** `.sandcastle/.env` is git-ignored; local = subscription token, CI = API key.

---

## Where to go next → [Detailed Notes](02-detailed-notes.md)

- [Getting started (install & first run)](02-detailed-notes.md#getting-started-install--first-run)
- [The three slots in depth](02-detailed-notes.md#the-three-slots-in-depth) · [Execution model](02-detailed-notes.md#the-execution-model) · [Advanced building blocks](02-detailed-notes.md#advanced-building-blocks)
- [Recipes](02-detailed-notes.md#recipes): parallel agents · implement→review · custom agents · CI
- [Full options reference](02-detailed-notes.md#appendix-b--full-options-reference) · [Primers](02-detailed-notes.md#appendix-a--primers) · [Glossary](02-detailed-notes.md#glossary)
