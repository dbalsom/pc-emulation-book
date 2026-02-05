# EGA Registers

Most register references you will find online are for the VGA exclusively, or else intermingle EGA and VGA to the point
where it can be confusing if you are looking for a EGA specific reference.

Every bit listed in this section is specific to the original IBM EGA, unless where noted.

> **NOTE:**
> The original IBM EGA and several clones have jumpers that can invert address line A09 during port decoding. This causes all the `3XX` range registers to be decoded at `2XX`. This is a fairly obscure feature and I am not aware of anything that uses it - even video BIOS routines will typically fail to control the card with this jumper set.

The EGA can switch between a port base of `3DX` and `3BX` for the CRTC and Input Status Register 1 registers - this is primarily for MDA compatibility. The EGA may configure itself this way on boot depending on the status of the [EGA DIP Switches](./ega-switches.md).

## Indexed Registers

Register indexing is a common way to reduce the complexity of address decoding and conserve the IO address space. In its most common form, it consists of a pair of registers - an **address port** and a **data port**. First, a byte address or **register index** is written to the address port. This selects the desired register, assuming it represents a valid index. Then, with the desired register selected, the new value for the register is written to the data port. The address port and data port are typically consecutive IO addresses, with the address port at an even address. There is a good reason for this.

A consequence of the 8088's transparent 8-bit bus is that an indexed register can be selected and written to via a single word-sized `OUT`. The data byte is typically packed into AH, with the address in AL. The 8088's BIU will convert the word write into two 8-bit writes at the base IO address and then the base address + 1. On the AT and subsequent 16-bit architectures, this conversion had to be specifically emulated by hardware on the motherboard.

Indexed registers can also be implemented via an internal flip-flop, where only a single IO port is required. The first write will set the register index, the second write will set the corresponding register data. Under this scheme there must be a way to reset the flip-flop to a known state. This technique is used for the EGA's single Attribute Controller IO port, which can be reset by reading `Input Status Register 1` at either `3DAh` or `3BAh`, depending on the EGA's current base address.

## Register File Overview

| I/O Address   | Read Function           | Write Function                       |
| :------------ | :---------------------- | :----------------------------------- |
| **3B4 / 3D4** | Not Readable            | CRTC Address Register                |
| **3B5 / 3D5** | Not Readable            | CRTC Data Register                   |
| **3BA / 3DA** | Input Status Register 1 | Feature Control Register             |
| **3C0**       | Not Readable            | Attribute Controller                 |
| **3C2**       | Input Status Register 0 | Miscellaneous Output Register        |
| **3C4**       | Not Readable            | Sequencer Address Register           |
| **3C5**       | Not Readable            | Sequencer Data Register              |
| **3CE**       | Not Readable            | Graphics Controller Address Register |
| **3CF**       | Not Readable            | Graphics Controller Data Register    |

### Register Set Details Index

 - [External Registers](#external-register-details)
 - [CRTC](#crtc-register-details)
 - [Attribute Controller](#attribute-controller-register-details)


### CRTC Registers

The EGA uses a custom LSI CRTC chip. It is very similar in operation to the [Motorola 6845](../../display-graphics/6845.md), but defines most vertical counters in units of scanlines. Using scanlines as the vertical unit is more convenient for a graphics-mode oriented video adapter. It also has the big advantage of not requiring any memory-addressing tricks that lead to inconvenient video memory layouts on the CGA and Hercules cards.

Most of the EGA CRTC registers are read-only, with the exception of the three register pairs that hold memory addresses - the Start Address, Cursor Location, and Light Pen address registers can be read out. The inability to read the EGA CRTC registers was an annoyance for graphics and games programmers everywhere. This was rectified on the VGA which made most of the register file readable, but much software written for 4bpp modes did not rely on this to maintain backwards compatibility.

| Index   | Register Name            | Access | Description                                         |
| :------ | :----------------------- | :----- | :-------------------------------------------------- |
| **00h** | Horizontal Total         | W      | Total character clocks in a scanline, minus 2       |
| **01h** | Horizontal Display End   | W      | Number of characters visible per line               |
| **02h** | Start Horizontal Blank   | W      | Character position where horizontal blanking begins |
| **03h** | End Horizontal Blank     | W      | Character position where horizontal blanking ends   |
| **04h** | Start Horizontal Retrace | W      | Character position where horizontal retrace begins  |
| **05h** | End Horizontal Retrace   | W      | Character position where horizontal retrace ends    |
| **06h** | Vertical Total           | W      | Total number of scanlines per frame                 |
| **07h** | Overflow                 | W      | High bits for V-Total, V-Display, V-Sync            |
| **08h** | Preset Row Scan          | W      | Starting scanline within a character cell           |
| **09h** | Max Scan Line            | W      | Height of character cell minus 1                    |
| **0Ah** | Cursor Start             | W      | Top scanline of cursor                              |
| **0Bh** | Cursor End               | W      | Bottom scanline of cursor                           |
| **0Ch** | Start Address High       | RW     | High byte of display memory start pointer           |
| **0Dh** | Start Address Low        | RW     | Low byte of display memory start pointer            |
| **0Eh** | Cursor Location High     | RW     | High byte of cursor memory address                  |
| **0Fh** | Cursor Location Low      | RW     | Low byte of cursor memory address                   |
| **10h** | Vertical Retrace Start   | W      | Scanline where Vertical Retrace begins              |
| **10h** | Light Pen Address High   | R      | High byte of Light Pen latched memory address       |
| **11h** | Vertical Retrace End     | W      | Scanline where Vertical Retrace ends (Bits 0-3)     |
| **11h** | Light Pen Address Low    | R      | Low byte of Light Pen latched memory address        |
| **12h** | Vertical Display End     | W      | Last visible scanline (low 8 bits)                  |
| **13h** | Offset                   | W      | Span width of logical scanline                      |
| **14h** | Underline Location       | W      | Scanline within cell for underline                  |
| **15h** | Start Vertical Blank     | W      | Scanline where blanking starts                      |
| **16h** | End Vertical Blank       | W      | Scanline where blanking ends                        |
| **17h** | Mode Control             | W      | Hardware compatibility/timing toggles               |
| **18h** | Line Compare             | W      | Scanline on which CRTC start address is reset       |

### Graphics Controller Registers

| Port    | Register Name       | Access |
| :------ | :------------------ | :----- |
| **3CC** | Graphics 1 Position | W      |
| **3CA** | Graphics 2 Position | W      |
| **3CE** | Graphics Address    | W      |
| **3CF** | Graphics Data       | W      |

On the original IBM EGA, there are two separate Graphics Controller chips. They can generally be treated as a single entity except for the two **Graphics Position** registers. These two registers are used to tell each of the graphics controllers which pair of graphics planes they will be managing.

The Graphics Controller chips lack an IOW pin, thus all their registers are write-only.

### Graphics Controller Indexed Registers

| Index   | Register Name    |
| :------ | :--------------- |
| **00h** | Set/Reset        |
| **01h** | Enable Set/Reset |
| **02h** | Color Compare    |
| **03h** | Data Rotate      |
| **04h** | Read Map Select  |
| **05h** | Mode Register    |
| **06h** | Miscellaneous    |
| **07h** | Color Don't Care |
| **08h** | Bit Mask         |

### Sequencer Registers

| Port    | Register Name     | Access |
| :------ | :---------------- | :----- |
| **3C4** | Sequencer Address | W      |
| **3C5** | Sequencer Data    | W      |

### Sequencer Indexed Registers

| Index   | Register Name        |
| :------ | :------------------- |
| **00h** | Reset                |
| **01h** | Clocking Mode        |
| **02h** | Map Mask             |
| **03h** | Character Map Select |
| **04h** | Memory Mode          |


### Attribute Controller Registers

| Port          | Register Name                             | Access |
| :------------ | :---------------------------------------- | :----- |
| **3BA / 3CA** | Reset Attribute Flip-Flop                 | R      |
| **3C0**       | Address / Data (Flip-flops on each write) | W      |

### Attribute Controller Indexed Registers

| Index       | Register Name                                               | Access |
| :---------- | :---------------------------------------------------------- | :----- |
| **00h-0Fh** | [Attribute Palette Entries](#attribute-palette-entry) [0-F] | W*     |
| **10h**     | [Mode Control](#attribute-mode-control)                     | W      |
| **11h**     | [Overscan Color](#overscan-color-register)                  | W      |
| **12h**     | [Color Plane Enable](#color-plane-enable-register)          | W      |
| **13h**     | [Horizontal Pel Panning](#pel-panning-register)             | W      |


The first sixteen registers in the Attribute Controller define a 4bpp palette.

## External Register Details

```toml_bitfield
name = "Miscellaneous Output Register"
anchor = "miscellaneous-output-register"
bits = 8
description = "Controls basic hardware configuration such as IO address and clock selection"

[[register]]
address = "3C2"
access = "Write-Only"

[[fields]]
name = "VSP"
lsb = 7
width = 1
description = "Vertical Sync Polarity (0=Pos, 1=Neg)"

[[fields]]
name = "HSP"
lsb = 6
width = 1
description = "Horizontal Sync Polarity (0=Pos, 1=Neg)"

[[fields]]
name = "PAGE"
lsb = 5
width = 1
description = "Page bit for Odd/Even mode"

[[fields]]
name = "DISABLE"
lsb = 4
width = 1
description = "Disable Video Drivers (1=Disable)"

[[fields]]
name = "CLK"
lsb = 2
width = 2
description = "Clock Select (00=14MHz, 01=16MHz, 10=External, 11=Unused)"

[[fields]]
name = "ERAM"
lsb = 1
width = 1
description = "Enable RAM (1=Enabled)"

[[fields]]
name = "IO"
lsb = 0
width = 1
description = "I/O Address (0=3Bx mono, 1=3Dx color)"
```

```toml_bitfield
name = "Feature Control Register"
anchor = "feature-control-register"
bits = 8
description = "Set control signals sent to the EGA Feature Connector"

[[register]]
address = "3BA / 3DA"
access = "Write-Only"

[[fields]]
name = "FC0"
lsb = 0
width = 1
description = "Feature Control Bit 0"

[[fields]]
name = "FC1"
lsb = 1
width = 1
description = "Feature Control Bit 1"

[[fields]]
name = "Reserved"
lsb = 2
width = 2
description = "Reserved"

[[fields]]
lsb = 4
width = 4
description = "Unused"
```

```toml_bitfield
name = "Input Status Register 0"
anchor = "input-status-register-0"
bits = 8
description = "Read DIP switches and interrupt status"

[[register]]
address = "3C2"
access = "Read-Only"

[[fields]]
lsb = 0
width = 4
description = "Unused"

[[fields]]
name = "SENSE"
lsb = 4
width = 1
description = "Switch Sense - State of selected configuration switch"

[[fields]]
name = "FEAT0"
lsb = 5
width = 1
description = "State of FEAT0 pin on Feature Connector"

[[fields]]
name = "FEAT1"
lsb = 6
width = 1
description = "State of FEAT1 pin on Feature Connector"

[[fields]]
name = "INT"
lsb = 7
width = 1
description = "CRT Interrupt Pending (1=Yes)"
```

## Attribute Controller Register Details

```toml_bitfield
name = "Attribute Palette Entry"
anchor = "attribute-palette-entry"
bits = 8
description = "Used by the Attribute Controller to look up an output color from a 4bpp pixel index"

[[register]]
address = "3C0 Index 0-Fh"
access = "Write-Only"

[[fields]]
name = "B"
lsb = 0
width = 1
description = "Blue"
color = "0000AA"

[[fields]]
name = "G"
lsb = 1
width = 1
description = "Green"
color = "00AA00"

[[fields]]
name = "R"
lsb = 2
width = 1
description = "Red"
color = "AA0000"

[[fields]]
name = "SB/I"
lsb = 3
width = 1
description = "Secondary Blue / Mono Intensity"
color = "5555FF"

[[fields]]
name = "SG/I"
lsb = 4
width = 1
description = "Secondary Green / Intensity"
color = "55FF55"

[[fields]]
name = "SR"
lsb = 5
width = 1
description = "Secondary Red"
color = "FF5555"

[[fields]]
name = "Unused"
lsb = 6
width = 2
description = "Unused"

```

```toml_bitfield
name = "Attribute Mode Control"
anchor = "attribute-mode-control"
bits = 8
description = "Specifies general mode options for Attribute Controller operation"

[[register]]
address = "3C0 Index 10h"
access = "Write-Only"

[[fields]]
name = "G/A"
lsb = 0
width = 1
description = "**Video Mode:**<br>**1**: Graphics Mode<br>**0**: Alphanumeric Mode"

[[fields]]
name = "DT"
lsb = 1
width = 1
description = "**Text Attribute Type:**<br>**0**: Color<br>**1**: MDA"

[[fields]]
name = "LG"
lsb = 2
width = 1
description = "Enable Line Graphics Characters"

[[fields]]
name = "B/I"
lsb = 3
width = 1
description = "**Attribute Bit 7 interpreted as:**<br>**1**: Blink Enabled<br>**0**: Background Intensity"

[[fields]]
name = "Unused"
lsb = 4
width = 4
description = "Unused"
```


```toml_bitfield
name = "Overscan Color Register"
anchor = "overscan-color-register"
bits = 8
description = "Selects the color to use when drawing the overscan area"

[[register]]
address = "3C0 Index 11h"
access = "Write-Only"

[[fields]]
name = "B"
lsb = 0
width = 1
description = "Blue"
color = "0000AA"

[[fields]]
name = "G"
lsb = 1
width = 1
description = "Green"
color = "00AA00"

[[fields]]
name = "R"
lsb = 2
width = 1
description = "Red"
color = "AA0000"

[[fields]]
name = "SB/I"
lsb = 3
width = 1
description = "Secondary Blue"
color = "5555FF"

[[fields]]
name = "SG/I"
lsb = 4
width = 1
description = "Secondary Green / Intensity"
color = "55FF55"

[[fields]]
name = "SR"
lsb = 5
width = 1
description = "Secondary Red"
color = "FF5555"

[[fields]]
name = "Unused"
lsb = 6
width = 2
description = "Unused"

```

```toml_bitfield
name = "Color Plane Enable Register"
anchor = "color-plane-enable-register"
bits = 8
description = "Controls which bits are enabled when addressing the palette registers"

[[register]]
address = "3C0 Index 12h"
access = "Write-Only"

[[fields]]
name = "ECP"
lsb = 0
width = 4
description = "**Enable Color Planes**<br>Each bit set in this field enables the corresponding plane 0-3."

[[fields]]
name = "MUX"
lsb = 4
width = 2
description = "Video Status MUX"

[[fields]]
name = "Unused"
lsb = 6
width = 2
description = "Unused"
```

```toml_bitfield
name = "Horizontal Pel Panning Register"
anchor = "pel-panning-register"
bits = 8
description = "Shifts the display horizontally to the left"

[[register]]
address = "3C0 Index 13h"
access = "Write-Only"

[[fields]]
name = "PAN"
lsb = 0
width = 4
description = "**Horizontal Pel Panning Value**<br>EGA Mode: 0-7<br>Monochrome Mode: 8,0-7"

[[fields]]
name = "Unused"
lsb = 4
width = 4
description = "Unused"
```