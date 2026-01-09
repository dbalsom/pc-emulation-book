#!/usr/bin/env python3
import json
import sys
import os
import re
from csv_table import csv_to_markdown

# Regex to match {{#csvtable path/to/file.csv}}
CSV_REGEX = re.compile(r'\{\{#csvtable\s+(.*?)\}\}')

def process_chapter(chapter_data, base_dir):
    """Recursively process chapter content to replace csvtable tags."""
    content = chapter_data.get('content', '')
    source_path = chapter_data.get('source_path', chapter_data.get('path', ''))
    
    # Calculate the directory of the current markdown file
    if source_path:
        current_dir = os.path.dirname(os.path.join(base_dir, source_path))
    else:
        current_dir = base_dir

    def replace_match(match):
        rel_path = match.group(1).strip()
        csv_path = os.path.join(current_dir, rel_path)
        
        # Security: ensure we don't escape the build directory? 
        # For now, trust the author.
        
        if not os.path.exists(csv_path):
            return f"> **Error: CSV file not found: {rel_path}**"
            
        try:
            with open(csv_path, 'r', encoding='utf-8', newline='') as f:
                return csv_to_markdown(f)
        except Exception as e:
            return f"> **Error processing CSV {rel_path}: {e}**"

    # Replace all occurrences
    new_content = CSV_REGEX.sub(replace_match, content)
            
    chapter_data['content'] = new_content
    
    # Process sub-items
    for sub_item in chapter_data.get('sub_items', []):
        if 'Chapter' in sub_item:
            process_chapter(sub_item['Chapter'], base_dir)
            
    return chapter_data

def main():
    # mdbook passes the book data via stdin as a JSON array: [context, book]
    if len(sys.argv) > 1 and sys.argv[1] == "supports":
        # mdbook checks if we support the renderer (usually "html")
        sys.exit(0)

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

    # Determine base directory for resolving relative paths
    root_dir = context.get('root', '.')
    book_config = context.get('config', {}).get('book', {})
    src_dir = book_config.get('src', 'src')
    base_dir = os.path.join(root_dir, src_dir)

    # Process every section
    for section in book['sections']:
        if 'Chapter' in section:
            process_chapter(section['Chapter'], base_dir)
            
    # Write back to stdout
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    
    print(json.dumps(book, ensure_ascii=False))

if __name__ == '__main__':
    # Force stdin/stdout to UTF-8
    if sys.platform == 'win32':
        sys.stdin.reconfigure(encoding='utf-8')
        sys.stdout.reconfigure(encoding='utf-8')
    main()
