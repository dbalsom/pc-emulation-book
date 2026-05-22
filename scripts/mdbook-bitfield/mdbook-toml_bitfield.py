#!/usr/bin/env python3
import json
import sys
import os
import re
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

    # look for ```bitfield and replace the block with SVG
    lines = content.split('\n')
    new_lines = []
    in_block = False
    block_lines = []
    found_bitfield = False
    
    for line in lines:
        stripped_line = line.strip()
        if stripped_line.startswith('```bitfield') or stripped_line.startswith('```toml_bitfield'):
            in_block = True
            found_bitfield = True
            block_lines = []
            continue
            
        # Check for {{#bitfield file.toml#anchor}}
        bitfield_match = re.search(r'\{\{#bitfield\s+([^#]+)(?:#([^}]+))?\}\}', line)
        if bitfield_match:
            found_bitfield = True
            filename = bitfield_match.group(1).strip()
            anchor = bitfield_match.group(2)
            if anchor:
                anchor = anchor.strip()
                
            # Determine file path
            # 1. Try relative to the current markdown file's source path
            # src_dir is relative to the book root, where mdbook is run
            src_dir = os.path.dirname(path) if path else ""
            toml_path = os.path.join(src_dir, filename)
            
            # 2. Fallback to src/bitfields/
            if not os.path.exists(toml_path):
                fallback_path = os.path.join("src", "bitfields", filename)
                if os.path.exists(fallback_path):
                    toml_path = fallback_path

            if not os.path.exists(toml_path):
                # TODO: this should probably be a build error instead
                new_lines.append(f"<pre style='color:red'>Error: Could not find bitfield file '{filename}'</pre>")
                continue
                
            try:
                with open(toml_path, "rb") as f:
                    raw_data = tomllib.load(f)
                    
                # Handle single or multi-register definitions
                reg_data_list = []
                if "registers" in raw_data:
                    regs_src = raw_data["registers"]
                    
                    if isinstance(regs_src, dict):
                        # Dictionary-based format (e.g. [registers.my-anchor])
                        # Inject the dictionary key as the 'anchor' if not present
                        for k, v in regs_src.items():
                            if isinstance(v, dict):
                                if "anchor" not in v:
                                    v["anchor"] = k
                                # If an anchor filter is active, only append matches
                                if anchor:
                                    if str(v.get("anchor", "")) == anchor or k == anchor:
                                        reg_data_list.append(v)
                                else:
                                    reg_data_list.append(v)
                                    
                        if anchor and not reg_data_list:
                            raise Exception(f"Register with anchor '{anchor}' not found in {toml_path}")
                        if not anchor and not reg_data_list:
                            raise Exception(f"No registers found in array in {toml_path}")

                    elif isinstance(regs_src, list):
                        # Array-based format (e.g. [[registers]])
                        if anchor:
                            found = False
                            for r in regs_src:
                                if str(r.get("anchor", "")) == anchor:
                                    reg_data_list.append(r)
                                    found = True
                                    break
                            if not found:
                                raise Exception(f"Register with anchor '{anchor}' not found in {toml_path}")
                        else:
                            # If no anchor, grab all registers
                            if regs_src:
                                reg_data_list = regs_src
                            else:
                                raise Exception(f"No registers found in array in {toml_path}")
                    else:
                        raise Exception(f"'registers' key must be a list or dict in {toml_path}")
                else:
                    reg_data_list = [raw_data]
                    
                
                all_svg_outputs = []
                for reg_data in reg_data_list:
                    reg = RegisterDef.model_validate(reg_data)
                    
                    # Apply global style if loaded
                    global_style = config.get('loaded_style', {})
                    if global_style:
                        merged_style = reg.style.model_dump()
                        merged_style.update(global_style)
                        reg.style = StyleDef.model_validate(merged_style)
                    
                    # Read parameters from mdbook config
                    table_format = config.get('table')
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
                        
                    svg_output = f'<div class="toml-bitfield-wrapper">\n{svg_output}\n</div>'
                    all_svg_outputs.append(svg_output)
                
                # Replace the match in the line with the combined outputs
                combined_output = "\n".join(all_svg_outputs)
                new_line = line[:bitfield_match.start()] + combined_output + line[bitfield_match.end():]
                new_lines.append(new_line)
                
            except Exception as e:
                new_lines.append(f"<pre style='color:red'>Error rendering SVG from {toml_path}: {e}</pre>")
                
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

                # TODO: actually use this
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
                     
                svg_output = f'<div class="toml-bitfield-wrapper">\n{svg_output}\n</div>'
                
                new_lines.append(svg_output)
            except Exception as e:
                # Fallback: print error in place of SVG for debugging
                # TODO: Again, should probably be a build error?
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
        sys.stderr.write(f"DEBUG: mdbook-bitfield: checking support for renderer '{renderer}'\n")
        
        if renderer == "html":
            sys.exit(0)

        sys.stderr.write(f"ERROR: mdbook-bitfield currently only supports html renderer\n")
        sys.exit(1)

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
    preprocessors = context.get('config', {}).get('preprocessor', {})
    config = preprocessors.get('bitfield', preprocessors.get('toml_bitfield', {}))

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
        sys.stderr.write(f"DEBUG: mdbook-bitfield: attempting to load style from '{os.path.abspath(style_path)}'\n")
    else:
        sys.stderr.write("DEBUG: mdbook-bitfield: no style file specified or found in CWD or script dir.\n")

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
    # TODO: 'txt' is a bit windows-specific.  maybe .exclude_list is more agnostic
    exclude_file_path = os.path.join(script_dir, "exclude_list.txt")
    excluded_files = []
    
    if os.path.exists(exclude_file_path):
        try:
            with open(exclude_file_path, "r", encoding="utf-8") as f:
                excluded_files = [line.strip() for line in f if line.strip()]
        except Exception as e:
            sys.stderr.write(f"Warning: Could not read exclude list: {e}\n")

    # Process every top-level item
    for section in book['items']:
        if 'Chapter' in section:
            process_chapter(section['Chapter'], excluded_files, config)
            
    # Write back to stdout
    # TODO: redundant with reconfigure in __main__? factor out?
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    
    # Dump just the book object. 
    # ensure_ascii=False allows actual UTF-8 to be output
    print(json.dumps(book, ensure_ascii=False))

if __name__ == '__main__':
    # Force stdin/stdout to UTF-8 to avoid encoding issues on Windows
    # mdbook communicates via JSON over stdio, which should be UTF-8.
    if sys.platform == 'win32':
        sys.stdin.reconfigure(encoding='utf-8')
        sys.stdout.reconfigure(encoding='utf-8')
    main()
