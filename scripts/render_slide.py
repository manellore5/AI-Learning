"""Render slide page(s) from a PDF cropped to the DIAGRAM content — dropping the
title block (redundant with the Anki card front) and the watermark/footer chrome.

Used by the /anki skill to attach clean diagram images from slide decks. The crop
is the bounding box of all images + non-chrome, non-title text blocks, so it never
cuts diagram content; it only trims the heading and page furniture.

Usage:
    python scripts/render_slide.py deck.pdf --pages 49,58,61 --out-dir media --prefix mydeck
    python scripts/render_slide.py deck.pdf --pages 49 --out-dir media --prefix d --keep-title

Outputs <out-dir>/<prefix>-p<page>.png for each page. PPTX decks: convert to PDF
first (e.g. `soffice --headless --convert-to pdf deck.pptx`) and pass that PDF.

Requires PyMuPDF (fitz): pip install pymupdf
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

# Footer / watermark text fragments to exclude from the crop box (lowercased).
DEFAULT_CHROME = ("not for distribution",)


def parse_pages(spec: str) -> list[int]:
    pages: list[int] = []
    for part in spec.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            a, b = part.split("-", 1)
            pages.extend(range(int(a), int(b) + 1))
        else:
            pages.append(int(part))
    return pages


def content_box(page, chrome: tuple[str, ...], keep_title: bool):
    import fitz

    d = page.get_text("dict")
    tblocks = []
    for b in d["blocks"]:
        if b.get("type") != 0:  # text blocks only
            continue
        txt = "".join(s["text"] for ln in b["lines"] for s in ln["spans"])
        if not txt.strip() or any(c in txt.lower() for c in chrome):
            continue
        size = max((s["size"] for ln in b["lines"] for s in ln["spans"]), default=0)
        tblocks.append((fitz.Rect(b["bbox"]), size))

    gmax = max((s for _, s in tblocks), default=0)
    box = fitz.Rect()
    for r, size in tblocks:
        # The largest-font block(s) are the slide title — drop unless --keep-title.
        if not keep_title and size >= gmax - 1.5:
            continue
        box |= r
    for img in page.get_images(full=True):
        for r in page.get_image_rects(img[0]):
            box |= r
    return box


def main() -> int:
    ap = argparse.ArgumentParser(description="Render title-less slide diagram crops from a PDF.")
    ap.add_argument("pdf")
    ap.add_argument("--pages", required=True, help="e.g. '49,58,61' or '46-75'")
    ap.add_argument("--out-dir", required=True)
    ap.add_argument("--prefix", required=True, help="output filename prefix")
    ap.add_argument("--scale", type=float, default=2.0, help="render scale (2.0 ~= 144 dpi)")
    ap.add_argument("--keep-title", action="store_true", help="keep the slide title in the crop")
    ap.add_argument("--chrome", default=",".join(DEFAULT_CHROME),
                    help="comma-separated footer/watermark fragments to exclude")
    args = ap.parse_args()

    try:
        import fitz
    except ModuleNotFoundError:
        print("ERROR: PyMuPDF missing. Run: pip install pymupdf", file=sys.stderr)
        return 3

    src = Path(args.pdf)
    if not src.exists():
        print(f"ERROR: file not found: {src}", file=sys.stderr)
        return 2

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    chrome = tuple(c.strip().lower() for c in args.chrome.split(",") if c.strip())

    doc = fitz.open(str(src))
    written = []
    for pno in parse_pages(args.pages):
        if not (1 <= pno <= doc.page_count):
            print(f"skip p{pno}: out of range (1-{doc.page_count})", file=sys.stderr)
            continue
        page = doc.load_page(pno - 1)
        box = content_box(page, chrome, args.keep_title)
        if box.is_empty:
            print(f"skip p{pno}: no content found", file=sys.stderr)
            continue
        box += (-8, -8, 8, 8)
        box &= page.rect
        pix = page.get_pixmap(matrix=fitz.Matrix(args.scale, args.scale), clip=box)
        out = out_dir / f"{args.prefix}-p{pno}.png"
        pix.save(str(out))
        written.append(str(out))
        print(f"p{pno}: {pix.width}x{pix.height}px -> {out}")

    if not written:
        print("ERROR: nothing rendered", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
