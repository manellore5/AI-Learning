# Sandcastle — Quickstart (get productive in ~15 min)

Goal: install Sandcastle, wire up your Claude subscription, and get one agent to make a commit in an isolated sandbox. For the *why* behind each step and everything else, see the **[Reference](02-reference.md)**.

> **Mental model refresher:** `run()` = copy code into an isolated **sandbox** → let an **agent** work on a **prompt** → merge the resulting **commits** back to your repo. Three slots: **agent** (who), **sandbox** (where), **branchStrategy** (how changes return).

---

## 0. Prerequisites

- **Node.js** (with `npm`/`npx`) and **Git**.
- **A sandbox runtime.** For local dev, install **[Docker Desktop](https://www.docker.com/)** (our recommended default). Alternatives: Podman (rootless), or Vercel (cloud microVMs — no local Docker needed).
- **A Claude login** — your **Claude Pro/Max subscription** works (recommended), or an Anthropic API key.
- Run these inside a **git repository** (Sandcastle operates on your repo).

Sanity check:

```bash
node -v && git --version && docker info | head -1
```

---

## 1. Install

```bash
npm install --save-dev @ai-hero/sandcastle
```

## 2. Scaffold the config

```bash
npx @ai-hero/sandcastle init
```

This creates a **`.sandcastle/`** directory in your repo containing:

- `Dockerfile` — the sandbox image (what tools the agent has available)
- `prompt.md` — the default prompt template
- `main.ts` (or `main.mts`) — the runnable entry script calling `run()`
- `.env.example` — the env vars the agent needs
- prompt templates (`implement`, `plan`, `review`, `merge`) you can build pipelines from

## 3. Authenticate — use your Claude subscription ⭐

Create your env file and add a token:

```bash
cp .sandcastle/.env.example .sandcastle/.env
```

**Option A — Claude Pro/Max subscription (recommended).** On your host, run:

```bash
claude setup-token
```

Copy the value into `.sandcastle/.env`:

```dotenv
CLAUDE_CODE_OAUTH_TOKEN=sk-ant-oat-...
GH_TOKEN=ghp_...            # GitHub token, so the agent can use gh / push
```

The agent inside the sandbox now uses **your Claude subscription** — no per-token API billing.

**Option B — Anthropic API key (pay-per-token).** Instead of the OAuth token, set:

```dotenv
ANTHROPIC_API_KEY=sk-ant-...
```

> **Team note:** each engineer uses **their own** `CLAUDE_CODE_OAUTH_TOKEN`. `.sandcastle/.env` is git-ignored — never commit tokens. In **CI**, a subscription token usually isn't available, so pipelines typically use `ANTHROPIC_API_KEY` from a secret store (see the [CI recipe](02-reference.md#recipe-4--ci--automation)).

## 4. Your first run

Edit `.sandcastle/prompt.md` to a small, safe task, e.g.:

```markdown
Add a `CONTRIBUTING.md` with a short "How to run tests" section. Keep it under 20 lines.
```

`.sandcastle/main.ts` already contains something like:

```typescript
import { run, claudeCode } from "@ai-hero/sandcastle";
import { docker } from "@ai-hero/sandcastle/sandboxes/docker";

await run({
  agent: claudeCode("claude-opus-4-8"),
  sandbox: docker(),
  promptFile: ".sandcastle/prompt.md",
});
```

Run it:

```bash
npx tsx .sandcastle/main.ts
```

What happens: Sandcastle builds the sandbox image → starts an isolated container → the agent works on your prompt → any commit it makes is brought back to your repo. With Docker's default **`head`** strategy, the change lands **directly on your current branch's working tree**.

## 5. Verify it worked

```bash
git log --oneline -3     # the agent's commit should be here
git status               # see what changed
```

You just ran an AI agent in a box and got a commit back. 🎉

---

## 6. A slightly more real example — put commits on a branch

Don't want the agent touching your working tree? Send its work to a **named branch** instead:

```typescript
import { run, claudeCode } from "@ai-hero/sandcastle";
import { docker } from "@ai-hero/sandcastle/sandboxes/docker";

const result = await run({
  agent: claudeCode("claude-opus-4-8"),
  sandbox: docker(),
  branchStrategy: { type: "branch", branch: "agent/add-contributing" },
  promptFile: ".sandcastle/prompt.md",
  maxIterations: 3,          // let it iterate up to 3 times
  name: "add-contributing",  // label in the logs
});

console.log(result.commits); // [{ sha: "…" }]
console.log(result.branch);  // "agent/add-contributing"
```

Then review it like any PR: `git checkout agent/add-contributing`.

---

## 7. The one recipe worth learning early: implement → verify → review

This is the pattern most teams reach for. It uses **`createSandbox()`** so both agents share **one warm container** (deps installed once), with a **test gate** between them:

```typescript
import { createSandbox, claudeCode } from "@ai-hero/sandcastle";
import { docker } from "@ai-hero/sandcastle/sandboxes/docker";

await using sandbox = await createSandbox({
  branch: "agent/fix-42",
  sandbox: docker(),
  hooks: { sandbox: { onSandboxReady: [{ command: "npm install" }] } },
});

// 1) Implement
await sandbox.run({
  agent: claudeCode("claude-opus-4-8"),
  promptFile: ".sandcastle/implement.md",
  maxIterations: 5,
});

// 2) Gate: run tests directly in the same sandbox (non-zero exitCode is returned, not thrown)
const tests = await sandbox.exec("npm test");
if (tests.exitCode !== 0) throw new Error(`Tests failed:\n${tests.stdout}\n${tests.stderr}`);

// 3) Review on the same branch + container
await sandbox.run({
  agent: claudeCode("claude-sonnet-4-6"),
  prompt: "Review the changes and fix any issues.",
});
```

`await using` tears the sandbox down automatically when the block ends. Full explanation in the [reference](02-reference.md#createsandbox--reusable-warm-sandbox).

---

## Next steps

- **Understand the moving parts** → [Reference: core concepts](02-reference.md#core-concepts--the-vocabulary) and [the three slots](02-reference.md#the-three-slots-in-depth).
- **Pick the right sandbox for us** → [provider comparison](02-reference.md#2-the-sandbox-slot--where-it-runs).
- **Build our real workflows** → [recipes](02-reference.md#recipes) (parallel agents, review pipeline, custom agents, CI).
- **Every option** → [full options reference](02-reference.md#appendix-b--full-options-reference).

---

## Troubleshooting the first run

| Symptom | Likely cause / fix |
|---|---|
| `docker: command not found` / can't connect | Docker Desktop isn't running. Start it; re-run `docker info`. |
| Auth / 401 errors from the agent | `CLAUDE_CODE_OAUTH_TOKEN` missing or expired — re-run `claude setup-token`. Or set `ANTHROPIC_API_KEY`. |
| Agent can't push / use `gh` | `GH_TOKEN` not set in `.sandcastle/.env`. |
| Run hangs then times out | Idle timeout (default 600s) — the agent produced no output. Check the prompt is actionable; see logs under `.sandcastle/logs/`. |
| First build is slow | The sandbox Docker image is building. Subsequent runs reuse it. |

More in the [reference troubleshooting section](02-reference.md#troubleshooting--gotchas).
