# EGA Registers

Most register references you will find online are for the VGA exclusively, or else intermingle EGA and VGA to the point
where it can be confusing if you are looking for a EGA specific reference.

Every bit listed in this section is specific to the original IBM EGA, unless where noted.

> **NOTE:**
> The original IBM EGA and several clones have jumpers that can invert address line A09 during port decoding. This causes all the `3XX` range registers to be decoded at `2XX`. This is a fairly obscure feature and I am not aware of anything that uses it - even video BIOS routines will typically fail to control the card with this jumper set.

The EGA can switch between a port base of `3DX` and `3BX` for the CRTC and Input Status Register 1 registers - this is primarily for MDA compatibility. The EGA may configure itself this way on boot depending on the status of the [EGA DIP Switches](./ega-switches.md).

## Indexed Registers

Register indexing is a common way to reduce the complexity of address decoding and converve the IO address space. In its most common form, it consists of a pair of registers - an **address port** and a **data port**. First, a byte address or **register index** is written to the address port. This selects the desired register, assuming it it represents a valid index. Then, with the desired register selected, the new value for the register is written to the data port. The address port and data port are typically consecutive IO addresses, with the address port at an even address. There is a good reason for this.

A consequence of the 8088's transparent 8-bit bus means that an indexed register can be selected and written to via a single word-sized `OUT`. The data byte is typically packed into AH, with the address in AL. The 8088's BIU will convert the word write into two 8-bit writes at the base IO address and then the base address + 1. On the AT and subsequent 16-bit architectures, this conversion had to be specifically emulated by hardware on the motherboard.

Indexed registers can also be implemented via an internal flip-flop, where only a single IO port is required. The first write will set the register index, the second write will set the corresponding register data. Under this scheme there must be a way to reset the flip-flop to a known state. This technique is used for the EGA's single Attribute Controller IO port, which can be reset by reading `Input Status Register 1` at either `3DAh` or `3BAh`, depending on the EGA's current base address.

## Register File Overview

| I/O Address     | Read Function           | Write Function                         |
| :-------------- | :---------------------- | :------------------------------------- |
| **3B4h / 3D4h** | Not Readable            | **CRTC Index Register**                |
| **3B5h / 3D5h** | Not Readable            | **CRTC Data Register**                 |
| **3BAh / 3DAh** | Input Status Register 1 | **Feature Control Register**           |
| **3C0h**        | Not Readable            | **Attribute Controller**               |
| **3C2h**        | Input Status Register 0 | **Miscellaneous Output Register**      |
| **3C4h**        | Not Readable            | **Sequencer Index Register**           |
| **3C5h**        | Not Readable            | **Sequencer Data Register**            |
| **3CEh**        | Not Readable            | **Graphics Controller Index Register** |
| **3CFh**        | Not Readable            | **Graphics Controller Data Register**  |

### CRTC Registers

The EGA uses a custom LSI CRTC chip. It is very similar in operation to the [Motorola 6845](../../display-graphics/6845.md), but defines most vertical counters in units of scanlines. Using scanlines as the vertical unit is more convenient for a graphics-mode oriented video adapter. It also has the big advantage of not requiring any memory-addressing tricks that lead to inconvenient video memory layouts on the CGA and Hercules cards.

Most of the EGA CRTC registers are read-only, with the exeption of the three register pairs that hold memory addresses - the Start Address, Cursor Location, and Light Pen address registers can be read out. The inability to read the EGA CRTC registers was an annoyance for graphics and games programmers everywhere. This was rectified on the VGA which made most of the register file readable, but much software written for 4bpp modes did not rely on this to maintain backwards compatibility.

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


## SuperEGAs
