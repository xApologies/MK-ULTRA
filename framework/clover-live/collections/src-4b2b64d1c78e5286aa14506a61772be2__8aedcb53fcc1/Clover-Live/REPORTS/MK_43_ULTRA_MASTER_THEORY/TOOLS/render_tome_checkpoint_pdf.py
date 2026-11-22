from __future__ import annotations

import argparse
import hashlib
import html
import importlib.util
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


ROOT = Path(__file__).resolve().parents[3]
WORKSPACE = ROOT / "REPORTS/MK_43_ULTRA_MASTER_THEORY"
SOURCE_RENDERER = ROOT / "MODEL/LIVE_MODEL/LIBRARY/recovery_08m/render_clover_mk43_gravity_scientific_pdf.py"
BATCH_CONFIG = {
    "V01_C02_C03": {
        "chapters": [
            WORKSPACE / "VOLUME_01_FOUNDATIONS/V01_C02_DISTINCTION_INFORMATION_AND_STRUCTURAL_REALITY.md",
            WORKSPACE / "VOLUME_01_FOUNDATIONS/V01_C03_CHIRALITY_AS_ORGANIZED_DIFFERENCE.md",
        ],
        "pdf": WORKSPACE / "VOLUME_01_FOUNDATIONS/MK_ULTRA_TOME_CHECKPOINT_V01_C02_C03.pdf",
        "subtitle": "Chapters 2-3 | Distinction, Information, Structural Reality, and Chirality",
        "subject": "Foundations: distinction, structural information, and chirality",
    },
    "V01_C04_C05": {
        "chapters": [
            WORKSPACE / "VOLUME_01_FOUNDATIONS/V01_C04_RECURSION_INHERITANCE_AND_PERSISTENCE.md",
            WORKSPACE / "VOLUME_01_FOUNDATIONS/V01_C05_ER_FOAM_AND_PRE_GEOMETRIC_CONNECTIVITY.md",
        ],
        "pdf": WORKSPACE / "VOLUME_01_FOUNDATIONS/MK_ULTRA_TOME_CHECKPOINT_V01_C04_C05.pdf",
        "subtitle": "Chapters 4-5 | Recursion, Inheritance, Persistence, and ER Foam",
        "subject": "Foundations: recursion, persistence, and pre-geometric connectivity",
    },
    "V01_C06_C07": {
        "chapters": [
            WORKSPACE / "VOLUME_01_FOUNDATIONS/V01_C06_PLANCK_LANDSCAPE_AND_FOUNDATIONAL_GEOMETRY.md",
            WORKSPACE / "VOLUME_01_FOUNDATIONS/V01_C07_PROJECTION_TRANSDUCTION_AND_REALIZATION.md",
        ],
        "pdf": WORKSPACE / "VOLUME_01_FOUNDATIONS/MK_ULTRA_TOME_CHECKPOINT_V01_C06_C07.pdf",
        "subtitle": "Chapters 6-7 | Planck Landscape, Geometry, Projection, and Realization",
        "subject": "Foundations: Planck-scale geometry and downstream realization",
    },
    "V01_C08": {
        "chapters": [
            WORKSPACE / "VOLUME_01_FOUNDATIONS/V01_C08_CONSERVATION_ACROSS_REPRESENTATIONAL_LEVELS.md",
        ],
        "pdf": WORKSPACE / "VOLUME_01_FOUNDATIONS/MK_ULTRA_TOME_CHECKPOINT_V01_C08_VOLUME_I_COMPLETE.pdf",
        "subtitle": "Chapter 8 | Conservation Across Representational Levels | Volume I Complete",
        "subject": "Foundations: conservation across representation and completion of Volume I",
    },
}


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


register_style = ParagraphStyle(
    "AddressRegister",
    parent=base.small_style,
    fontSize=5.8,
    leading=7.0,
    alignment=TA_LEFT,
    splitLongWords=True,
    wordWrap="CJK",
)

original_table_block = base.table_block


def register_table(lines: list[str]) -> list[object]:
    rows: list[list[Paragraph]] = []
    for line in lines:
        protected = line.strip().strip("|").replace(r"\|", "__PIPE__")
        cells = [cell.strip().replace("__PIPE__", r"\|") for cell in protected.split("|")]
        if all(set(cell or "-") <= set("-: ") for cell in cells):
            continue
        rows.append([base.paragraph(cell, register_style) for cell in cells])
    if len(rows[0]) != 5 or rows[0][0].getPlainText() != "API handle":
        return original_table_block(lines)
    table = Table(rows, colWidths=[1.12 * inch, 1.78 * inch, 0.55 * inch, 1.08 * inch, 2.47 * inch], repeatRows=1)
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#DDEBF0")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.HexColor("#12334A")),
                ("GRID", (0, 0), (-1, -1), 0.22, colors.HexColor("#B5C8CF")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 2),
                ("RIGHTPADDING", (0, 0), (-1, -1), 2),
                ("TOPPADDING", (0, 0), (-1, -1), 2),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
            ]
        )
    )
    return [table]


base.table_block = register_table


def page_decor(canvas, doc) -> None:
    canvas.saveState()
    width, height = letter
    canvas.setStrokeColor(colors.HexColor("#B7CCD4"))
    canvas.setLineWidth(0.4)
    canvas.line(0.7 * inch, height - 0.52 * inch, width - 0.7 * inch, height - 0.52 * inch)
    canvas.setFont(base.BODY, 7.4)
    canvas.setFillColor(colors.HexColor("#607783"))
    canvas.drawString(0.7 * inch, height - 0.39 * inch, "MK ULTRA - MASTER THEORY - VOLUME I CHECKPOINT")
    canvas.drawRightString(width - 0.7 * inch, 0.42 * inch, f"Page {doc.page}")
    canvas.restoreState()


def clean_markdown(text: str) -> str:
    return (
        text.replace("â€”", "-").replace("â€“", "-").replace("â€‘", "-")
        .replace("\n\\[\n", "\n$$\n").replace("\n\\]\n", "\n$$\n")
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch", choices=sorted(BATCH_CONFIG), default="V01_C02_C03")
    args = parser.parse_args()
    config = BATCH_CONFIG[args.batch]
    chapters = config["chapters"]
    pdf = config["pdf"]
    story: list[object] = [
        Spacer(1, 1.3 * inch),
        base.paragraph("MK ULTRA", base.title_style),
        base.paragraph("MASTER THEORY - VOLUME I CHECKPOINT", base.h1_style),
        base.paragraph(config["subtitle"], base.subtitle_style),
        Spacer(1, 0.28 * inch),
        base.paragraph(
            "A resumable publication checkpoint generated from Library 4.1 through Runtime -> BRANE -> API/QMO -> Library 4.1. "
            "Evidence classes and local formal qualifications are preserved in the chapter text.",
            base.body_style,
        ),
        PageBreak(),
    ]
    for index, path in enumerate(chapters):
        markdown = clean_markdown(path.read_text(encoding="utf-8"))
        chapter_story = base.parse_markdown(markdown)
        # Each chapter starts with its own volume heading; retain it but avoid the base renderer's title-page spacer.
        if chapter_story and isinstance(chapter_story[0], Spacer):
            while chapter_story and isinstance(chapter_story[0], Spacer):
                chapter_story.pop(0)
        if len(chapter_story) > 1 and isinstance(chapter_story[1], Paragraph):
            chapter_story[1] = base.paragraph(
                "A foundational synthesis from the validated Library 4.1 address space",
                base.subtitle_style,
            )
        story.extend(chapter_story)
        if index + 1 < len(chapters):
            story.append(PageBreak())

    doc = SimpleDocTemplate(
        str(pdf),
        pagesize=letter,
        rightMargin=0.72 * inch,
        leftMargin=0.72 * inch,
        topMargin=0.68 * inch,
        bottomMargin=0.85 * inch,
        title=f"MK Ultra - Master Theory - Volume I Checkpoint - {args.batch}",
        author="Clover",
        subject=config["subject"],
    )
    doc.build(story, onFirstPage=page_decor, onLaterPages=page_decor)
    print(f"{pdf}\n{pdf.stat().st_size}\n{sha256(pdf)}")


if __name__ == "__main__":
    main()
