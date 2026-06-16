---
name: learn
description: Generate study notes from a YouTube video OR a web article/page — link, glossary, key notes, and a Mermaid understanding diagram — saved as a markdown file per source, organized by course, and committed to git. Use when the user wants to /learn a YouTube URL or any web URL, take notes from a video or article, or process a lecture/blog post/docs page into reviewable notes.
---

# /learn — video or web article → study notes

## Quick start

```
/learn <url> --course "<Course_Name>"
```

The `<url>` can be a **YouTube video** or **any web page** (article, blog post, docs):
- `/learn https://youtube.com/watch?v=abc123 --course "Andrew_Ng_DeepLearning"`
- `/learn https://martinfowler.com/articles/some-post.html --course "Architecture"`

## What it produces

One self-contained markdown file per source at `<Course>/<Title>.md` with:
1. Source URL (clickable, at the top)
2. A 4–5 line **Summary** (quick "what's this about" reference)
3. Glossary (bold-term format with `_Avoid_:` aliases)
4. Key Notes (chapter-aware for long videos)
5. Mermaid `graph TD` understanding diagram

Plus the raw source text saved to `<Course>/.transcripts/<Title>.txt` (hidden folder, so notes can be regenerated later without cluttering the index) — the video transcript for videos, or the extracted article text for web pages.

`<Course>` is a top-level folder per learning. It may be nested (e.g. `Mattpock/AI coding for real engineers`) — pass the path you want in `--course`.

## Workflow

Follow these steps in order:

1. **Parse args** — extract `<url>` and `--course "<Course>"` (the destination folder, may be nested). If course is missing, ask the user.
2. **Get the source text** — branch on what `<url>` is:

   **(a) YouTube / yt-dlp-supported video** — create a temp workdir, then run:
   ```
   python scripts/fetch_transcript.py <url> --workdir <tmp>
   ```
   Outputs `transcript.txt`, `title.txt`, and (sometimes) `chapters.json` in the workdir. Read them with the Read tool.

   **(b) Any other web page (article / blog / docs)** — fetch the page content directly:
   - Use the **`WebFetch`** tool on `<url>` with a prompt like *"Return the article's title on the first line, then the full main body text verbatim — headings, paragraphs, code blocks, lists. Exclude nav, ads, cookie banners, comments, and footer."*
   - Treat the returned title as `title.txt` and the body as the source text (the article's equivalent of a transcript). There are no chapters.
   - **Fallbacks:** if `WebFetch` fails (404, cross-host redirect → retry with the new URL, or a JS-heavy/login-gated page returns little usable text), drive the **Playwright browser** (`browser_navigate` → `browser_snapshot` / read page text) to read the rendered content. If the page is genuinely gated and neither works, ask the user to paste the text and continue from step 4.

   **(c) Paid course player (e.g. aihero.dev)** — `fetch_transcript.py` returns `Unsupported URL` and `WebFetch` is blocked by the paywall; ask the user to paste the transcript/article text, then continue from step 4.
3. **Confirm the source text** is in hand (transcript or article body) plus a title (and `chapters.json` if a video).
4. **Determine destination** — `<Course>/<Sanitized_Title>.md`. Sanitize the title: keep alphanumerics, spaces, hyphens; drop other punctuation. If a note with that name already exists in the course, stop and tell the user (don't duplicate).
5. **Generate the note** using the template below. Compose it yourself from the source text — do not call an external LLM.
6. **Save files** — write `<Course>/<Title>.md`, and copy the source text to `<Course>/.transcripts/<Title>.txt`.
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

## Summary
<4–5 lines, plain language: what this video is about and what you'll take away. Written so a future reader can decide in 10 seconds whether to open it.>

## Glossary
**<Term>**:
<One or two tight sentences — define what the term IS.>
_Avoid_: <alias>, <alias>

**<Term>**:
<Definition.>

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

**Summary** — 4–5 lines, the first thing after the metadata. Plainly state what the video covers and the main takeaway, so it works as a quick reference without opening the full notes. No jargon the reader wouldn't already know; this is the "should I revisit this?" blurb.

**Glossary** — use the bold-term format (not a table): `**Term**:` on its own line, the definition on the next line, then an optional `_Avoid_: alias1, alias2` line listing other words for the same thing. Tight and opinionated — one or two sentences defining what the term IS, not what it does. Prefer the glossary's own terms inside other definitions. Group under `### <subheading>` if natural clusters emerge. Skip generic terms the user already knows.

**Key Notes** — bulleted, organized by topic. If `chapters.json` exists AND the video is longer than ~30 minutes, use one `### <Chapter Title>` subsection per chapter (preserves lecture structure for recall). Otherwise group by natural topic.

**Mermaid diagram** — `graph TD` (top-down). Short node labels (1–4 words). Show relationships between the main concepts the video covers, not every detail. Aim for 5–12 nodes — readable, not exhaustive. Test mentally: would this make sense at a glance in 3 months?

## Edge cases

- **No course flag** — ask the user before proceeding.
- **URL already processed** — a note with that title already exists in the course; report and stop (don't duplicate).
- **Captions unavailable** (video) — `fetch_transcript.py` falls back to audio transcription automatically (slower, ~10–15 min per hour of video on CPU).
- **Very long video (>3 hours)** — transcript may strain context; warn the user and offer to process by chapter range if needed.
- **Web page returns little/no text** — likely JS-rendered or gated; fall back to the Playwright browser, then to asking the user to paste.
- **Web page has no clear title** — derive a sensible title from the H1 or the page topic; confirm with the user if ambiguous.
- **Paywalled / login-only page** — neither `WebFetch` nor the browser will get clean text; ask the user to paste it.
- **No git remote** — push will fail silently; commit still succeeds. Mention this to the user once.
