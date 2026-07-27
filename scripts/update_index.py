"""Rebuild the repo's INDEX.md files for a free-form, course-per-folder layout.

Layout (any depth inside a top-level course folder is fine):

    <repo>/
      INDEX.md                         <- master index (auto)
      <Course or Source>/              <- one top-level folder per "learning"
        INDEX.md                       <- per-course index (auto)
        <anything>/<note>.md|.txt      <- notes, organized however you like

For each note it tries to read a metadata line of the form
    "Source: <url> · Course: <name> · Added: <YYYY-MM-DD>"
(produced by the /learn skill). If that's missing — e.g. a raw .txt note —
it falls back to the file name and path so the note still shows up and stays
searchable. Idempotent: safe to run any time.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent

# Top-level folders that are tooling/plumbing, not notes.
EXCLUDE_DIRS = {"scripts", ".claude", ".git", ".github", ".venv", "venv"}
NOTE_EXTS = {".md", ".txt"}
SKIP_NAMES = {"index.md", "readme.md"}

# Short blurb per top-level category, shown in the master INDEX.md.
# Keyed by exact folder name; unknown folders fall back to "—". Extend as
# categories are added (see README.md for the human-facing version).
CATEGORY_DESCRIPTIONS = {
    "AI in SDLC": "Using AI across the software development lifecycle — planning, PRDs, skills, agentic loops",
    "Agentic AI": "Agent design, planning, tool use, multi-agent systems",
    "Loop Engineering": "Designing the loops that drive agents — model/instruction/task/agent/multi-agent stacks",
    "MCP": "Model Context Protocol — building servers and tools",
    "RAG": "Retrieval-augmented generation — retrieval, chunking, embeddings, reranking, eval",
    "Context Engineering": "Managing what the model carries — context windows, compaction, memory, knowledge formats",
    "Prompt Engineering": "Prompt design, prompt caching, token efficiency",
    "Harness Engineering": "The scaffolding around a model — sandboxes, hooks, skills, guides & sensors, verification",
    "Agentic Security": "Security risks and vulnerabilities in agents / MCP",
    "LLM Internals": "How LLMs work under the hood — tokenizers, transformers, attention",
    "AWS AI Practitioner": "AWS Certified AI Practitioner exam prep",
    "Anki": "Driving Anki (spaced repetition) from Claude",
    "sandcastle-notes": "Sandcastle sandboxing notes",
    "Chess": "Chess openings flashcards",
}


def is_hidden(path: Path, base: Path) -> bool:
    """True if any folder between base and path starts with '.' (e.g. .transcripts)."""
    return any(part.startswith(".") for part in path.relative_to(base).parts[:-1])

META_RE = re.compile(
    r"Source:\s*(\S+)\s*[·|]\s*Course:\s*([^·|]+?)\s*[·|]\s*Added:\s*(\d{4}-\d{2}-\d{2})"
)


def is_note(path: Path) -> bool:
    name = path.name.lower()
    if path.suffix.lower() not in NOTE_EXTS or name in SKIP_NAMES:
        return False
    if name == "transcript.txt" or name.endswith(".transcript.txt"):
        return False
    return True


def first_summary_line(text: str) -> str:
    """First non-empty line under a `## Summary` heading, for the index description."""
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.strip().lower() == "## summary":
            for follow in lines[i + 1:]:
                if follow.strip():
                    return follow.strip()
            break
    return ""


def parse_note(path: Path) -> dict:
    """Return {title, url, added, summary} — url/added/summary may be empty for plain notes."""
    title = path.stem.replace("_", " ").strip()
    url = added = None
    summary = ""
    if path.suffix.lower() == ".md":
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            text = ""
        lines = text.splitlines()
        if lines and lines[0].lstrip("#").strip():
            title = lines[0].lstrip("#").strip()
        m = META_RE.search(text)
        if m:
            url = m.group(1).strip()
            added = m.group(3).strip()
        summary = first_summary_line(text)
    return {"title": title, "url": url, "added": added, "summary": summary, "path": path}


def cell(text: str, limit: int = 140) -> str:
    """Make a string safe for a markdown table cell (escape pipes, collapse, truncate)."""
    text = " ".join(text.split()).replace("|", "\\|")
    if len(text) > limit:
        text = text[: limit - 1].rstrip() + "…"
    return text or "—"


def md_link(text: str, target: Path | str) -> str:
    href = quote(str(target).replace("\\", "/"), safe="/")
    return f"[{text}]({href})"


def collect_notes(folder: Path) -> list[dict]:
    notes = [
        parse_note(p)
        for p in sorted(folder.rglob("*"))
        if p.is_file() and is_note(p) and not is_hidden(p, folder)
    ]
    notes.sort(key=lambda n: n["path"].as_posix().lower())
    return notes


def write_course_index(folder: Path, notes: list[dict]) -> None:
    lines = [
        f"# {folder.name}",
        "",
        "Auto-generated by `scripts/update_index.py`. Do not edit by hand.",
        "",
        "| # | Note | Description | Added | Source |",
        "|---|------|-------------|-------|--------|",
    ]
    for i, n in enumerate(notes, start=1):
        rel = n["path"].relative_to(folder).as_posix()
        note_link = md_link(cell(n["title"]), rel)
        desc = cell(n["summary"])
        # Relative file paths get URL-encoded (spaces); external URLs are used verbatim.
        src = f"[link]({n['url']})" if n["url"] else "—"
        lines.append(f"| {i:02d} | {note_link} | {desc} | {n['added'] or '—'} | {src} |")
    (folder / "INDEX.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_master_index(sections: list[tuple[Path, list[dict]]]) -> None:
    lines = [
        "# AI-Learning — Index",
        "",
        "Auto-generated by `scripts/update_index.py`. Do not edit by hand.",
        "",
        "| Category | Description | Notes | Last Updated |",
        "|----------|-------------|-------|--------------|",
    ]
    for folder, notes in sorted(sections, key=lambda s: s[0].name.lower()):
        dates = [n["added"] for n in notes if n["added"]]
        last = max(dates) if dates else "—"
        link = md_link(folder.name, f"{folder.name}/INDEX.md")
        desc = cell(CATEGORY_DESCRIPTIONS.get(folder.name, ""))
        lines.append(f"| {link} | {desc} | {len(notes)} | {last} |")
    if not sections:
        lines.append("| _no notes yet_ | — | 0 | — |")
    (ROOT / "INDEX.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    sections: list[tuple[Path, list[dict]]] = []
    for child in sorted(ROOT.iterdir()):
        if not child.is_dir() or child.name in EXCLUDE_DIRS or child.name.startswith("."):
            continue
        notes = collect_notes(child)
        if not notes:
            continue
        write_course_index(child, notes)
        sections.append((child, notes))
    write_master_index(sections)
    total = sum(len(n) for _, n in sections)
    print(f"Updated indexes: {len(sections)} course(s), {total} note(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
