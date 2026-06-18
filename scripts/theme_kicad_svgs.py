#!/usr/bin/env python3
# cspell:words KiCad rglob
"""Rewrite KiCad schematic SVGs so they respond to light and dark CSS themes."""

from __future__ import annotations

import argparse
import re
import sys
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path
from string import Template
from textwrap import dedent

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SVG_DIR = REPO_ROOT / "src" / "images" / "schematics"
THEME_STYLE_ID = "pc-book-schematic-theme"

_THEME_STYLE_TEMPLATE = Template(
    dedent(
        """\
        <style id="$style_id" type="text/css"><![CDATA[
        svg {
          color-scheme: light dark;
        $light_vars
        }

        @media (prefers-color-scheme: dark) {
          svg {
        $dark_vars
          }
        }
        ]]></style>"""
    )
)

@dataclass(frozen=True)
class ColorRole:
    name: str
    light: str
    dark: str

    @property
    def variable(self) -> str:
        return f"--pc-book-schematic-{self.name}"


COLOR_ROLES = {
    "#fff": ColorRole("background-mask", "#ffffff", "#1f1f1f"),
    "#840000": ColorRole("wire", "#840000", "#ff8c8c"),
    "#a90000": ColorRole("pin-number", "#a90000", "#ff7373"),
    "#006464": ColorRole("label", "#006464", "#5ed8d8"),
    "#0000c2": ColorRole("blue-label", "#0000c2", "#95a8ff"),
    "#000084": ColorRole("dark-blue-label", "#000084", "#7f95ff"),
    "#009600": ColorRole("junction", "#009600", "#63d66a"),
    "#725600": ColorRole("brown-label", "#725600", "#d3bd73"),
    "#ffffc2": ColorRole("component-fill", "#ffffc2", "#3a3624"),
}

COLOR_ALIASES = {
    "#ffffff": "#fff",
}

KNOWN_COLORS = set(COLOR_ROLES) | set(COLOR_ALIASES)

# Yes, regex XML parsing. The horror. Avert your eyes...
# TODO: rewrite with xml.etree.ElementTree
SVG_OPEN_RE = re.compile(r"(<svg\b[^>]*>)", re.IGNORECASE)
THEME_STYLE_RE = re.compile(
    rf"\s*<style\b[^>]*\bid=[\"']{re.escape(THEME_STYLE_ID)}[\"'][^>]*>.*?</style>",
    re.IGNORECASE | re.DOTALL,
)
STYLE_COLOR_RE = re.compile(
    r"(?P<prefix>\b(?:fill|stroke)\s*:\s*)"
    r"(?P<color>#[0-9a-f]{3}(?:[0-9a-f]{3})?)(?P<suffix>\b)",
    re.IGNORECASE,
)
ATTRIBUTE_COLOR_RE = re.compile(
    r"(?P<prefix>\b(?:fill|stroke)\s*=\s*[\"'])"
    r"(?P<color>#[0-9a-f]{3}(?:[0-9a-f]{3})?)(?P<suffix>[\"'])",
    re.IGNORECASE,
)
HEX_COLOR_RE = re.compile(r"#[0-9a-f]{3}(?:[0-9a-f]{3})?\b", re.IGNORECASE)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Replace KiCad schematic SVG fill/stroke colors with CSS variables and "
            "embed light/dark color definitions in each SVG."
        )
    )
    parser.add_argument(
        "paths",
        nargs="*",
        help=(
            "SVG files or directories to update. Directories are searched "
            "recursively for *.svg files. Defaults to src/images/schematics."
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
    parser.add_argument(
        "--fail-on-unknown-colors",
        action="store_true",
        help="Exit with status 1 if an SVG contains unrecognized hex colors.",
    )
    return parser.parse_args(argv)


def find_svg_paths(raw_paths: Iterable[str] | None = None) -> list[Path]:
    """
    Finds and resolves all SVG file paths from a list of strings representing 
    files or directories.
    """
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
    light_vars = "\n".join(
        f"  {role.variable}: {role.light};"
        for role in COLOR_ROLES.values()
    )
    dark_vars = "\n".join(
        f"    {role.variable}: {role.dark};"
        for role in COLOR_ROLES.values()
    )

    return _THEME_STYLE_TEMPLATE.substitute(
        style_id=THEME_STYLE_ID,
        light_vars=light_vars,
        dark_vars=dark_vars,
    )


def strip_theme_style(svg_text: str) -> str:
    return THEME_STYLE_RE.sub("", svg_text)


def replacement_for(color: str) -> str | None:
    normalized = color.lower()
    role = COLOR_ROLES.get(COLOR_ALIASES.get(normalized, normalized))
    if role is None:
        return None

    return f"var({role.variable}, {role.light})"


def replace_color_match(match: re.Match[str]) -> str:
    replacement = replacement_for(match.group("color"))
    if replacement is None:
        return match.group(0)

    return f"{match.group('prefix')}{replacement}{match.group('suffix')}"


def insert_theme_style(svg_text: str) -> str:
    theme_style = build_theme_style()
    if not SVG_OPEN_RE.search(svg_text):
        raise ValueError("Could not find an opening <svg> tag")

    return SVG_OPEN_RE.sub(rf"\1{theme_style}", svg_text, count=1)


def themed_svg(svg_text: str) -> tuple[str, list[str]]:
    without_theme = strip_theme_style(svg_text)
    unknown_colors = sorted(
        {
            color.lower()
            for color in HEX_COLOR_RE.findall(without_theme)
            if color.lower() not in KNOWN_COLORS
        }
    )

    rewritten = STYLE_COLOR_RE.sub(replace_color_match, without_theme)
    rewritten = ATTRIBUTE_COLOR_RE.sub(replace_color_match, rewritten)
    rewritten = insert_theme_style(rewritten)

    return rewritten, unknown_colors


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
    unknown_by_path: dict[Path, list[str]] = {}

    for svg_path in svg_paths:
        original = svg_path.read_text(encoding="utf-8")
        try:
            rewritten, unknown_colors = themed_svg(original)
        except ValueError as error:
            print(f"{relpath(svg_path)}: {error}", file=sys.stderr)
            return 2

        if unknown_colors:
            unknown_by_path[svg_path] = unknown_colors

        if rewritten == original:
            continue

        changed_paths.append(svg_path)
        if args.dry_run or args.check:
            print(f"would update {relpath(svg_path)}")
        else:
            svg_path.write_text(rewritten, encoding="utf-8")
            print(f"updated {relpath(svg_path)}")

    for svg_path, colors in unknown_by_path.items():
        color_list = ", ".join(colors)
        print(f"{relpath(svg_path)}: unknown colors: {color_list}", file=sys.stderr)

    if args.fail_on_unknown_colors and unknown_by_path:
        return 1

    if args.check and changed_paths:
        return 1

    if not changed_paths and not unknown_by_path:
        print("No changes needed.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())