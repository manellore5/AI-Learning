# AI-Learning

My study-notes repo for AI/ML courses. Each lesson becomes a self-contained markdown note — **glossary**, **key notes**, and a **Mermaid understanding diagram** — organized in a folder per course and indexed automatically.

Browse everything from [`INDEX.md`](INDEX.md). For how a video becomes a note, see [How These Notes Are Made (Process)](How%20These%20Notes%20Are%20Made%20%28Process%29.md).

## Layout

```
INDEX.md                         ← master index of every course (auto)
<Course>/                        ← one top-level folder per learning (may be nested)
  INDEX.md                       ← index of notes in this course (auto)
  <Note Title>.md                ← url + summary + glossary + key notes + Mermaid diagram
  .transcripts/<Note Title>.txt  ← raw transcript (hidden; kept for regeneration)
scripts/                         ← the pipeline tooling
.claude/skills/learn/SKILL.md    ← the /learn skill
requirements.txt
```

A `<Course>` folder can be nested — e.g. `Mattpock/AI coding for real engineers/` — by passing that path to `--course`. Notes can be `.md` (from `/learn`) or any `.txt`; the indexer lists both.

## How to add notes

Open this repo in Claude Code and run the `/learn` skill:

```
/learn https://youtube.com/watch?v=XXXX --course "Andrew_Ng_DeepLearning"
```

It fetches the transcript, composes the note (glossary + key notes + Mermaid), files it under `<Course>/`, rebuilds the indexes, and commits + pushes.

**The `<url>` can also be a web article** (blog post, docs page). `/learn` fetches the page, extracts the main body text, and composes the same note from it — no transcript needed.

```
/learn https://martinfowler.com/articles/some-post.html --course "Architecture"
```

**For paid/login-gated pages** (e.g. aihero.dev) neither `yt-dlp` nor the page fetch can read the content. Open the lesson, paste the transcript/article text, and ask Claude to generate the note from it — the output is identical, just sourced from pasted text.

## One-time setup

```powershell
pip install -r requirements.txt   # yt-dlp + faster-whisper
winget install Gyan.FFmpeg        # required by yt-dlp for audio/subtitles
```

`yt-dlp` grabs captions (fast path); if a video has none, `faster-whisper` transcribes the audio locally on CPU. No cloud LLM — Claude (in Claude Code) writes the notes directly.

## Rebuild the index manually

```powershell
python scripts/update_index.py
```

Idempotent — safe to run any time. Skips `scripts/`, `.claude/`, hidden folders, and transcript files.
