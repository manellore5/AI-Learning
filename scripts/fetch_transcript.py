"""Fetch a YouTube video's transcript.

Tries English captions via yt-dlp first; falls back to downloading audio
and transcribing with faster-whisper.

Outputs to <workdir>:
  - transcript.txt   plain-text transcript
  - title.txt        video title
  - chapters.json    chapter markers (only if the video has chapters)
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path


def run(cmd: list[str], check: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, check=check, capture_output=True, text=True, encoding="utf-8", errors="replace")


def get_metadata(url: str) -> dict:
    proc = run(["yt-dlp", "--dump-single-json", "--skip-download", url])
    return json.loads(proc.stdout)


def try_captions(url: str, workdir: Path) -> Path | None:
    """Try to fetch English captions. Returns path to transcript.txt or None."""
    out_pattern = str(workdir / "subs.%(ext)s")
    proc = run(
        [
            "yt-dlp",
            "--write-auto-sub",
            "--write-sub",
            "--sub-lang", "en,en-US,en-GB",
            "--sub-format", "vtt/srt/best",
            "--skip-download",
            "--convert-subs", "srt",
            "-o", out_pattern,
            url,
        ],
        check=False,
    )
    if proc.returncode != 0:
        return None

    srt_files = list(workdir.glob("*.srt"))
    if not srt_files:
        return None

    text = srt_to_text(srt_files[0].read_text(encoding="utf-8", errors="replace"))
    if not text.strip():
        return None

    transcript_path = workdir / "transcript.txt"
    transcript_path.write_text(text, encoding="utf-8")
    return transcript_path


def srt_to_text(srt: str) -> str:
    lines = []
    for raw in srt.splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.isdigit():
            continue
        if "-->" in line:
            continue
        line = re.sub(r"<[^>]+>", "", line)
        lines.append(line)
    deduped = []
    for line in lines:
        if not deduped or deduped[-1] != line:
            deduped.append(line)
    return "\n".join(deduped) + "\n"


def transcribe_audio(url: str, workdir: Path, whisper_model: str) -> Path:
    """Download audio with yt-dlp and transcribe via faster-whisper."""
    audio_template = str(workdir / "audio.%(ext)s")
    run(
        [
            "yt-dlp",
            "-x",
            "--audio-format", "mp3",
            "-o", audio_template,
            url,
        ]
    )
    audio_files = list(workdir.glob("audio.*"))
    if not audio_files:
        raise RuntimeError("yt-dlp did not produce an audio file")
    audio_path = audio_files[0]

    from faster_whisper import WhisperModel

    print(f"[fetch_transcript] Loading whisper model '{whisper_model}' (first run downloads it)...", file=sys.stderr)
    model = WhisperModel(whisper_model, device="cpu", compute_type="int8")
    print(f"[fetch_transcript] Transcribing {audio_path.name}...", file=sys.stderr)
    segments, _ = model.transcribe(str(audio_path), beam_size=1)

    transcript_path = workdir / "transcript.txt"
    with transcript_path.open("w", encoding="utf-8") as fh:
        for seg in segments:
            fh.write(seg.text.strip() + "\n")
    return transcript_path


def write_chapters(meta: dict, workdir: Path) -> Path | None:
    chapters = meta.get("chapters") or []
    if not chapters:
        return None
    path = workdir / "chapters.json"
    path.write_text(json.dumps(chapters, indent=2), encoding="utf-8")
    return path


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("url")
    ap.add_argument("--workdir", required=True, help="Directory to write transcript.txt, title.txt, chapters.json")
    ap.add_argument("--whisper-model", default="base", help="faster-whisper model size (tiny/base/small/medium)")
    args = ap.parse_args()

    if not shutil.which("yt-dlp"):
        print("ERROR: yt-dlp not found on PATH. Run: pip install -r requirements.txt", file=sys.stderr)
        return 2

    workdir = Path(args.workdir)
    workdir.mkdir(parents=True, exist_ok=True)

    print(f"[fetch_transcript] Fetching metadata for {args.url}", file=sys.stderr)
    meta = get_metadata(args.url)
    title = meta.get("title") or "untitled"
    (workdir / "title.txt").write_text(title, encoding="utf-8")
    duration = meta.get("duration") or 0
    write_chapters(meta, workdir)

    print("[fetch_transcript] Trying captions...", file=sys.stderr)
    transcript = try_captions(args.url, workdir)
    if transcript is None:
        print("[fetch_transcript] No captions found, transcribing audio...", file=sys.stderr)
        transcript = transcribe_audio(args.url, workdir, args.whisper_model)

    summary = {
        "title": title,
        "duration_seconds": duration,
        "transcript": str(transcript),
        "chapters": str(workdir / "chapters.json") if (workdir / "chapters.json").exists() else None,
        "captions_used": transcript.name == "transcript.txt" and (workdir / "audio.mp3").exists() is False,
    }
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
