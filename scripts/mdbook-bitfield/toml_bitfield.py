#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
import os
import uuid
import re
from typing import Any, Dict, List, Optional, Tuple

import svgwrite
from pydantic import BaseModel, Field as PField, ValidationError, field_validator, model_validator

try:
    import tomllib  # Python 3.11+
except ModuleNotFoundError:
    import tomli as tomllib  # type: ignore


def slugify(text: str) -> str:
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


def transform_links(text: str, render_markdown: bool = True) -> str:
    """
    Detects {{Header Name}} or {{Header Name|Display Text}} 
    and converts them to Markdown internal links or plain text.
    """
    if not text:
        return text

    # Regex to capture {{Target}} or {{Target|Label}}
    pattern = r'\{\{(.*?)(?:\|(.*?))?\}\}'
    
    def replace_match(match):
        target = match.group(1)
        # If Group 2 is present, use it as label; otherwise use the target
        label = match.group(2) if match.group(2) else target
        
        if render_markdown:
            anchor = slugify(target)
            return f"[{label}](#{anchor})"
        else:
            return label 

    return re.sub(pattern, replace_match, text)


class FieldDef(BaseModel):
    name: str = ""
    lsb: int
    width: int = 1
    access: str = ""
    reset: str = ""
    description: str = ""
    color: str = ""  # optional
    css_class: str = ""  # optional override

    @property
    def msb(self) -> int:
        return self.lsb + self.width - 1

    def bit_range_str(self, ascending: bool = False) -> str:
        if self.width <= 1:
            return f"{self.lsb}"
        if ascending:
            return f"{self.lsb}:{self.msb}"
        return f"{self.msb}:{self.lsb}"

    @field_validator("width")
    @classmethod
    def _width_positive(cls, v: int) -> int:
        if v <= 0:
            raise ValueError("field width must be > 0")
        return v

    @field_validator("lsb")
    @classmethod
    def _lsb_nonnegative(cls, v: int) -> int:
        if v < 0:
            raise ValueError("field lsb must be >= 0")
        return v

class StyleDef(BaseModel):
    font_family: str = 'ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace'
    reserved_color: str = "#f4f4f4"
    undefined_color: str = "#e0e0e0"
    stroke_color: str = "#111"
    index_position: str = "bottom"  # "top" or "bottom"
    table_order: str = "ascending" # "ascending" or "descending"
    fallback_name: str = "--"
    hatch_angle: int = 45
    hatch_spacing: float = 4.0
    hatch_opacity: float = 0.5
    table_gap: float = 20.0
    reg_digits: int = 4
    show_access: bool = False
    show_reset: bool = False
    cell_gradient: bool = False
    
    # Header Spacing
    header_name_gap: float = 15.0
    header_desc_gap: float = 15.0
    header_addr_gap: float = 15.0
    
    # Font sizes
    header_fontsize: float = 18.0
    description_fontsize: float = 12.0
    bit_num_fontsize: float = 11.0
    field_name_fontsize: float = 13.0

    # CSS Classes
    header_class: str = "reg-header"
    description_class: str = "reg-desc"
    address_class: str = "reg-addr"
    bit_class: str = "reg-bit-num"
    field_name_class: str = "reg-field-name"
    field_meta_class: str = "reg-field-meta"
    legend_title_class: str = "legendT"
    legend_text_class: str = "legend"
    
    reserved_class: str = "field-reserved"
    undefined_class: str = "field-undefined"
    
    field_classes: List[str] = PField(default_factory=lambda: [
        "field-color-0", "field-color-1", "field-color-2", "field-color-3",
        "field-color-4", "field-color-5", "field-color-6", "field-color-7"
    ])
    
    palette: List[str] = PField(default_factory=lambda: [
        "#dae8fc",  # blue
        "#d5e8d4",  # green
        "#ffe6cc",  # orange
        "#e1d5e7",  # purple
        "#d0e0e3",  # teal
        "#fff2cc",  # yellow
        "#f5f5f5",  # grey
        "#bac8d3",  # blue-grey
    ])

    @field_validator("index_position")
    @classmethod
    def _validate_index_pos(cls, v: str) -> str:
        v = v.lower().strip()
        if v not in ("top", "bottom"):
            raise ValueError("index_position must be 'top' or 'bottom'")
        return v

    @field_validator("table_order")
    @classmethod
    def _validate_table_order(cls, v: str) -> str:
        v = v.lower().strip()
        if v not in ("ascending", "descending"):
            raise ValueError("table_order must be 'ascending' or 'descending'")
        return v

class RegisterMap(BaseModel):
    address: str
    access: str = ""

class RegisterDef(BaseModel):
    name: str
    bits: int
    address: str = ""
    description: str = ""
    anchor: str = ""
    default_access: str = ""
    register_access: str = ""  # "RO", "RW", "WO", etc.
    reg_maps: List[RegisterMap] = PField(default_factory=list, alias="register")
    style: StyleDef = PField(default_factory=StyleDef)
    fields: List[FieldDef] = PField(default_factory=list)

    @property
    def msb(self) -> int:
        return self.bits - 1

    @model_validator(mode="after")
    def _normalize_addresses(self) -> "RegisterDef":
        # If 'register' list is empty, populate it from top-level address/access
        if not self.reg_maps and self.address:
            self.reg_maps.append(RegisterMap(address=self.address, access=self.register_access))
        return self

    @field_validator("name")
    @classmethod
    def _reg_name_nonempty(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("register name cannot be empty")
        return v

    @field_validator("bits")
    @classmethod
    def _bits_positive(cls, v: int) -> int:
        if v <= 0:
            raise ValueError("register bits must be > 0")
        return v

    @model_validator(mode="after")
    def _validate_bounds_and_overlaps(self) -> "RegisterDef":
        used: List[Optional[str]] = [None] * self.bits
        for f in self.fields:
            if f.msb >= self.bits:
                raise ValueError(
                    f"Field '{f.name}' out of bounds: {f.bit_range_str()} for {self.bits}-bit register"
                )
            for b in range(f.lsb, f.msb + 1):
                if used[b] is not None:
                    raise ValueError(f"Fields '{used[b]}' and '{f.name}' overlap at bit {b}")
                used[b] = f.name
        
        # Validate register_access consistency
        if self.register_access:
            reg_acc = self.register_access.upper()
            if reg_acc in ("RO", "R"):
                for f in self.fields:
                    f_acc = (f.access or self.default_access).upper()
                    if f_acc in ("WO", "W", "RW", "WR"):
                        raise ValueError(
                            f"Register is marked '{self.register_access}' but field '{f.name}' has access '{f.access}'"
                        )
            elif reg_acc in ("WO", "W"):
                for f in self.fields:
                    f_acc = (f.access or self.default_access).upper()
                    if f_acc in ("RO", "R", "RW", "WR"):
                        raise ValueError(
                            f"Register is marked '{self.register_access}' but field '{f.name}' has access '{f.access}'"
                        )

        return self

def _layout_params(reg: RegisterDef, num_addresses: int = 1) -> Dict[str, float]:
    bits = reg.bits
    target_w = 800.0
    bit_w = target_w / max(bits, 1)
    # bit_w = max(14.0, min(34.0, bit_w))  # Removed clamping to ensure fixed width

    margin = 24.0
    
    # Dynamic header height calculation
    # Name (20) + Gap + Desc (18 if present) + Gap + Addrs (18*N) + Gap
    h_name = 20.0
    h_desc = 18.0 if reg.description.strip() else 0.0
    h_addr = max(1, num_addresses) * 18.0
    
    header_h = h_name + reg.style.header_name_gap
    if h_desc > 0:
        header_h += h_desc + reg.style.header_desc_gap
    header_h += h_addr + reg.style.header_addr_gap
    
    bitnum_h = 22.0
    field_h = bit_w  # Square cells
    gap_h = 14.0
    legend_title_h = 20.0
    legend_line_h = 18.0

    w = margin * 2 + bit_w * bits
    return {
        "bit_w": bit_w,
        "margin": margin,
        "header_h": header_h,
        "bitnum_h": bitnum_h,
        "field_h": field_h,
        "gap_h": gap_h,
        "legend_title_h": legend_title_h,
        "legend_line_h": legend_line_h,
        "w": w,
    }


def _pick_palette_color(i: int, palette: List[str]) -> str:
    if not palette:
        return "#ffffff"
    return palette[i % len(palette)]


def _auto_fill_reserved(reg: RegisterDef) -> List[FieldDef]:
    owner: List[Optional[FieldDef]] = [None] * reg.bits
    for f in reg.fields:
        for b in range(f.lsb, f.msb + 1):
            owner[b] = f

    out: List[FieldDef] = []
    b = 0
    while b < reg.bits:
        if owner[b] is None:
            start = b
            while b < reg.bits and owner[b] is None:
                b += 1
            width = b - start
            out.append(
                FieldDef(
                    name="UNDEFINED",
                    lsb=start,
                    width=width,
                    access="",
                    reset="",
                    description="",
                    color=reg.style.undefined_color,
                    css_class=reg.style.undefined_class,
                )
            )
        else:
            f = owner[b]
            assert f is not None
            out.append(f)
            b = f.msb + 1

    uniq: Dict[Tuple[int, int, str], FieldDef] = {}
    for f in out:
        uniq[(f.lsb, f.msb, f.name)] = f
    return sorted(uniq.values(), key=lambda x: (-x.msb, -x.lsb, x.name))


def generate_md_table(reg: RegisterDef) -> str:
    """Generates a Markdown table for the fields."""
    # Determine sorting order based on table_order style
    is_descending = (reg.style.table_order == "descending")
    is_ascending = not is_descending
    # Collect fields
    fields = sorted(reg.fields, key=lambda f: f.lsb, reverse=is_descending)
    
    # Determine columns
    has_access = reg.style.show_access or any(f.access for f in fields)
    has_reset = reg.style.show_reset or any(f.reset for f in fields)
    
    header = "| Bits | Name |"
    sep = "|---:|:---|"
    if has_access:
        header += " Access |"
        sep += ":---:|"
    if has_reset:
        header += " Reset |"
        sep += ":---:|"
    header += " Description |"
    sep += ":---|"
    
    lines = [header, sep]
    
    for f in fields:
        if f.name.lower() in ["reserved", "res"]:
             desc = f.description or "Reserved"
        else:
             # Process description for links
             desc = transform_links(f.description, render_markdown=True)
             
        if f.name:
             name_str = f"**{f.name}**"
        else:
             name_str = reg.style.fallback_name
             
        row = f"| {f.bit_range_str(ascending=is_ascending)} | {name_str} |"
        
        if has_access:
             acc = f.access or reg.default_access or ""
             row += f" {acc} |"
             
        if has_reset:
             rst = f.reset or ""
             row += f" {rst} |"
             
        row += f" {desc} |"
        lines.append(row)
        
    return "\n".join(lines) + "\n"


def render_svg(reg: RegisterDef, render_table: bool) -> str:
    p = _layout_params(reg, num_addresses=len(reg.reg_maps))
    bit_w = p["bit_w"]
    margin = p["margin"]
    header_h = p["header_h"]
    bitnum_h = p["bitnum_h"]
    field_h = p["field_h"]
    gap_h = p["gap_h"]
    legend_title_h = p["legend_title_h"]
    legend_line_h = p["legend_line_h"]
    w = p["w"]

    fields = _auto_fill_reserved(reg)

    # Generate unique IDs early so we can assign url(#id) to field colors
    unique_suffix = uuid.uuid4().hex[:8]
    hatch_id = f"hatch-{unique_suffix}"
    grad_id = f"cell-gradient-{unique_suffix}"

    # Assign classes/colors
    colored_fields: List[FieldDef] = []
    color_i = 0
    for f in sorted(fields, key=lambda x: (-x.msb, -x.lsb, x.name)):
        # Create a copy to modify
        f_new = FieldDef(**f.model_dump())
        
        desc_lower = (f.description or "").strip().lower()
        is_undefined_desc = desc_lower in ("reserved", "unused", "undefined")

        if is_undefined_desc:
            if f.name == "RESERVED" or f.name == "UNUSED":
              if not f_new.css_class:
                  f_new.css_class = reg.style.reserved_class
            if f.name == "UNDEFINED":
              if not f_new.css_class:
                  f_new.css_class = reg.style.undefined_class
            
            # Force hatch pattern
            f_new.color = f"url(#{hatch_id})"
        else:
            # Normal field
            if not f_new.css_class and not f_new.color:
                # Assign from palette/classes
                if reg.style.field_classes:
                    f_new.css_class = reg.style.field_classes[color_i % len(reg.style.field_classes)]
                else:
                    # Fallback to color palette
                    f_new.color = _pick_palette_color(color_i, reg.style.palette)
                color_i += 1
        
        colored_fields.append(f_new)

    # Filter fields for legend/table
    is_descending = (reg.style.table_order == "descending")
    is_undefined_name = f.name.strip().lower() in ("reserved", "unused", "undefined")
    legend_fields = [f for f in sorted(reg.fields, key=lambda x: (x.lsb, x.name), reverse=is_descending) 
                     if not is_undefined_name]

    if render_table:
        # Title + Header + Rows
        legend_h = legend_title_h + legend_line_h + (len(legend_fields) * legend_line_h) + 10
    else:
        legend_h = 0.0

    diagram_h = header_h + bitnum_h + field_h
    h = margin * 2 + diagram_h + gap_h + legend_h

    x0 = margin
    y0 = margin
    
    if reg.style.index_position == "bottom":
        y_fields = y0 + header_h
        y_bitnums = y_fields + field_h
    else:
        y_bitnums = y0 + header_h
        y_fields = y_bitnums + bitnum_h

    def x_for_bit(bit_index: int) -> float:
        # MSB on the left
        return x0 + (reg.msb - bit_index) * bit_w

    dwg = svgwrite.Drawing(size=("100%", "100%"), viewBox=f"0 0 {w:.0f} {h:.0f}", profile="full")

    # Accessibility: use SVG-native <title>/<desc>
    title_text = reg.name + (f" @ {reg.address}" if reg.address else "")
    desc_text = reg.description.strip() or None
    if desc_text:
        desc_text = transform_links(desc_text, render_markdown=False)
    dwg.set_desc(title=title_text, desc=desc_text)

    # Hatch pattern for undefined fields
    h_spacing = reg.style.hatch_spacing
    h_angle = reg.style.hatch_angle
    h_opacity = reg.style.hatch_opacity
    
    pattern = dwg.pattern(id=hatch_id, size=(h_spacing, h_spacing), patternUnits="userSpaceOnUse", patternTransform=f"rotate({h_angle})")
    pattern.add(dwg.rect(insert=(0, 0), size=(h_spacing, h_spacing), fill=reg.style.undefined_color))
    pattern.add(dwg.line(start=(0, 0), end=(0, h_spacing), stroke=reg.style.stroke_color, stroke_width=1, stroke_opacity=h_opacity))
    dwg.defs.add(pattern)

    if reg.style.cell_gradient:
        # Vertical gradient: Highlight top -> Body -> Dark bottom edge
        grad = dwg.linearGradient(start=(0, 0), end=(0, 1), id=grad_id)
        grad.add_stop_color(offset=0, color="white", opacity=0.3)
        grad.add_stop_color(offset=0.05, color="white", opacity=0.0)
        grad.add_stop_color(offset=0.05, color="black", opacity=0.0)
        grad.add_stop_color(offset=0.95, color="black", opacity=0.15)
        grad.add_stop_color(offset=1, color="black", opacity=0.25)
        dwg.defs.add(grad)

    # Header
    # Register Name
    # Baseline at y0 + 20
    dwg.add(dwg.text(reg.name, insert=(x0, y0 + 20), class_=reg.style.header_class))
    
    y_cursor = y0 + 20 + reg.style.header_name_gap

    # Description
    if reg.description.strip():
        y_cursor += 18.0 # Add line height to reach baseline
        clean_desc = transform_links(reg.description, render_markdown=False)
        dwg.add(dwg.text(clean_desc, insert=(x0, y_cursor), class_=reg.style.description_class))
        y_cursor += reg.style.header_desc_gap
    
    # Addresses
    acc_map = {
        "RO": "Read Only", "R": "Read Only",
        "WO": "Write Only", "W": "Write Only",
        "RW": "Read/Write", "WR": "Read/Write"
    }
    
    for rmap in reg.reg_maps:
        y_cursor += 18.0 # Add line height to reach baseline
        addr_display = rmap.address

        try:
            val = int(rmap.address, 0)
            hex_width = reg.style.reg_digits
            addr_display = f"0x{val:0{hex_width}X}"
        except ValueError:
            pass
            
        line_text = addr_display
        if rmap.access:
            acc_str = acc_map.get(rmap.access.upper(), rmap.access)
            line_text += f" ({acc_str})"
            
        dwg.add(dwg.text(line_text, insert=(x0, y_cursor), class_=reg.style.address_class))
        # Final gap (header_addr_gap) is handled by _layout_params in the total height

    # Bit numbers row
    for b in range(reg.msb, -1, -1):
        xb = x_for_bit(b)
        dwg.add(dwg.text(str(b), insert=(xb + bit_w / 2, y_bitnums + 16), text_anchor="middle", class_=reg.style.bit_class))

    # Outer border for fields row
    dwg.add(
        dwg.rect(
            insert=(x0, y_fields),
            size=(bit_w * reg.bits, field_h),
            fill="none",
            stroke=reg.style.stroke_color,
            stroke_width=1,
        )
    )

    # Fields
    for f in colored_fields:
        x_left = x_for_bit(f.msb)
        width_px = f.width * bit_w

        kwargs = {}
        if f.css_class:
            kwargs["class_"] = f.css_class
        if f.color:
            kwargs["fill"] = f.color

        dwg.add(
            dwg.rect(
                insert=(x_left, y_fields),
                size=(width_px, field_h),
                stroke=reg.style.stroke_color,
                stroke_width=1,
                **kwargs
            )
        )

        if reg.style.cell_gradient:
            dwg.add(
                dwg.rect(
                    insert=(x_left, y_fields),
                    size=(width_px, field_h),
                    fill=f"url(#{grad_id})",
                    stroke="none"
                )
            )

        # Internal bit separators for multi-bit fields
        if f.width > 1:
            for i in range(1, f.width):
                x_sep = x_for_bit(f.msb - i)
                dwg.add(dwg.line(
                    start=(x_sep, y_fields),
                    end=(x_sep, y_fields + field_h),
                    stroke=reg.style.stroke_color,
                    stroke_opacity=0.15,
                    stroke_width=1
                ))

        cx = x_left + width_px / 2
        cy = y_fields + field_h / 2 + 5

        display_name = f.name if f.name else reg.style.fallback_name

        if width_px < 40:
            t = dwg.text(display_name, insert=(cx, cy), text_anchor="middle", class_=reg.style.field_name_class)
            t.rotate(-90, center=(cx, cy))
            dwg.add(t)
        else:
            dwg.add(dwg.text(display_name, insert=(cx, y_fields + field_h / 2 + 4), text_anchor="middle", class_=reg.style.field_name_class))

        if f.name.upper() not in ("RESERVED", "UNUSED", "UNDEFINED") and width_px >= 85 and field_h >= 40:
            meta_parts = []
            # Removed bit range display inside the field
            if reg.style.show_access:
                access = (f.access or reg.default_access or "").strip()
                if access:
                    meta_parts.append(access)
            if reg.style.show_reset and f.reset.strip():
                meta_parts.append(f"r={f.reset.strip()}")
            
            if meta_parts:
                meta = " ".join(meta_parts)
                dwg.add(dwg.text(meta, insert=(cx, y_fields + field_h - 6), text_anchor="middle", class_=reg.style.field_meta_class))

    # Legend / Table
    if render_table:
        y_table_top = y_fields + field_h + reg.style.table_gap
        
        has_access = any((f.access or reg.default_access) for f in legend_fields)
        has_reset = any(f.reset for f in legend_fields)

        # Column offsets
        current_x = x0
        col_x = {}
        
        col_x["bits"] = current_x
        current_x += 60
        
        col_x["name"] = current_x
        current_x += 140
        
        if has_access:
            col_x["access"] = current_x
            current_x += 60
            
        if has_reset:
            col_x["reset"] = current_x
            current_x += 60
            
        col_x["desc"] = current_x
        
        # Header
        dwg.add(dwg.text("Bits", insert=(col_x["bits"], y_table_top), class_=reg.style.legend_text_class, font_weight="bold"))
        dwg.add(dwg.text("Name", insert=(col_x["name"], y_table_top), class_=reg.style.legend_text_class, font_weight="bold"))
        
        if has_access:
            dwg.add(dwg.text("Access", insert=(col_x["access"], y_table_top), class_=reg.style.legend_text_class, font_weight="bold"))
        if has_reset:
            dwg.add(dwg.text("Reset", insert=(col_x["reset"], y_table_top), class_=reg.style.legend_text_class, font_weight="bold"))
            
        dwg.add(dwg.text("Description", insert=(col_x["desc"], y_table_top), class_=reg.style.legend_text_class, font_weight="bold"))
        
        # Separator line
        dwg.add(dwg.line(start=(x0, y_table_top + 4), end=(w - margin, y_table_top + 4), stroke=reg.style.stroke_color, stroke_width=0.5))

        y_row = y_table_top + legend_line_h
        
        for f in legend_fields:
            bits = f.bit_range_str(ascending=not is_descending)
            name = f.name if f.name else reg.style.fallback_name
            access = f.access or reg.default_access or ""
            reset = f.reset or ""
            desc = transform_links(f.description, render_markdown=False) if f.description else ""
            
            dwg.add(dwg.text(bits, insert=(col_x["bits"], y_row), class_=reg.style.legend_text_class))
            dwg.add(dwg.text(name, insert=(col_x["name"], y_row), class_=reg.style.legend_text_class))
            
            if has_access:
                dwg.add(dwg.text(access, insert=(col_x["access"], y_row), class_=reg.style.legend_text_class))
            if has_reset:
                dwg.add(dwg.text(reset, insert=(col_x["reset"], y_row), class_=reg.style.legend_text_class))
                
            dwg.add(dwg.text(desc, insert=(col_x["desc"], y_row), class_=reg.style.legend_text_class))
            
            y_row += legend_line_h

    return dwg.tostring()

def load_toml(path: str) -> Dict[str, Any]:
    with open(path, "rb") as f:
        return tomllib.load(f)


def write_text(path: str, s: str) -> None:
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(s)
        if not s.endswith("\n"):
            f.write("\n")


def main(argv: Optional[List[str]] = None) -> int:
    ap = argparse.ArgumentParser(description="Generate SVG register diagrams from TOML.")
    ap.add_argument("input", help="Input TOML register definition file.")
    ap.add_argument("-o", "--output", default="", help="Output SVG path. If omitted, prints to stdout.")
    ap.add_argument("-s", "--style", default="", help="Optional TOML file containing global style definitions.")
    ap.add_argument("--table", choices=["svg", "md"], help="Generate a field table in SVG or Markdown format.")
    ap.add_argument("--show-access", action="store_true", help="Show access type (RO, RW, etc.) in the register bit cells.")
    ap.add_argument("--show-reset", action="store_true", help="Show reset value in the register bit cells.")
    args = ap.parse_args(argv)

    try:
        raw = load_toml(args.input)
        reg = RegisterDef.model_validate(raw)

        style_path = args.style
        if not style_path and os.path.exists("style.toml"):
            style_path = "style.toml"

        if style_path:
            style_raw = load_toml(style_path)
            # Support both [style] table and top-level keys
            if "style" in style_raw and isinstance(style_raw["style"], dict):
                style_config = style_raw["style"]
            else:
                style_config = style_raw
            
            # Merge: CLI style overrides register style
            merged_style = reg.style.model_dump()
            merged_style.update(style_config)
            reg.style = StyleDef.model_validate(merged_style)

        # CLI flags override style settings if set
        if args.show_access:
            reg.style.show_access = True
        if args.show_reset:
            reg.style.show_reset = True

        svg = render_svg(reg, table_format=args.table)
    except ValidationError as e:
        print("error: invalid register definition:", file=sys.stderr)
        print(e, file=sys.stderr)
        return 2
    except Exception as e:
        print(f"error: {e}", file=sys.stderr)
        return 1

    if args.output:
        write_text(args.output, svg)
        if args.table == "md":
            md_path = os.path.splitext(args.output)[0] + ".md"
            md_content = generate_md_table(reg)
            write_text(md_path, md_content)
    else:
        sys.stdout.write(svg)
        if not svg.endswith("\n"):
            sys.stdout.write("\n")
        if args.table == "md":
             # If writing to stdout, append the markdown table
             md_content = generate_md_table(reg)
             sys.stdout.write("\n" + md_content)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
