from __future__ import annotations

import argparse
import math
from pathlib import Path

from PIL import Image, ImageDraw


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("page_directory", type=Path)
    parser.add_argument("--per-sheet", type=int, default=4)
    parser.add_argument("--page-width", type=int, default=580)
    args = parser.parse_args()
    pages = sorted(args.page_directory.glob("page-*.png"), key=lambda p: int(p.stem.split("-")[-1]))
    if not pages:
        raise RuntimeError("no rendered PDF pages found")
    output = args.page_directory / "contact_sheets"
    output.mkdir(exist_ok=True)
    columns = 2
    rows = math.ceil(args.per_sheet / columns)
    for sheet_index in range(math.ceil(len(pages) / args.per_sheet)):
        batch = pages[sheet_index * args.per_sheet : (sheet_index + 1) * args.per_sheet]
        rendered = []
        for page in batch:
            image = Image.open(page).convert("RGB")
            height = round(image.height * args.page_width / image.width)
            rendered.append((page, image.resize((args.page_width, height), Image.Resampling.LANCZOS)))
        cell_height = max(image.height for _, image in rendered) + 38
        sheet = Image.new("RGB", (columns * args.page_width + 30, rows * cell_height + 20), "#d8e0e3")
        draw = ImageDraw.Draw(sheet)
        for ordinal, (page, image) in enumerate(rendered):
            x = 10 + (ordinal % columns) * args.page_width
            y = 28 + (ordinal // columns) * cell_height
            sheet.paste(image, (x, y))
            draw.text((x, 7 + (ordinal // columns) * cell_height), f"PDF page {page.stem.split('-')[-1]}", fill="#17384a")
        target = output / f"sheet-{sheet_index + 1:02d}.png"
        sheet.save(target, optimize=True)
        print(target)


if __name__ == "__main__":
    main()
