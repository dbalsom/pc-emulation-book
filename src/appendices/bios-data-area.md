# The BIOS Data Area (BDA) 

The BIOS Data Area (BDA) is a 257-byte[^1] region of memory located at segment 0x0040 (physical address 0x00400). 

It is used by the BIOS to store system variables and state.

{{#csvtable bda.csv}}

```toml_bitfield
name = "Equipment List Flags"
anchor = "equipment-list-flags"
bits = 16
description = "Bit flags describing the hardware configuration detected by the BIOS"

[[register]]
address = "40:10"

[[fields]]
name = "nPRN"
lsb = 14
width = 2
description = "Number of printer ports installed"

[[fields]]
lsb = 13
width = 1
description = "Reserved"

[[fields]]
name = "GP"
lsb = 12
width = 1
description = "Game port installed"

[[fields]]
name = "nCOM"
lsb = 9
width = 3
description = "Number of serial ports installed"

[[fields]]
name = "DMA"
lsb = 8
width = 1
description = "DMA controller installed (if 0)"

[[fields]]
name = "nFLOP"
lsb = 6
width = 2
description = "Number of floppy drives installed, -1"

[[fields]]
name = "VM"
lsb = 4
width = 2
description = "Initial video mode at boot time"

[[fields]]
name = "RAM"
lsb = 2
width = 2
description = "Onboard RAM installed (first 256K)"

[[fields]]
name = "FPU"
lsb = 1
width = 1
description = "FPU installed"

[[fields]]
name = "IPL"
lsb = 0
width = 1
description = "Floppy drive installed"
```

```toml_bitfield
name = "Keyboard Flag Byte 0"
anchor = "keyboard-flag-byte-0"
bits = 8
description = "Primary keyboard status flags"

[[register]]
address = "40:17"

[[fields]]
name = "INS"
lsb = 7
width = 1
description = "Insert active"

[[fields]]
name = "CAPS"
lsb = 6
width = 1
description = "Caps-Lock active"

[[fields]]
name = "NUM"
lsb = 5
width = 1
description = "Num-Lock active"

[[fields]]
name = "SCRL"
lsb = 4
width = 1
description = "Scroll-Lock active"

[[fields]]
name = "ALT"
lsb = 3
width = 1
description = "ALT key depressed"

[[fields]]
name = "CTRL"
lsb = 2
width = 1
description = "CTRL key depressed"

[[fields]]
name = "LSHFT"
lsb = 1
width = 1
description = "Left Shift key depressed"

[[fields]]
name = "RSHFT"
lsb = 0
width = 1
description = "Right Shift key depressed"
```

```toml_bitfield
name = "Keyboard Flag Byte 1"
anchor = "keyboard-flag-byte-1"
bits = 8
description = "Secondary keyboard status flags"

[[register]]
address = "40:18"

[[fields]]
name = "INS"
lsb = 7
width = 1
description = "Insert key depressed"

[[fields]]
name = "CAPS"
lsb = 6
width = 1
description = "Caps-Lock key depressed"

[[fields]]
name = "NUM"
lsb = 5
width = 1
description = "Num-Lock key depressed"

[[fields]]
name = "SCRL"
lsb = 4
width = 1
description = "Scroll-Lock key depressed"

[[fields]]
name = "SUSP"
lsb = 3
width = 1
description = "Suspend key has been toggled"

[[fields]]
name = "SYS"
lsb = 2
width = 1
description = "System key depressed and held"

[[fields]]
name = "LALT"
lsb = 1
width = 1
description = "Left ALT key depressed"

[[fields]]
name = "LCTRL"
lsb = 0
width = 1
description = "Left CTRL key depressed"
```

```toml_bitfield
name = "Floppy Recalibration Status"
anchor = "floppy-recalibrate-status"
bits = 8
description = "Interrupt and calibration status for floppy drives"

[[register]]
address = "40:3E"

[[fields]]
name = "INT"
lsb = 7
width = 1
description = "Working interrupt flag (1=working)"

[[fields]]
lsb = 4
width = 3
description = "Unused"

[[fields]]
name = "DRV3"
lsb = 3
width = 1
description = "1 = Recalibrate drive 3"

[[fields]]
name = "DRV2"
lsb = 2
width = 1
description = "1 = Recalibrate drive 2"

[[fields]]
name = "DRV1"
lsb = 1
width = 1
description = "1 = Recalibrate drive 1"

[[fields]]
name = "DRV0"
lsb = 0
width = 1
description = "1 = Recalibrate drive 0"
```

```toml_bitfield
name = "Floppy Motor Status"
anchor = "floppy-motor-status"
bits = 8
description = "Current state of floppy drive motors"

[[register]]
address = "40:3F"

[[fields]]
name = "WR"
lsb = 7
width = 1
description = "Write operation in progress"

[[fields]]
lsb = 4
width = 3
description = "Unused"

[[fields]]
name = "DRV3"
lsb = 3
width = 1
description = "1 = Drive 3 motor on"

[[fields]]
name = "DRV2"
lsb = 2
width = 1
description = "1 = Drive 2 motor on"

[[fields]]
name = "DRV1"
lsb = 1
width = 1
description = "1 = Drive 1 motor on"

[[fields]]
name = "DRV0"
lsb = 0
width = 1
description = "1 = Drive 0 motor on"
```

```toml_bitfield
name = "Floppy Controller Status"
anchor = "floppy-controller-status"
bits = 8
description = "Status bytes returned from the floppy controller from the last disk operation (INT 13,1)"

[[register]]
address = "40:41"

[[fields]]
name = "TMO"
lsb = 7
width = 1
description = "Floppy time-out"

[[fields]]
name = "SEEK"
lsb = 6
width = 1
description = "Seek to track failed"

[[fields]]
name = "FAIL"
lsb = 5
width = 1
description = "Floppy controller failure"

[[fields]]
name = "CRC"
lsb = 4
width = 1
description = "CRC check / data error"

[[fields]]
name = "DMA"
lsb = 3
width = 1
description = "Floppy controller DMA error"

[[fields]]
name = "SEC"
lsb = 2
width = 1
description = "Sector not found"

[[fields]]
name = "ADDR"
lsb = 1
width = 1
description = "Address mark not found"

[[fields]]
name = "CMD"
lsb = 0
width = 1
description = "Invalid floppy controller command"
```

```toml_bitfield
name = "Video Mode Options (EGA+)"
anchor = "video-mode-options"
bits = 8
description = "EGA/VGA video mode flags"

[[register]]
address = "40:87"

[[fields]]
name = "MODE"
lsb = 7
width = 1
description = "Video mode number passed to INT 10, function 0 (Bit 7)"

[[fields]]
name = "RAM"
lsb = 5
width = 2
description = "Video RAM: 00=64K, 01=128K, 10=192K, 11=256K"

[[fields]]
lsb = 4
width = 1
description = "Reserved"

[[fields]]
name = "INACT"
lsb = 3
width = 1
description = "1 = Video subsystem is inactive"

[[fields]]
lsb = 2
width = 1
description = "Reserved"

[[fields]]
name = "MONO"
lsb = 1
width = 1
description = "1 = Video subsystem attached to monochrome"

[[fields]]
name = "CURS"
lsb = 0
width = 1
description = "1 = Alphanumeric cursor emulation enabled"
```

```toml_bitfield
name = "EGA DIP and Feature Switches"
anchor = "ega-dip-switches"
bits = 8
description = "EGA feature bit switches (emulated on VGA)"

[[register]]
address = "40:88"

[[fields]]
name = "FEAT1"
lsb = 7
width = 1
description = "Input FEAT1 (ISR0 bit 6) after output on FCR1"

[[fields]]
name = "FEAT1"
lsb = 6
width = 1
description = "Input FEAT1 (ISR0 bit 5) after output on FCR1"

[[fields]]
name = "FEAT0"
lsb = 5
width = 1
description = "Input FEAT0 (ISR0 bit 6) after output on FCR0"

[[fields]]
name = "FEAT0"
lsb = 4
width = 1
description = "Input FEAT0 (ISR0 bit 5) after output on FCR0"

[[fields]]
name = "SW4"
lsb = 3
width = 1
description = "EGA SW4 config (1=off)"

[[fields]]
name = "SW3"
lsb = 2
width = 1
description = "EGA SW3 config (1=off)"

[[fields]]
name = "SW2"
lsb = 1
width = 1
description = "EGA SW2 config (1=off)"

[[fields]]
name = "SW1"
lsb = 0
width = 1
description = "EGA SW1 config (1=off)"
```


```toml_bitfield
name = "Video Display Data (MCGA/VGA)"
anchor = "video-display-data"
bits = 8
description = "MCGA and VGA specific status. Bits 7 and 4 control scan lines."

[[register]]
address = "40:89"

[[fields]]
name = "SL_HI"
lsb = 7
width = 1
description = "Scan Line Select Bit 1 (00=350, 01=400, 10=200)"

[[fields]]
lsb = 5
width = 2
description = "Reserved"

[[fields]]
name = "SL_LO"
lsb = 4
width = 1
description = "Scan Line Select Bit 0"

[[fields]]
name = "PAL"
lsb = 3
width = 1
description = "1 = Default palette loading is disabled"

[[fields]]
name = "MONO"
lsb = 2
width = 1
description = "1 = Using monochrome monitor"

[[fields]]
name = "GRAY"
lsb = 1
width = 1
description = "1 = Gray scale is enabled"

[[fields]]
name = "VGA"
lsb = 0
width = 1
description = "1 = VGA is active"
```

```toml_bitfield
name = "Floppy Media Control"
anchor = "floppy-media-control"
bits = 8
description = "Last selected floppy drive data and step rates"

[[register]]
address = "40:8B"

[[fields]]
name = "RATE"
lsb = 6
width = 2
description = "Data Rate: 00=500K, 01=300K, 10=250K"

[[fields]]
name = "STEP"
lsb = 4
width = 2
description = "Step Rate: 00=0C, 01=0D, 10=0A"

[[fields]]
lsb = 0
width = 4
description = "Reserved"
```

```toml_bitfield
name = "Floppy Media Status"
anchor = "floppy-media-status"
bits = 8
description = "Media status for Drives 0-3 (4 copies at 40:90..93)"

[[register]]
address = "40:90"

[[fields]]
name = "RATE"
lsb = 6
width = 2
description = "Data Rate: 00=500K, 01=300K, 10=250K"

[[fields]]
name = "DBL"
lsb = 5
width = 1
description = "Double stepping required"

[[fields]]
name = "EST"
lsb = 4
width = 1
description = "1 = Media/drive established"

[[fields]]
lsb = 3
width = 1
description = "Reserved"

[[fields]]
name = "STATE"
lsb = 0
width = 3
description = "Drive/Media State"
```

```toml_bitfield
name = "Keyboard Mode/Type"
anchor = "keyboard-mode-byte"
bits = 8
description = "Extended keyboard status flags"

[[register]]
address = "40:96"

[[fields]]
name = "RD_ID"
lsb = 7
width = 1
description = "Read ID in process"

[[fields]]
name = "ID_CH"
lsb = 6
width = 1
description = "Last char was first ID char"

[[fields]]
name = "NUM"
lsb = 5
width = 1
description = "Force Num-Lock if Rd ID & KBX"

[[fields]]
name = "101"
lsb = 4
width = 1
description = "101/102 enhanced keyboard installed"

[[fields]]
name = "R_ALT"
lsb = 3
width = 1
description = "Right ALT key depressed"

[[fields]]
name = "R_CTL"
lsb = 2
width = 1
description = "Right CTRL key depressed"

[[fields]]
name = "E0"
lsb = 1
width = 1
description = "Last code was the E0 hidden code"

[[fields]]
name = "E1"
lsb = 0
width = 1
description = "Last code was the E1 hidden code"
```

```toml_bitfield
name = "Keyboard LED Flags"
anchor = "keyboard-led-state"
bits = 8
description = "Status of keyboard indicators and transmission"

[[register]]
address = "40:97"

[[fields]]
name = "ERR"
lsb = 7
width = 1
description = "Keyboard transmit error flag"

[[fields]]
name = "MODE"
lsb = 6
width = 1
description = "Mode indicator update"

[[fields]]
name = "RSND"
lsb = 5
width = 1
description = "Re-send received flag"

[[fields]]
name = "ACK"
lsb = 4
width = 1
description = "ACK received"

[[fields]]
name = "CIRC"
lsb = 3
width = 1
description = "Circus system indicator"

[[fields]]
name = "CAPS"
lsb = 2
width = 1
description = "Caps-Lock indicator"

[[fields]]
name = "NUM"
lsb = 1
width = 1
description = "Num-Lock indicator"

[[fields]]
name = "SCRL"
lsb = 0
width = 1
description = "Scroll-Lock indicator"
```


```toml_bitfield
name = "RTC Wait Function Flags"
anchor = "rtc-wait-flags"
bits = 8
description = "INT 15,86 RTC wait function status"

[[register]]
address = "40:A0"

[[fields]]
name = "ELAP"
lsb = 7
width = 1
description = "1 = INT 15,86 wait time elapsed"

[[fields]]
lsb = 1
width = 6
description = "Unused"

[[fields]]
name = "PEND"
lsb = 0
width = 1
description = "1 = Wait pending"
```

## Primary Emulation Resources

 - (helppc.netcore2k.net) [BDA - BIOS Data Area - PC Memory Map](https://helppc.netcore2k.net/table/bios-data-area)

## References

[^1]: [Intel® Platform Innovation Framework for EFI Compatibility Support Module Specification, Revision 0.97](https://www.intel.com/content/dam/doc/reference-guide/efi-compatibility-support-module-specification-v097.pdf), September 4, 2007.
