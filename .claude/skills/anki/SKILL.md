---
name: anki
description: Turn a source (YouTube/Udemy/article URL, PPTX, PDF, or an existing /learn note) into dense topic-overview Anki flashcards — one card per concept-topic with explainer, example, glossary, diagram, and collapsible details — grouped into content-sized decks (~20–30 cards) and pushed to Anki via AnkiConnect, with a git-tracked markdown source-of-truth. Use when the user wants to /anki a source or make Anki cards / flashcards from a document, slides, video, or article.
---

# /anki — source → topic-overview Anki cards

Sibling of `/learn`. `/learn` makes one readable note per source; `/anki` makes
**spaced-repetition cards**: split a source into concept-topics, emit **one dense card
per topic** into Anki, plus a git-tracked markdown source-of-truth.

Verbatim payloads, the note model, the markdown template, and the sync logic live in
[REFERENCE.md](REFERENCE.md). Read it before step 5.

## Quick start

```
/anki <source> --course "<Course>"     # e.g. --course "AWS/AI Practitioner"
```

`<source>` auto-detected: **http(s)** → web/YouTube/Udemy · **`.pptx`/`.pdf`** →
`scripts/parse_slides.py` · **existing `/learn` `.md`** → reuse as source text.
Optional `--pages <start>-<end>` to restrict a PDF/slide range.

## Prerequisites (check, don't assume)

1. **Anki open + AnkiConnect** (add-on `2055492159`). Probe before any push:
   `curl -s localhost:8765 -X POST -d '{"action":"version","version":6}'`. Refused →
   see **Anki offline** below.
2. **`pip install python-pptx pymupdf`** — only for `.pptx`/`.pdf` (in `requirements.txt`).
3. **Internet** for kroki.io — only when rendering a generated Mermaid diagram.

## Workflow

1. **Parse args** — `<source>`, `--course`, optional `--pages`. Missing course → ask.
2. **Get source text** — by type:
   - YouTube → `python scripts/fetch_transcript.py <url> --workdir <tmp>`.
   - Web/Udemy → `WebFetch` (title + full body; exclude nav/ads/footer). Fallbacks:
     redirect → retry new URL; JS/gated → Jina `https://r.jina.ai/<url>`; else ask to paste.
   - PPTX/PDF → `python scripts/parse_slides.py "<file>" --workdir <tmp>` → reads
     `sections.json` (`{index,title,text,images[]}`) + images in `<tmp>/media/`. Honor
     `--pages` by keeping only that index range.
   - Existing `/learn` `.md` → read directly, no re-fetch.
3. **Cluster into concept-topics** — group the body into coherent self-contained topics
   (may span or split sections). Slug each: lowercase, alphanumerics→`-`.
   `<source-id>` = slug of `<Course>/<Title>` (stable across re-runs).
4. **Propose decks (~20–30 cards) and CONFIRM** — decks are content-sized, NOT per-source:
   right-sized source → own deck `<Course>::<Title>`; small → join a related existing deck
   (check `deckNames`); large (>~35) → split into themed sub-decks. Show deck name(s) +
   counts, **wait for confirmation** before any push. Record each topic's deck.
5. **Build each card** — fill `TopicOverview` fields (Topic/Explainer/Application/Glossary/
   Diagram/Details) per [REFERENCE.md](REFERENCE.md). `Application` = a use-case OR an
   example, whichever fits (bold-labelled). Diagram, in priority order:
   (a) **slide deck (PDF/PPTX)** → render a title-less content crop of the diagram slide:
   `python scripts/render_slide.py <pdf> --pages <N> --out-dir <tmp>/media --prefix <id>`
   (drops the slide title — redundant with the front — and the watermark/footer, never
   cuts diagram content; PPTX: convert to PDF first via `soffice --headless --convert-to pdf`);
   (b) **article figure** → use the real image as-is;
   (c) **no usable image** but a diagram aids recall → author Mermaid and render
   `python scripts/render_mermaid.py --src <tmp>/d.mmd --out <tmp>/media/<id>-<slug>.png`;
   (d) else leave empty.
6. **Push media + notes** — ensure model (`createModel` if missing) and deck(s)
   (`createDeck`); `storeMediaFile` each image; then sync notes (step 7). See REFERENCE.md.
7. **Sync (idempotent)** — per topic, `findNotes tag:src::<id> tag:topic::<slug>` →
   update if found (move deck via `changeDeck` if changed), else `addNote`. Report removed
   topics; never auto-delete. Full payloads in REFERENCE.md.
8. **Write markdown** — `<Course>/<Sanitized Title> — Cards.md` (template in REFERENCE.md),
   one block per topic with its deck + tags. Copy raw source to `<Course>/.transcripts/`,
   diagram images to `<Course>/.transcripts/media/`.
9. **Index + commit**:
   ```
   python scripts/update_index.py
   git add "<Course>" INDEX.md scripts requirements.txt && git commit -m "Add Anki cards: <Course>/<Title>"
   git push 2>$null
   ```
10. **Report** — deck(s) + counts, added vs updated, removed-topic warnings, and (if Anki
    was closed) that the push was skipped.

## Edge cases

- **No course flag** → ask.
- **Anki offline** (port refused) → still build cards + write markdown + commit/push, then
  warn: "Anki not running — cards not pushed. Open Anki and re-run; tag-keyed sync pushes
  with no duplicates." Don't block the markdown.
- **PPTX/PDF dep missing** → `parse_slides.py` exits with a `pip install` hint; relay it.
- **kroki fails / render error** → skip that diagram (leave Diagram empty), note it, continue.
- **Source already has cards** → not an error; step 7 syncs.
- **Paywalled player** (e.g. aihero.dev) → fetch blocked; ask user to paste, continue from step 3.
- **No git remote** → push fails silently; commit still succeeds. Mention once.
