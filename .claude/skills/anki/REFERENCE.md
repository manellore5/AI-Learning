# /anki — reference (payloads, model, template)

Loaded on demand during a run. SKILL.md holds the workflow; this holds the
verbatim AnkiConnect payloads, the note model, and the markdown template.

## AnkiConnect basics

All calls are HTTP POSTs of JSON to `http://localhost:8765`, `"version": 6`.
For large payloads (HTML fields), write the JSON to a temp file and
`curl -s localhost:8765 -d @payload.json`.

Actions used: `version`, `modelNames`, `createModel`, `deckNames`, `createDeck`,
`storeMediaFile`, `addNote`, `findNotes`, `notesInfo`, `updateNoteFields`,
`findCards`, `changeDeck`.

## TopicOverview model (createModel — once)

Create if `modelNames` lacks `TopicOverview`.

```json
{
  "action": "createModel",
  "version": 6,
  "params": {
    "modelName": "TopicOverview",
    "inOrderFields": ["Topic", "Explainer", "Application", "Glossary", "Diagram", "Details"],
    "isCloze": false,
    "cardTemplates": [
      {
        "Name": "Card 1",
        "Front": "<div class=\"topic\">What is {{Topic}}?</div>",
        "Back": "{{FrontSide}}<hr id=answer><div class=\"explainer\">{{Explainer}}</div>{{#Application}}<div class=\"example\">{{Application}}</div>{{/Application}}{{#Glossary}}<div class=\"glossary\"><b>Glossary</b><br>{{Glossary}}</div>{{/Glossary}}{{#Diagram}}<div class=\"diagram\">{{Diagram}}</div>{{/Diagram}}{{#Details}}<details class=\"details\"><summary>▸ More details</summary>{{Details}}</details>{{/Details}}"
      }
    ],
    "css": ".card{font-family:-apple-system,Segoe UI,Roboto,Arial,sans-serif;font-size:18px;line-height:1.5;color:#222;background:#fff;text-align:left;max-width:760px;margin:0 auto;padding:6px 10px}.topic{font-size:22px;font-weight:700}hr#answer{margin:14px 0;border:none;border-top:1px solid #ddd}.explainer{margin:12px 0}.example{background:#f5f7ff;border-left:3px solid #6b8cff;padding:8px 12px;margin:10px 0;border-radius:4px}.glossary{margin:12px 0}.glossary b{color:#1a3b8c}.diagram{margin:12px 0}.diagram img{max-width:100%;height:auto;border:1px solid #eee;border-radius:4px}details.details{margin-top:14px;color:#444}details.details summary{cursor:pointer;font-weight:600;color:#1a3b8c}"
  }
}
```

The `{{#Field}}…{{/Field}}` conditionals hide Example/Glossary/Diagram/Details when empty.

## Card fields (what to put in each)

- **Topic** — specific topic name; front renders as *"What is {{Topic}}?"* (prefer
  `MCP Tool Annotations` over `Annotations`).
- **Explainer** — 2–3 lines, plain language, includes the "why it matters". The part
  you grade recall on.
- **Application** — EITHER a use-case OR a concrete example, whichever fits this topic
  (not both). Lead with a bold label so the reader knows which: `<b>Use case.</b> …`
  or `<b>Example.</b> …`. Empty only if neither adds anything.
- **Glossary** — terms *within this topic* as HTML: `<b>Term</b> — one-line def.<br>`
  per term. Skip generic terms.
- **Diagram** — `<img src="<id>-<slug>.png">` or empty. Priority: (a) for slide decks,
  a title-less content crop via `scripts/render_slide.py` (drops title + watermark/footer,
  never cuts diagram content); (b) a real article figure; (c) generated Mermaid via
  `scripts/render_mermaid.py` only when it truly aids recall; (d) empty.
- **Details** — extra depth, collapsed under `▸ More details`. Populate whenever there's
  more to say.

## addNote (per new topic)

```json
{
  "action": "addNote",
  "version": 6,
  "params": {
    "note": {
      "deckName": "<Course>::<Deck>",
      "modelName": "TopicOverview",
      "fields": {
        "Topic": "...",
        "Explainer": "...",
        "Application": "<b>Use case.</b> ...   (or <b>Example.</b> ... — whichever fits)",
        "Glossary": "<b>Term A</b> — definition.<br><b>Term B</b> — definition.",
        "Diagram": "<img src=\"<id>-<slug>.png\">",
        "Details": "..."
      },
      "tags": ["src::<source-id>", "topic::<slug>"],
      "options": {"allowDuplicate": false}
    }
  }
}
```

## storeMediaFile (before addNote, if the card has an image)

```json
{"action":"storeMediaFile","version":6,"params":{"filename":"<id>-<slug>.png","path":"<abs path to image>"}}
```

Use the same `<id>-<slug>.png` referenced in the Diagram field.

## Re-run sync (idempotent)

Card identity = tag pair `src::<source-id>` + `topic::<slug>`.

1. `findNotes {"query":"tag:src::<id> tag:topic::<slug>"}`.
   - **Found** → `updateNoteFields` with rebuilt fields. If the assigned deck changed,
     `findCards` for the note, then `changeDeck` those card ids to the new deck.
   - **Not found** → `addNote`.
2. **Removed topics** — `findNotes {"query":"tag:src::<id>"}`, map ids→slugs via
   `notesInfo`, and report any slug no longer produced. **Never auto-delete** — list them.

## Markdown source-of-truth (`<Course>/<Title> — Cards.md`)

```markdown
# <Title> — Anki Cards
Source: <url-or-file> · Course: <Course> · Added: <YYYY-MM-DD> · src-id: <source-id>

> <N> topic cards across deck(s): `<Course>::<Deck1>` (k), `<Course>::<Deck2>` (m).

## <Topic 1>
- Deck: `<Course>::<Deck>` · Tags: `src::<id>` `topic::<slug>`

**Explainer.** <2–3 lines.>

**Example.** <if any.>

**Glossary.**
- **<Term>** — <definition.>

**Diagram.** ![<alt>](.transcripts/media/<id>-<slug>.png) <!-- or: none -->

**More details.** <extra depth.>

## <Topic 2>
...
```

Keep a copy of stored diagram images under `<Course>/.transcripts/media/` so the git
artifact is self-contained.

## Design intent (don't re-litigate)

Dense overview cards = one revision sheet per topic, not atomic recall cards. Grade
Again/Hard/Good/Easy on the **Explainer**; treat Glossary/Diagram/Details as reference.
The `Glossary` field can later seed atomic per-term cards without re-fetching.
