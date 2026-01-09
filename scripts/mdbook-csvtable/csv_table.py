import csv
import sys
import argparse
import re

def slugify(text):
    """
    Converts text to a Markdown-compatible anchor slug.
    Example: "My Header!" -> "my-header"
    """
    text = text.lower()
    # Remove non-alphanumeric characters (excluding spaces and hyphens)
    text = re.sub(r'[^\w\s-]', '', text)
    # Replace whitespace and existing hyphens with a single hyphen
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')

def transform_links(text):
    """
    Detects [[Header Name]] or [[Header Name|Display Text]] 
    and converts them to Markdown internal links.
    """
    # Regex to capture [[Target]] or [[Target|Label]]
    # Group 1 = Target Header
    # Group 2 = Label (optional)
    pattern = r'\[\[(.*?)(?:\|(.*?))?\]\]'
    
    def replace_match(match):
        target_header = match.group(1)
        # If Group 2 is present, use it as label; otherwise use the target header
        display_text = match.group(2) if match.group(2) else target_header
        
        anchor = slugify(target_header)
        return f"[{display_text}](#{anchor})"

    return re.sub(pattern, replace_match, text)

def get_column_widths(rows):
    """
    Calculates the maximum width required for each column.
    """
    if not rows:
        return []

    num_columns = len(rows[0])
    widths = [0] * num_columns

    for row in rows:
        for index, cell in enumerate(row):
            if index < num_columns:
                widths[index] = max(widths[index], len(cell))
    
    # Minimum width of 3 for separation lines
    return [max(w, 3) for w in widths]

def pad_cell(cell, width):
    return cell.ljust(width)

def csv_to_markdown(input_file):
    try:
        reader = csv.reader(input_file)
        rows = list(reader)
    except Exception as e:
        sys.stderr.write(f"Error reading CSV: {e}\n")
        sys.exit(1)

    if not rows:
        return ""

    processed_rows = []
    
    # Pre-process: Handle newlines AND transform links
    for row in rows:
        new_row = []
        for cell in row:
            cleaned = cell.replace('\n', '<br>')
            cleaned = transform_links(cleaned)
            new_row.append(cleaned)
        processed_rows.append(new_row)

    # Calculate Widths (Must happen AFTER transformation to account for extra char length)
    widths = get_column_widths(processed_rows)
    
    header = processed_rows[0]
    data = processed_rows[1:]

    output_lines = []

    # Header
    header_cells = [pad_cell(h, w) for h, w in zip(header, widths)]
    output_lines.append(f"| {' | '.join(header_cells)} |")

    # Separator
    separator_cells = ['-' * w for w in widths]
    output_lines.append(f"| {' | '.join(separator_cells)} |")

    # Data
    for row in data:
        # Handle ragged rows
        current_row = row + [""] * (len(header) - len(row))
        padded_cells = [pad_cell(cell, w) for cell, w in zip(current_row, widths)]
        output_lines.append(f"| {' | '.join(padded_cells)} |")

    return "\n".join(output_lines)

def main():
    parser = argparse.ArgumentParser(description="Convert CSV to Markdown table with [[Link]] support.")
    parser.add_argument('file', nargs='?', type=argparse.FileType('r'), default=sys.stdin,
                        help="Path to CSV file (stdin if empty)")
    
    args = parser.parse_args()
    print(csv_to_markdown(args.file))

if __name__ == "__main__":
    main()