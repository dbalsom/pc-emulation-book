# SuperEGA Registers

There were several video chipset manufacturers who produced EGA chipsets with extended capabilities, most typically an increased resolution of 640x480. These adapters were typically called SuperEGAs.

SuperEGA chipsets often extended the standard EGA register file, with new register indices defined for the CRTC, graphics controllers, sequencer and attribute controller.

### ET2000

The Tseng Labs ET2000 was an advanced chipset designed to be adaptable to a variety of different graphics adapters, although it only ever appeared on three EGA cards: the Tseng Labs EVA and EVA/480, and the NEC GB-1 (a rebadged EVA/480). The plain EVA model lacks the 25MHz clock that allows 640x480 resolution.

It is comprised of three VLSI chipsets in PLCC68 packages:

| Chip   | Function             |
| :----- | :------------------- |
| ET2000 | CRTC / Sequencer     |
| ET2001 | Attribute Controller |
| ET2002 | Graphics Controller  |

A fourth chip, the ET2003 bit-slice processor, was announced but never saw production.

#### Clocking Select Bits

As with most SuperEGAs, the ET2000 in its full incarnation is typically paired with a 25MHz pixel clock - it also has a third crystal, a 19.96608MHz clock that is used as a pixel clock in 132 column modes, as well as clocking the memory address multiplexers.

| bits | clock select                        |
| :--- | :---------------------------------- |
| 00   | 14.381818MHz (OSC pin from ISA bus) |
| 01   | 16.257MHz                           |
| 10   | 25MHz or external OSC (J3)          |
| 11   | 19.96608MHz                         |

#### Extended General Registers

| Port | Access | Description          |
| :--- | :----- | :------------------- |
| 7CXh | W      | CMII Activation Port |
| 3C8h | W      | CMII Command Port    |

These are essentially the same decoded port - the CMII compatibility module will respond to A10 set as a special 'wake' address. It must be written to twice, with a data byte that has bits 7 and 6 set, to activate the card and begin hooking IO writes for translation.

#### Extended CRTC Registers

| Index   | Name                               | Access | Description                               |
| :------ | :--------------------------------- | :----- | :---------------------------------------- |
| **19h** | Overflow #2                        | W      | High bits for V-Total, V-Display, V-Sync  |
| **1Ah** | ?                                  | W      | ET2000 BIOS sets bit 1 then reads 12h (?) |
| **1Bh** | X Zoom Start Column                | ?      | Character clock of zoom viewport start    |
| **1Ch** | X Zoom End Column                  | ?      | Character clock of zoom viewport end      |
| **1Dh** | Y Zoom Start Scanline              | ?      | Scanline on which zoom viewport starts    |
| **1Eh** | Y Zoom End Scanline                | ?      | Scanline on which zoom viewport ends      |
| **1Fh** | Y Zoom Start and End Scanline High | ?      |                                           |
| **20h** | Zoom Start Address Low             | ?      |                                           |
| **21h** | Zoom Start Address Middle          | ?      |                                           |
| **22h** | ?                                  | ?      |                                           |
| **23h** | ?                                  | ?      |                                           |
| **24h** | ?                                  | ?      |                                           |
| **25h** | ?                                  | ?      |                                           |

#### Extended Sequencer Registers

| Index   | Name             | Access | Description                                |
| :------ | :--------------- | :----- | :----------------------------------------- |
| **06h** | Zoom Timing      | W      | Controls timings for zoom/viewport feature |
| **07h** | Character Timing | W      | Set to 03, 02 or 01 in large column modes  |

#### Extended Graphics Controller Registers

| Index   | Name | Access | Description      |
| :------ | :--- | :----- | :--------------- |
| **0Dh** | ?    | W      | Initialized to 0 |

#### Extended Attribute Controller Registers

| Index   | Name | Access | Description                   |
| :------ | :--- | :----- | :---------------------------- |
| **14h** | ?    | W      | Initialized to 0              |
| **15h** | ?    | W      | Initialized to 0              |
| **16h** | ?    | W      | Bit 1 set in 132 column modes |