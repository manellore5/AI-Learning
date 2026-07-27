# AI-Learning

My study-notes repo for AI/ML topics. Each lesson, article, or video becomes a self-contained markdown note — **source link**, **summary**, **glossary**, **key notes**, and a **Mermaid understanding diagram** — filed under a **topic category** and indexed automatically.

Browse everything from [`INDEX.md`](INDEX.md) (auto-generated). For how a source becomes a note, see [How These Notes Are Made (Process)](How%20These%20Notes%20Are%20Made%20%28Process%29.md).

## Categories

Top-level folders are **topic categories**. A category can hold notes directly or nest them per source (e.g. `AI in SDLC/F1loop-Notes/`, `Harness Engineering/…`).

| Category | What goes here |
|----------|----------------|
| [AI in SDLC](AI%20in%20SDLC/INDEX.md) | Using AI across the software development lifecycle — planning, PRDs, skills, agentic loops, TDD (incl. the F1loop and Matt Pocock courses, and AWS AI-DLC Workflows) |
| Agentic AI | Agent design, planning, tool use, multi-agent systems *(placeholder — no notes yet)* |
| [Loop Engineering](Loop%20Engineering/INDEX.md) | Designing the loops that drive agents — model/instruction/task/agent/multi-agent loop stacks |
| [MCP](MCP/INDEX.md) | Model Context Protocol — building servers and tools |
| RAG | Retrieval-augmented generation — retrieval, chunking, embeddings, reranking, eval *(placeholder — no notes yet)* |
| [Context Engineering](Context%20Engineering/INDEX.md) | Managing what the model carries — context windows, pruning/compaction, memory, knowledge formats |
| [Prompt Engineering](Prompt%20Engineering/INDEX.md) | Prompt design, prompt caching, token efficiency |
| [Harness Engineering](Harness%20Engineering/INDEX.md) | The scaffolding around a model — sandboxes, hooks, skills, guides & sensors, verification |
| [Agentic Security](Agentic%20Security/INDEX.md) | Security risks and vulnerabilities in agents / MCP |

**Other / foundational folders** (kept as-is, outside the topic taxonomy):

| Folder | What goes here |
|--------|----------------|
| [LLM Internals](LLM%20Internals/INDEX.md) | How LLMs work under the hood — tokenizers, transformers, attention |
| [AWS AI Practitioner](AWS%20AI%20Practitioner/INDEX.md) | AWS Certified AI Practitioner exam prep |
| [Anki](Anki/INDEX.md) | Driving Anki (spaced repetition) from Claude |
| [sandcastle-notes](sandcastle-notes/INDEX.md) | Sandcastle sandboxing notes |
| Chess | Chess openings flashcards |

Empty categories (**Agentic AI**, **RAG**) carry a placeholder `README.md` so the folder exists in git; they don't appear in [`INDEX.md`](INDEX.md) until they hold a real note (the indexer skips zero-note folders and ignores `README.md`).

## Layout

```
INDEX.md                         ← master index of every category (auto)
<Category>/                      ← one top-level folder per topic category (may nest per source)
  INDEX.md                       ← index of notes in this category (auto)
  <Note Title>.md                ← url + summary + glossary + key notes + Mermaid diagram
  .transcripts/<Note Title>.txt  ← raw transcript/source text (hidden; kept for regeneration)
scripts/                         ← the pipeline tooling
.claude/skills/learn/SKILL.md    ← the /learn skill
requirements.txt
```

A `<Category>` folder can nest sources — e.g. `AI in SDLC/Mattpock/AI coding for real engineers/` — by passing that path to `--course`. Notes can be `.md` (from `/learn`) or any `.txt`; the indexer lists both, recursing to any depth inside a category. Notes are commonly suffixed with their author/organization (e.g. `… - Addy Osmani`, `Prompt Caching-rajibdeb`) to distinguish sources on the same topic.

## How to add notes

Open this repo in Claude Code and run the `/learn` skill, passing the destination **category** as `--course`:

```
/learn https://youtube.com/watch?v=XXXX --course "LLM Internals"
```

It fetches the transcript, composes the note (summary + glossary + key notes + Mermaid), files it under the category, rebuilds the indexes, and commits + pushes.

**The `<url>` can also be a web article** (blog post, docs page). `/learn` fetches the page, extracts the main body text, and composes the same note from it — no transcript needed.

```
/learn https://martinfowler.com/articles/harness-engineering.html --course "Harness Engineering"
```

**For paid/login-gated pages** (e.g. aihero.dev) neither `yt-dlp` nor the page fetch can read the content. Open the lesson, paste the transcript/article text, and ask Claude to generate the note from it — the output is identical, just sourced from pasted text.

## One-time setup

```bash
pip install -r requirements.txt   # yt-dlp + faster-whisper
# ffmpeg is required by yt-dlp for audio/subtitles:
#   macOS:   brew install ffmpeg
#   Windows: winget install Gyan.FFmpeg
```

`yt-dlp` grabs captions (fast path); if a video has none, `faster-whisper` transcribes the audio locally on CPU. No cloud LLM — Claude (in Claude Code) writes the notes directly.

## Rebuild the index manually

```bash
python scripts/update_index.py
```

Idempotent — safe to run any time. Skips `scripts/`, `.claude/`, hidden folders, and transcript files, and regenerates the master `INDEX.md` plus each `<Category>/INDEX.md`.
