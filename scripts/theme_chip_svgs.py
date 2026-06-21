#!/usr/bin/env python3
# cspell:words rglob
"""Rewrite chip SVG pin labels so they respond to light and dark CSS themes."""

from __future__ import annotations

import argparse
import re
import sys
from collections.abc import Iterable
from pathlib import Path
from string import Template
from textwrap import dedent

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SVG_DIR = REPO_ROOT / "src" / "images" / "chips"
THEME_STYLE_ID = "pc-book-chip-theme"
PIN_LABEL_CLASS = "pc-book-chip-pin-label"
PIN_LABEL_LIGHT = "#1f2937"
PIN_LABEL_DARK = "#e5e7eb"

_THEME_STYLE_TEMPLATE = Template(
    dedent(
        """\
        <style id="$style_id" type="text/css"><![CDATA[
        svg {
          color-scheme: light dark;
        }

        .$pin_label_class {
          fill: $pin_label_light;
        }

        @media (prefers-color-scheme: dark) {
          .$pin_label_class {
            fill: $pin_label_dark;
          }
        }
        ]]></style>"""
    )
)

SVG_OPEN_RE = re.compile(r"(<svg\b[^>]*>)", re.IGNORECASE)
THEME_STYLE_RE = re.compile(
    rf"\s*<style\b[^>]*\bid=[\"']{re.escape(THEME_STYLE_ID)}[\"'][^>]*>.*?</style>",
    re.IGNORECASE | re.DOTALL,
)
TEXT_TAG_RE = re.compile(r"<text\b(?P<attrs>[^>]*)>", re.IGNORECASE)
STYLE_ATTR_RE = re.compile(r'(?P<prefix>\bstyle\s*=\s*")(?P<style>[^"]*)(?P<suffix>")')
CLASS_ATTR_RE = re.compile(r'(?P<prefix>\bclass\s*=\s*")(?P<class_names>[^"]*)(?P<suffix>")')
FILL_DECL_RE = re.compile(r"(^|;)\s*fill\s*:[^;]*;?", re.IGNORECASE)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Embed light/dark theme variables in chip SVGs and apply them to "
            "outer pin labels."
        )
    )
    parser.add_argument(
        "paths",
        nargs="*",
        help=(
            "SVG files or directories to update. Directories are searched "
            "recursively for *.svg files. Defaults to src/images/chips."
        ),
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the files that would change without writing them.",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Exit with status 1 if any SVG would be changed.",
    )
    return parser.parse_args(argv)


def find_svg_paths(raw_paths: Iterable[str] | None = None) -> list[Path]:
    paths = [Path(path) for path in raw_paths] if raw_paths else [DEFAULT_SVG_DIR]
    svg_paths: set[Path] = set()

    for path in paths:
        resolved = path.resolve()

        if resolved.is_dir():
            svg_paths.update(resolved.rglob("*.svg"))
        elif resolved.is_file() and resolved.suffix.lower() == ".svg":
            svg_paths.add(resolved)
        else:
            raise FileNotFoundError(f"No valid SVG file or directory found at: '{path}'")

    return sorted(svg_paths)


def build_theme_style() -> str:
    return _THEME_STYLE_TEMPLATE.substitute(
        style_id=THEME_STYLE_ID,
        pin_label_class=PIN_LABEL_CLASS,
        pin_label_light=PIN_LABEL_LIGHT,
        pin_label_dark=PIN_LABEL_DARK,
    )


def strip_theme_style(svg_text: str) -> str:
    return THEME_STYLE_RE.sub("", svg_text)


def insert_theme_style(svg_text: str) -> str:
    theme_style = build_theme_style()
    if not SVG_OPEN_RE.search(svg_text):
        raise ValueError("Could not find an opening <svg> tag")

    return SVG_OPEN_RE.sub(rf"\1{theme_style}", svg_text, count=1)


def is_outer_pin_label_style(style: str) -> bool:
    normalized = re.sub(r"\s+", "", style.lower())
    return (
        "font-family:'consolas',monospace" in normalized
        and "font-size:24px" in normalized
    )


def themed_label_style(style: str) -> str:
    style_without_fill = FILL_DECL_RE.sub(lambda match: ";" if match.group(1) else "", style)
    return re.sub(r";{2,}", ";", style_without_fill).strip()


def themed_label_attrs(attrs: str) -> str:
    class_match = CLASS_ATTR_RE.search(attrs)
    if class_match is None:
        return f'{attrs} class="{PIN_LABEL_CLASS}"'

    class_names = class_match.group("class_names").split()
    if PIN_LABEL_CLASS in class_names:
        return attrs

    class_names.append(PIN_LABEL_CLASS)
    return CLASS_ATTR_RE.sub(
        rf"\g<prefix>{' '.join(class_names)}\g<suffix>",
        attrs,
        count=1,
    )


def replace_text_tag(match: re.Match[str]) -> str:
    attrs = match.group("attrs")
    style_match = STYLE_ATTR_RE.search(attrs)
    if style_match is None:
        return match.group(0)

    style = style_match.group("style")
    if not is_outer_pin_label_style(style):
        return match.group(0)

    replacement_style = themed_label_style(style)
    replacement_attrs = STYLE_ATTR_RE.sub(
        rf"\g<prefix>{replacement_style}\g<suffix>",
        attrs,
        count=1,
    )
    replacement_attrs = themed_label_attrs(replacement_attrs)
    return f"<text{replacement_attrs}>"


def themed_svg(svg_text: str) -> str:
    without_theme = strip_theme_style(svg_text)
    rewritten = TEXT_TAG_RE.sub(replace_text_tag, without_theme)
    return insert_theme_style(rewritten)


def relpath(path: Path) -> str:
    if path.is_relative_to(REPO_ROOT):
        return path.relative_to(REPO_ROOT).as_posix()
    return str(path)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])

    try:
        svg_paths = find_svg_paths(args.paths)
    except FileNotFoundError as error:
        print(error, file=sys.stderr)
        return 2

    changed_paths: list[Path] = []

    for svg_path in svg_paths:
        original = svg_path.read_text(encoding="utf-8")
        try:
            rewritten = themed_svg(original)
        except ValueError as error:
            print(f"{relpath(svg_path)}: {error}", file=sys.stderr)
            return 2

        if rewritten == original:
            continue

        changed_paths.append(svg_path)
        if args.dry_run or args.check:
            print(f"would update {relpath(svg_path)}")
        else:
            svg_path.write_text(rewritten, encoding="utf-8")
            print(f"updated {relpath(svg_path)}")

    if args.check and changed_paths:
        return 1

    if not changed_paths:
        print("No changes needed.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
