"""Render Mermaid diagram source to a PNG/SVG via the kroki.io web service.

Used by the /anki skill when a source has no usable embedded diagram and
Claude authors a Mermaid graph instead — Anki can't render Mermaid, so we
turn it into an image kroki returns, then store it as Anki media.

Stdlib only (urllib) — no pip dependency. Needs internet access; the diagram
source is POSTed to https://kroki.io.

Usage:
    python scripts/render_mermaid.py --src diagram.mmd --out media/topic.png
    echo "graph TD; A-->B" | python scripts/render_mermaid.py --out media/topic.png
"""
from __future__ import annotations

import argparse
import sys
import urllib.error
import urllib.request
from pathlib import Path

KROKI = "https://kroki.io/mermaid"


def render(source: str, fmt: str, timeout: int) -> bytes:
    url = f"{KROKI}/{fmt}"
    req = urllib.request.Request(
        url,
        data=source.encode("utf-8"),
        headers={
            "Content-Type": "text/plain",
            "Accept": f"image/{fmt}",
            # kroki.io sits behind Cloudflare, which 403s the default
            # "Python-urllib" agent. A normal browser UA passes the bot check.
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


def main() -> int:
    ap = argparse.ArgumentParser(description="Render Mermaid to an image via kroki.io.")
    ap.add_argument("--src", help="Mermaid source file (defaults to stdin)")
    ap.add_argument("--out", required=True, help="Output image path (e.g. media/topic.png)")
    ap.add_argument("--format", default="png", choices=["png", "svg"], help="Output format")
    ap.add_argument("--timeout", type=int, default=30, help="HTTP timeout in seconds")
    ap.add_argument(
        "--background",
        default="#ffffff",
        help="Opaque background injected into SVG output so default-theme text "
        "stays visible on dark pages (pass 'none' to keep it transparent)",
    )
    args = ap.parse_args()

    source = Path(args.src).read_text(encoding="utf-8") if args.src else sys.stdin.read()
    if not source.strip():
        print("ERROR: empty Mermaid source.", file=sys.stderr)
        return 2

    try:
        data = render(source, args.format, args.timeout)
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", "replace")[:500]
        print(f"ERROR: kroki returned {exc.code}: {body}", file=sys.stderr)
        return 3
    except urllib.error.URLError as exc:
        print(f"ERROR: could not reach kroki.io ({exc.reason}). Check internet.", file=sys.stderr)
        return 4

    if args.format == "svg" and args.background.lower() != "none":
        # kroki SVGs are transparent; mermaid's default theme assumes a light
        # page, so dark text disappears in dark-mode viewers without this.
        svg_text = data.decode("utf-8")
        svg_text = svg_text.replace(
            "<svg", f'<svg style="background-color:{args.background}"', 1
        )
        data = svg_text.encode("utf-8")

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(data)
    print(str(out.resolve()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
