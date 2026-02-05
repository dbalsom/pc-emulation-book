#!/usr/bin/env python3
import json
import sys
import os
try:
    import tomllib
except ImportError:
    import tomli as tomllib

from toml_bitfield import RegisterDef, render_svg, generate_md_table, StyleDef

# Read default CSS from sibling file
script_dir = os.path.dirname(os.path.realpath(__file__))
css_path = os.path.join(script_dir, "style.css")
DEFAULT_CSS = ""
if os.path.exists(css_path):
    try:
        with open(css_path, "r", encoding="utf-8") as f:
            DEFAULT_CSS = "<style>\n" + f.read() + "\n</style>"
    except Exception as e:
        sys.stderr.write(f"Warning: Could not read css file: {e}\n")

def process_chapter(chapter_data, exclude_files=None, config=None):
    """Recursively process chapter content to replace code blocks."""
    if exclude_files is None:
        exclude_files = []
    if config is None:
        config = {}

    content = chapter_data.get('content', '')
    path = chapter_data.get('source_path', chapter_data.get('path', ''))
    
    # Check if file should be excluded
    if path and any(path.endswith(f) for f in exclude_files):
        sys.stderr.write(f"Skipping excluded file: {path}\n")
        # Still must recurse for sub-items
        for sub_item in chapter_data.get('sub_items', []):
            if 'Chapter' in sub_item:
                process_chapter(sub_item['Chapter'], exclude_files)
        return chapter_data

    # Check for encoding issues in this chapter
    try:
        content.encode('utf-8')
    except UnicodeEncodeError:
        name = chapter_data.get('name', 'Unknown')
        path = chapter_data.get('source_path', chapter_data.get('path', 'Unknown'))
        sys.stderr.write(f"WARNING: Encoding issue (lone surrogates) detected in Chapter: '{name}' (File: {path})\n")

    # look for ```toml_bitfield and replace the block with SVG
    lines = content.split('\n')
    new_lines = []
    in_block = False
    block_lines = []
    found_bitfield = False
    
    for line in lines:
        if line.strip().startswith('```toml_bitfield'):
            in_block = True
            found_bitfield = True
            block_lines = []
            continue
            
        if in_block and line.strip().startswith('```'):
            in_block = False
            # Process the collected TOML block
            # Ensure clean newlines and trailing newline for parser
            clean_lines = [l.rstrip() for l in block_lines]
            toml_str = "\n".join(clean_lines) + "\n"
            
            try:
                # Parse the TOML and convert to a RegisterDef. 
                raw_data = tomllib.loads(toml_str)
                reg = RegisterDef.model_validate(raw_data)
                
                # Apply global style if loaded
                global_style = config.get('loaded_style', {})
                if global_style:
                    merged_style = reg.style.model_dump()
                    merged_style.update(global_style)
                    reg.style = StyleDef.model_validate(merged_style)
                
                # Read parameters from mdbook config
                table_format = config.get('table')
                style_override = config.get('style')
                render_svg_table = False

                if table_format == 'svg':
                    render_svg_table = True
                    
                # Render the SVG diagram
                svg_output = render_svg(reg, render_svg_table)
                
                # Wrap in anchor div if specified
                if reg.anchor:
                    svg_output = f'<div id="{reg.anchor}">{svg_output}</div>'
                
                # If Markdown table requested, generate and append it
                if table_format == 'md':
                     md_table = generate_md_table(reg)
                     svg_output += "\n\n" + md_table + "\n"
                
                new_lines.append(svg_output)
            except Exception as e:
                # Fallback: print error in place of SVG for debugging
                new_lines.append(f"<pre style='color:red'>Error rendering SVG: {e}</pre>")
            continue
            
        if in_block:
            block_lines.append(line)
        else:
            new_lines.append(line)
            
    chapter_data['content'] = "\n".join(new_lines)
    
    if found_bitfield:
        # Add CSS at the top, ensuring a blank line separates it from content
        # to prevent markdown parsing issues with headers.
        chapter_data['content'] = DEFAULT_CSS + "\n\n" + chapter_data['content']
    
    # Process sub-items
    for sub_item in chapter_data.get('sub_items', []):
        if 'Chapter' in sub_item:
            process_chapter(sub_item['Chapter'], exclude_files, config)
            
    return chapter_data

def main():
    # mdbook passes the book data via stdin as a JSON array: [context, book]
    if len(sys.argv) > 1 and sys.argv[1] == "supports":
        # mdbook checks if we support the renderer (usually "html")
        renderer = sys.argv[2] if len(sys.argv) > 2 else "unknown"
        sys.stderr.write(f"DEBUG: mdbook-toml_bitfield: checking support for renderer '{renderer}'\n")
        
        if renderer == "html":
            sys.exit(0)
        sys.exit(1)

    # Read from stdin
    try:
        data = json.load(sys.stdin)
    except Exception as e:
        sys.stderr.write(f"Error loading JSON from stdin: {e}\n")
        sys.exit(1)

    context = {}
    if isinstance(data, list):
        context = data[0]
        book = data[1]
    elif isinstance(data, dict):
        context = data.get('context', {})
        book = data['book']
    else:
        sys.stderr.write(f"Input is unknown type: {type(data)}\n")
        sys.exit(1)
    
    # Get configuration from context
    config = context.get('config', {}).get('preprocessor', {}).get('toml_bitfield', {})

    # Determine script directory for relative lookups
    script_dir = os.path.dirname(os.path.realpath(__file__))

    # Load global style if present
    global_style = {}
    style_path = config.get('style')
    
    # Resolution logic for style.toml:
    # Priority 1: Configured path
    # Priority 2: style.toml in CWD (book root)
    # Priority 3: style.toml in script directory
    
    if not style_path:
        if os.path.exists("style.toml"):
            style_path = "style.toml"
        else:
            default_style_path = os.path.join(script_dir, "style.toml")
            if os.path.exists(default_style_path):
                style_path = default_style_path
    
    if style_path:
        sys.stderr.write(f"DEBUG: mdbook-toml_bitfield: attempting to load style from '{os.path.abspath(style_path)}'\n")
    else:
        sys.stderr.write("DEBUG: mdbook-toml_bitfield: no style file specified or found in CWD or script dir.\n")

    if style_path and os.path.exists(style_path):
        try:
            with open(style_path, "rb") as f:
                style_raw = tomllib.load(f)
                if "style" in style_raw and isinstance(style_raw["style"], dict):
                    global_style = style_raw["style"]
                else:
                    global_style = style_raw
        except Exception as e:
            sys.stderr.write(f"Warning: Could not read style file '{style_path}': {e}\n")
    
    config['loaded_style'] = global_style

    # Files to exclude from processing
    # Read from exclude_list.txt in the same directory as the script
    exclude_file_path = os.path.join(script_dir, "exclude_list.txt")
    excluded_files = []
    
    if os.path.exists(exclude_file_path):
        try:
            with open(exclude_file_path, "r", encoding="utf-8") as f:
                excluded_files = [line.strip() for line in f if line.strip()]
        except Exception as e:
            sys.stderr.write(f"Warning: Could not read exclude list: {e}\n")

    # Process every section
    for section in book['sections']:
        if 'Chapter' in section:
            process_chapter(section['Chapter'], excluded_files, config)
            
    # Write back to stdout
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    
    # Dump just the book object. ensure_ascii=False ensures actual UTF-8 characters are output
    # rather than \uXXXX escapes, which avoids some parser issues with lone surrogates.
    print(json.dumps(book, ensure_ascii=False))

if __name__ == '__main__':
    # Force stdin/stdout to UTF-8 to avoid encoding issues on Windows
    # Mdbook communicates via JSON over stdio, which should be UTF-8.
    if sys.platform == 'win32':
        sys.stdin.reconfigure(encoding='utf-8')
        sys.stdout.reconfigure(encoding='utf-8')
    main()