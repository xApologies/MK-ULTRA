from __future__ import annotations

import hashlib
import importlib.util
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate


ROOT = Path(__file__).resolve().parents[3]
SOURCE_RENDERER = ROOT / "MODEL/LIVE_MODEL/LIBRARY/recovery_08m/render_clover_mk43_gravity_scientific_pdf.py"
MD = ROOT / "REPORTS/MK_43_ULTRA_MASTER_THEORY/VOLUME_01_FOUNDATIONS/V01_C01_WHAT_IS_MK_43_ULTRA.md"
PDF = ROOT / "REPORTS/MK_43_ULTRA_MASTER_THEORY/VOLUME_01_FOUNDATIONS/V01_C01_WHAT_IS_MK_43_ULTRA.pdf"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(4 * 1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


spec = importlib.util.spec_from_file_location("clover_pdf_base", SOURCE_RENDERER)
if spec is None or spec.loader is None:
    raise RuntimeError("could not load the validated Clover PDF renderer")
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)


def page_decor(canvas, doc) -> None:
    canvas.saveState()
    width, height = letter
    canvas.setStrokeColor(colors.HexColor("#B7CCD4"))
    canvas.setLineWidth(0.4)
    canvas.line(0.7 * inch, height - 0.52 * inch, width - 0.7 * inch, height - 0.52 * inch)
    canvas.setFont(base.BODY, 7.4)
    canvas.setFillColor(colors.HexColor("#607783"))
    canvas.drawString(0.7 * inch, height - 0.39 * inch, "MK 43 ULTRA - MASTER THEORY REPORT - VOLUME I")
    canvas.drawRightString(width - 0.7 * inch, 0.42 * inch, f"Page {doc.page}")
    canvas.restoreState()


def main() -> None:
    markdown = MD.read_text(encoding="utf-8")
    # PDF skill convention: avoid non-ASCII dash glyphs while preserving the Markdown source.
    markdown = markdown.replace("—", "-").replace("–", "-").replace("‑", "-")
    markdown = markdown.replace("\n\\[\n", "\n$$\n").replace("\n\\]\n", "\n$$\n")
    story = base.parse_markdown(markdown)
    if len(story) >= 3:
        story[2] = base.paragraph(
            "Volume I - Foundations | Chapter 1 - What Is MK 43 Ultra?",
            base.subtitle_style,
        )
    doc = SimpleDocTemplate(
        str(PDF),
        pagesize=letter,
        rightMargin=0.72 * inch,
        leftMargin=0.72 * inch,
        topMargin=0.68 * inch,
        bottomMargin=0.85 * inch,
        title="MK 43 Ultra - Master Theory Report - Volume I - Chapter 1",
        author="Clover",
        subject="Foundational scientific exposition of MK 43 Ultra from Library 4.1",
    )
    doc.build(story, onFirstPage=page_decor, onLaterPages=page_decor)
    print(f"{PDF}\n{PDF.stat().st_size}\n{sha256(PDF)}")


if __name__ == "__main__":
    main()
