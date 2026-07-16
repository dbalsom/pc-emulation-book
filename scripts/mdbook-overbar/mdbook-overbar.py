#!/usr/bin/env python3
import json
import re
import sys

TOKEN_RE = re.compile(r"(?<![A-Za-z0-9_])/(?P<name>[A-Z0-9_]*[A-Z][A-Z0-9_]*)(?![A-Za-z0-9_])")
FENCE_RE = re.compile(r"^\s*(`{3,}|~{3,})")
HTML_LINE_RE = re.compile(r"^\s*</?[A-Za-z][^>]*(?:>|$)")
COMMENT_LINE_RE = re.compile(r"^\s*<!--")
HTML_ELEMENT_RE = re.compile(r"<([A-Za-z][A-Za-z0-9:-]*)(?:\s[^>]*)?>.*?</\1>")
HTML_TAG_RE = re.compile(r"<!--.*?-->|<[^>]+>")
MARKDOWN_LINK_RE = re.compile(r"!?\[[^\]\n]*\]\([^)\n]*\)")
URL_RE = re.compile(r"https?://[^\s<>)]+")


def mask_range(mask, start, end):
    for idx in range(start, min(end, len(mask))):
        mask[idx] = True


def mask_pattern(mask, pattern, line):
    for match in pattern.finditer(line):
        mask_range(mask, match.start(), match.end())


def mask_inline_code(mask, line):
    pos = 0
    while pos < len(line):
        if line[pos] != "`":
            pos += 1
            continue

        end_ticks = pos + 1
        while end_ticks < len(line) and line[end_ticks] == "`":
            end_ticks += 1

        ticks = line[pos:end_ticks]
        closing = line.find(ticks, end_ticks)
        if closing == -1:
            mask_range(mask, pos, len(line))
            return

        mask_range(mask, pos, closing + len(ticks))
        pos = closing + len(ticks)


def protected_mask(line):
    mask = [False] * len(line)
    mask_pattern(mask, URL_RE, line)
    mask_pattern(mask, MARKDOWN_LINK_RE, line)
    mask_pattern(mask, HTML_ELEMENT_RE, line)
    mask_pattern(mask, HTML_TAG_RE, line)
    mask_inline_code(mask, line)
    return mask


def rewrite_overbar_tokens(line):
    mask = protected_mask(line)
    parts = []
    last = 0

    for match in TOKEN_RE.finditer(line):
        if any(mask[match.start():match.end()]):
            continue

        name = match.group("name")
        parts.append(line[last:match.start()])
        parts.append(f'<span class="pcbook-overbar">{name}</span>')
        last = match.end()

    if not parts:
        return line

    parts.append(line[last:])
    return "".join(parts)


def process_content(content):
    lines = content.split("\n")
    new_lines = []
    in_fence = False
    in_html_tag = False
    in_html_comment = False
    fence_char = ""
    fence_len = 0

    for line in lines:
        fence_match = FENCE_RE.match(line)
        if fence_match:
            fence = fence_match.group(1)
            if not in_fence:
                in_fence = True
                fence_char = fence[0]
                fence_len = len(fence)
            elif fence[0] == fence_char and len(fence) >= fence_len:
                in_fence = False

            new_lines.append(line)
            continue

        if in_html_comment:
            new_lines.append(line)
            if "-->" in line:
                in_html_comment = False
            continue

        if in_html_tag:
            new_lines.append(line)
            if ">" in line:
                in_html_tag = False
            continue

        if in_fence:
            new_lines.append(line)
            continue

        if COMMENT_LINE_RE.match(line):
            new_lines.append(line)
            if "-->" not in line:
                in_html_comment = True
            continue

        if HTML_LINE_RE.match(line):
            new_lines.append(line)
            if ">" not in line:
                in_html_tag = True
            continue

        new_lines.append(rewrite_overbar_tokens(line))

    return "\n".join(new_lines)


def process_chapter(chapter_data):
    chapter_data["content"] = process_content(chapter_data.get("content", ""))

    for sub_item in chapter_data.get("sub_items", []):
        if "Chapter" in sub_item:
            process_chapter(sub_item["Chapter"])

    return chapter_data


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "supports":
        sys.exit(0)

    try:
        data = json.load(sys.stdin)
    except Exception as e:
        sys.stderr.write(f"Error loading JSON from stdin: {e}\n")
        sys.exit(1)

    if isinstance(data, list):
        book = data[1]
    elif isinstance(data, dict):
        book = data["book"]
    else:
        sys.stderr.write(f"Input is unknown type: {type(data)}\n")
        sys.exit(1)

    for section in book["items"]:
        if "Chapter" in section:
            process_chapter(section["Chapter"])

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    print(json.dumps(book, ensure_ascii=False))


if __name__ == "__main__":
    if sys.platform == "win32":
        sys.stdin.reconfigure(encoding="utf-8")
        sys.stdout.reconfigure(encoding="utf-8")
    main()
