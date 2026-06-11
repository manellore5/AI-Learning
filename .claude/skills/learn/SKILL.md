---
name: learn
description: Generate study notes from a YouTube video — link, glossary, key notes, and a Mermaid understanding diagram — saved as a markdown file per video, organized by course, and committed to git. Use when the user wants to /learn a YouTube URL, take notes from a video, or process a course lecture into reviewable notes.
---

# /learn — YouTube video → study notes

## Quick start

```
/learn <youtube-url> --course "<Course_Name>"
```

Example: `/learn https://youtube.com/watch?v=abc123 --course "Andrew_Ng_DeepLearning"`

## What it produces

One self-contained markdown file per video at `<Course>/<Title>.md` with:
1. YouTube URL (clickable, at the top)
2. Glossary table
3. Key Notes (chapter-aware for long videos)
4. Mermaid `graph TD` understanding diagram

Plus the raw transcript saved to `<Course>/.transcripts/<Title>.txt` (hidden folder, so notes can be regenerated later without cluttering the index).

`<Course>` is a top-level folder per learning. It may be nested (e.g. `Mattpock/AI coding for real engineers`) — pass the path you want in `--course`.

## Workflow

Follow these steps in order:

1. **Parse args** — extract `<url>` and `--course "<Course>"` (the destination folder, may be nested). If course is missing, ask the user.
2. **Fetch transcript** — create a temp workdir, then run:
   ```
   python scripts/fetch_transcript.py <url> --workdir <tmp>
   ```
   Outputs `transcript.txt`, `title.txt`, and (sometimes) `chapters.json` in the workdir.
   - If the URL is not a YouTube / yt-dlp-supported site (e.g. a paid course player like aihero.dev), this returns `Unsupported URL`. In that case, ask the user to paste the transcript text and skip to step 4.
3. **Read** `transcript.txt`, `title.txt`, and `chapters.json` (if present) with the Read tool.
4. **Determine destination** — `<Course>/<Sanitized_Title>.md`. Sanitize the title: keep alphanumerics, spaces, hyphens; drop other punctuation. If a note with that name already exists in the course, stop and tell the user (don't duplicate).
5. **Generate the note** using the template below. Compose it yourself from the transcript — do not call an external LLM.
6. **Save files** — write `<Course>/<Title>.md`, and copy the transcript to `<Course>/.transcripts/<Title>.txt`.
7. **Update indexes** — run `python scripts/update_index.py` (rebuilds the master `INDEX.md` and each `<Course>/INDEX.md`).
8. **Git commit + push**:
   ```
   git add "<Course>" INDEX.md
   git commit -m "Add notes: <Course>/<Title>"
   git push 2>$null  # ignore failure if no remote configured
   ```

## notes.md template

```markdown
# <Video Title>
Source: <url> · Course: <Course> · Added: <YYYY-MM-DD>

## Glossary
| Term | Definition |
|------|------------|
| <term> | <one or two tight sentences> |

## Key Notes
### <Topic or Chapter Title>
- <key point>
- <key point>

## Understanding Diagram
\`\`\`mermaid
graph TD
  A[Concept] --> B[Related concept]
\`\`\`
```

## Writing guidance

**Glossary** — tight, opinionated, one or two sentences. Define what the term IS, not what it does. When the field uses several words for the same thing, pick one and list the rest after `_Avoid_:`. Skip generic terms the user already knows.

**Key Notes** — bulleted, organized by topic. If `chapters.json` exists AND the video is longer than ~30 minutes, use one `### <Chapter Title>` subsection per chapter (preserves lecture structure for recall). Otherwise group by natural topic.

**Mermaid diagram** — `graph TD` (top-down). Short node labels (1–4 words). Show relationships between the main concepts the video covers, not every detail. Aim for 5–12 nodes — readable, not exhaustive. Test mentally: would this make sense at a glance in 3 months?

## Edge cases

- **No course flag** — ask the user before proceeding.
- **URL already processed** — a note with that title already exists in the course; report and stop (don't duplicate).
- **Captions unavailable** — `fetch_transcript.py` falls back to audio transcription automatically (slower, ~10–15 min per hour of video on CPU).
- **Very long video (>3 hours)** — transcript may strain context; warn the user and offer to process by chapter range if needed.
- **No git remote** — push will fail silently; commit still succeeds. Mention this to the user once.
