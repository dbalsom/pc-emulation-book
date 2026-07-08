# Floppy Drive Controller

IBM PC/XT systems outfitted with a floppy drive had an "IBM 5.25" Diskette Drive Adapter" card installed in one of the available expansion slots. 

For a good look at the Diskette Drive Adapter, see [minuszerodegrees.net](https://www.minuszerodegrees.net/5150_5160/cards/5150_5160_cards.htm#floppy_adapter).

## At a Glance

| Item                 | Description                                    |
| -------------------- | ---------------------------------------------- |
| Controller IC        | NEC **µPD765A** or Intel **P8272A**            |
| Adapter clock        | **16.0MHz** crystal; **8MHz** controller clock |
| Supported drives     | Up to **4**                                    |
| DMA Channel          | **Channel 2**                                  |
| Interrupt            | **IRQ6**                                       |
| Primary I/O range    | `3F0h`-`3F7h`                                  |
| Secondary I/O range  | `370h`-`377h`                                  |
| DOR                  | `3F2h` primary, `372h` secondary               |
| Main status register | `3F4h` primary, `374h` secondary               |
| Data register        | `3F5h` primary, `375h` secondary               |
| Expansion ROM        | None                                           |


## Controller Overview

The IBM floppy drive controller, as we'll refer to it here, was a collection of 74-series logic chips and a 16.0Mhz clock crystal supporting the "brain" of the card, a **NEC µPD765A** (NEC 765) floppy drive controller chip (or the more-or-less identical **Intel P8272A**). 

> [!NOTE]
> Die photography of the P8272A has revealed the numbers '765' directly on the die - implying Intel licensed NEC's design.

The IBM floppy controller could support up to four floppy disk drives, although configurations of more than two were uncommon. Drives 0-3 would be assigned the drive letters A-D up until MS-DOS 5.0, whereupon DOS started to reserve drive letter C for hard disks. It might feel a bit cursed to have a floppy disk as drive C, but if you did indeed have three drives connected and an earlier version of MS-DOS, that's what you'd end up with.

The NEC 765 takes an 8MHz clock, divided once from the card's 16Mhz crystal. 

The 765 doesn't perform every function needed by a floppy controller. Notably, the controller's **voltage-controlled oscillator** (VCO), a crucial part of the controller's **phase-locked-loop** (PLL) is external to the 765, although the 765 has pins for interacting with it. Also external to the 765 is the **data separator** circuitry. 

### Operation

On the IBM PC/XT, the floppy drive controller is operated by the BIOS in DMA mode exclusively. It is possible to operate the controller in **polled-io mode** (PIO) in a manual fashion, but there are severe disadvantages to doing so - as was seen on the IBM PCjr which lacked a DMA controller. The lack of DMA prevented such operations as transferring data via the serial ports and floppy disk drive at the same time.

The 765 operates as a state machine with three basic operational phases:

 - During the **command phase** the controller receives bytes from the host that instruct it to perform a specific operation.
 - During the **execution phase** the controller carries out the operation specified in the command phase.
 - During the **result phase** the controller provides status information to the host describing the result of the execution phase.

The 765 is capable of running some operations, such as **seek** and **recalibrate**, on multiple drives simultaneously. 

### I/O Ports

The IBM Diskette Drive Adapter decodes the following IO port addresses:

| Primary | Secondary | 765 Port | RW  | Description             |
| ------- | --------- | -------- | --- | ----------------------- |
| `3F0h`  | `370h`    | n/a      |     | Base Address            |
| `3F2h`  | `372h`    | n/a      | W   | Digital Output Register |
| `3F4h`  | `374h`    | 0        | R   | µPD765A Status Register |
| `3F5h`  | `375h`    | 1        | RW  | µPD765A Data Register   |

## The Digital Output Register

The IBM controller card adds a main control register external to the 765, called the **Digital Output Register** or DOR. The DOR has several functions - it selects a specific drive as the target of operations, it can reset the 765, it can enable or disable interrupts and DMA, and it can turn on and off the attached floppy drive motors.

The DOR is a **write-only** register implemented with an 74LS273 8-bit register chip. 

{{#bitfield floppy_controller.toml#digital-output-register}}

### Drive Selection Bits

The two least significant bits (Bits 0-1) of the DOR control which floppy drive is selected. 

> [!IMPORTANT]
> If a drive's motor is not on, selecting it in the DOR will do nothing until the motor is turned on.

> [!NOTE]
> To avoid confusion, be aware that the DOR is the only drive selection method used by the IBM floppy drive controller. The NEC 765 command set includes fields that select which drive the operation is intended to target. Under IBM's controller design, these bits do nothing externally - the 765 is not in control of which drive is selected. You can verify this yourself by noting the 765's **unit select** pins, 28 and 29, are not connected on the schematic.

### Reset Bit

The DOR's \\(\overline{\mathrm{RESET}}\\) bit 2 drives the 765's active-high **RST** pin (1) via an inverter. When a `1` is written to bit 2, the 765's **RST** pin is pulled low, holding the controller in reset. 

> [!NOTE]
> The IBM floppy controller card ties the 765's **RDY** pin (35) high. This causes the 765 to generate an interrupt after coming out of the RESET state after "1-25ms", according to the datasheet. The controller is reset quite often during normal operation.

## The 765 Registers

The 765 contains **five** status registers in total. The first of these is the **main status register** (MSR). The MSR is the only status register that may be read at any time. The contents of the other status registers, **ST0—ST3**, are sent to host during the controller **result phase**. 

### The Main Status Register

{{#bitfield floppy_controller.toml#main-status-register}}

#### The BUSY bit

The **BUSY** bit is set when the controller is executing a command, and is only cleared when the last byte of the **result phase** has been read by the host CPU. It can be used as a general indication that a new command should not be sent to the CPU.

#### The DIO bit

The **DIO** bit controls the direction of transfer to or from the controller. The CPU should only send data to the controller when **DIO** is `0`. When **DIO** is `1`, the controller is not ready to receive data — it expects to have data to send to the CPU.

#### The MRQ bit

The **MRQ** bit can be usefully combined with the **DIO** bit to control data transfer to and from the controller.

| DIO | MRQ | Meaning                                                                                                       |
| --- | --- | ------------------------------------------------------------------------------------------------------------- |
| 0   | 0   | FDC is not ready to receive a byte from the CPU. (Busy, reset/disabled, or DMA operation in progress)         |
| 0   | 1   | FDC is ready and expecting to receive a command or data byte from the CPU via the data register.              |
| 1   | 0   | FDC has data pending, but not yet ready to read.                                                              |
| 1   | 1   | FDC has a byte ready for the CPU to read from the data register. Result bytes, sense bytes, or PIO read data. |

> [!NOTE]
> This bit may also be labelled as `RQM` in technical references. 

### Status Register 0 (ST0)

{{#bitfield floppy_controller.toml#status-register-0}}

### Status Register 1 (ST1)

{{#bitfield floppy_controller.toml#status-register-1}}

#### The No-Data Bit

The **No-Data** bit is set under the following conditions:

 - The FDC could not find the requested sector during execution of `READ DATA`, `WRITE DELETED DATA` or `SCAN`
 - The FDC could not read the ID field during execution of `READ ID`
 - The FDC could not find the starting sector during execution of `READ CYLINDER`.

### Status Register 2 (ST2)

{{#bitfield floppy_controller.toml#status-register-2}}

### Status Register 3 (ST3)

{{#bitfield floppy_controller.toml#status-register-3}}

> [!IMPORTANT]
> Remember that on the IBM floppy controller, the 765's unit select pins are not connected and do not drive selection of floppy drives. 

## Controller Commands

The 765 supports **15** different commands:
| Code  |                    Command Name                     |  MT  |  MF  |  SK  |
| :---: | :-------------------------------------------------: | :--: | :--: | :--: |
| `06h` |         [Read Data](#the-read-data-command)         | ✔️ | ✔️ | ✔️ |
| `0Ch` | [Read Deleted Data](#the-read-deleted-data-command) | ✔️ | ✔️ | ✔️ |
| `0Ah` |           [Read ID](#the-read-id-command)           |  0   | ✔️ |  0   |
| `02h` |        [Read Track](#the-read-track-command)        |  0   | ✔️ | ✔️ |
| `11h` |          [Scan Equal](#the-scan-commands)           | ✔️ | ✔️ | ✔️ |
| `19h` |       [Scan Low or Equal](#the-scan-commands)       | ✔️ | ✔️ | ✔️ |
| `1Dh` |      [Scan High or Equal](#the-scan-commands)       | ✔️ | ✔️ | ✔️ |
| `03h` |           [Specify](#the-specify-command)           |  0   |  0   |  0   |
| `05h` |                     Write Data                      | ✔️ | ✔️ |  0   |
| `09h` |                 Write Deleted Data                  | ✔️ | ✔️ |  0   |
| `0Fh` |                        Seek                         |  0   |  0   |  0   |
| `0Dh` |                   Format a Track                    |  0   | ✔️ |  0   |
| `07h` |                     Recalibrate                     |  0   |  0   |  0   |
| `08h` |               Sense Interrupt Status                |  0   |  0   |  0   |
| `04h` |                 Sense Drive Status                  |  0   |  0   |  0   |

Commands consist of **2—9** command bytes, sent during the **command phase**. The command will then enter the **execution phase**. When complete (or on error) the command enters the **result phase** and various status register bytes will be made available to read out from the data register.

The first **command code byte 0** is common to all commands and contains the **command code** as given in the table above, along with operational flags. These flags are not always applicable to each command. The flags applicable to each command are noted in the table above.

### Command Code Byte 0

{{#bitfield floppy_controller.toml#command-code-0}}

### Command Code Byte 1

{{#bitfield floppy_controller.toml#command-byte-drive-head}}

### The Read Data Command

The **Read Data** command is opcode `06h`. 

The **Read Data** command searches for the sector ID matching the specified cylinder, head, sector and sector size. The matching sector must have a normal **data address mark** (DAM).

In **DMA mode**, it will read successive sectors that have a normal DAM until terminal count. In **PIO mode**, it will read successive sectors that have a normal DAM until `EOT` is reached. 

If the **MT** flag is set, once the last sector of **side 0** is transferred, the FDC proceeds to repeat the operation on **side 1**.

The **Read Data** command behaves as follows depending on the value of the **SK** flag:
| SK  | DAM Type | Sector Read | CM  | Result                  |
| :-- | :------- | :---------- | :-- | :---------------------- |
| 0   | Normal   | Y           | 0   | Normal Termination      |
| 0   | Deleted  | Y           | 1   | No Further Sectors Read |
| 1   | Normal   | Y           | 0   | Normal Termination      |
| 1   | Deleted  | N           | 1   | Sector Skipped          |

After the data is transferred, the command enters the **result phase**.

#### Status Flags Affected

| Flag | Register | Triggering Event |
|------|-------|-------|
| WC | [ST2](#status-register-2-st2) | Value of `C` mismatch in Sector ID  |
| BC | [ST2](#status-register-2-st2) | Value of `C` mismatch in Sector ID and `C` was `0xFF` |
| CM | [ST2](#status-register-2-st2) | A **deleted data address mark** (DDAM) was encountered |
| ND | [ST1](#status-register-1-st1) | No matching Sector ID was found |
| MA | [ST1](#status-register-1-st1) | No **sector ID address mark** (IDAM) was found within two index pulses |
| DE | [ST1](#status-register-1-st1) | A bad data field CRC was encountered |

#### Command Format

|  Phase  | Byte |                    Byte                     |
| :-----: |:----:| :-----------------------------------------: |
| Command |0| [Command Code Byte 0](#command-code-byte-0) |
| Command |1| [Command Code Byte 1](#command-code-byte-1) |
| Command |2|                  Cylinder                   |
| Command |3|                    Head                     |
| Command |4|                   Sector                    |
| Command |5|               Sector Size (N)               |
| Command |6|                End of Track                 |
| Command |7|                Gap 3 Length                 |
| Command |8|              Data Length (DTL)              |
| Result  |0|        [ST0](#status-register-0-st0)        |
| Result  |1|        [ST1](#status-register-1-st1)        |
| Result  |2|        [ST2](#status-register-2-st2)        |
| Result  |3|                  Cylinder                   |
| Result  |4|                    Head                     |
| Result  |5|                   Sector                    |
| Result  |6|               Sector Size (N)               |

### The Read Deleted Data Command

The **Read Deleted Data** command is opcode `0Ch`. 

The **Read Deleted Data** command searches for the sector ID matching the specified cylinder, head, sector and sector size. The matching sector must have a normal **deleted data address mark** (DDAM).

In **DMA mode**, it will read successive sectors that have a DDAM until terminal count. In **PIO mode**, it will read successive sectors that have a DDAM until `EOT` is reached. 

If the **MT** flag is set, once the last sector of **side 0** is transferred, the FDC proceeds to repeat the operation on **side 1**.

The **Read Deleted Data** command behaves as follows depending on the value of the **SK** flag:
| SK  | DAM Type | Sector Read | CM  | Result                  |
| :-- | :------- | :---------- | :-- | :---------------------- |
| 0   | Normal   | Y           | 1   | No Further Sectors Read      |
| 0   | Deleted  | Y           | 0   | Normal Termination |
| 1   | Normal   | N           | 1   | Sector Skipped      |
| 1   | Deleted  | Y           | 0   | Normal Termination          |

After the data is transferred, the command enters the **result phase**.

#### Status Flags Affected

| Flag | Register | Triggering Event |
|------|-------|-------|
| WC | [ST2](#status-register-2-st2) | Value of `C` mismatch in Sector ID  |
| BC | [ST2](#status-register-2-st2) | Value of `C` mismatch in Sector ID and `C` was `0xFF` |
| CM | [ST2](#status-register-2-st2) | A **normal data address mark** (DAM) was encountered |
| ND | [ST1](#status-register-1-st1) | No matching Sector ID was found |
| MA | [ST1](#status-register-1-st1) | No **sector ID address mark** (IDAM) was found within two index pulses |
| DE | [ST1](#status-register-1-st1) | A bad data field CRC was encountered |

#### Command Format

|  Phase  | Byte |                    Byte                     |
| :-----: | :--: | :-----------------------------------------: |
| Command |  0   | [Command Code Byte 0](#command-code-byte-0) |
| Command |  1   | [Command Code Byte 1](#command-code-byte-1) |
| Command |  2   |                  Cylinder                   |
| Command |  3   |                    Head                     |
| Command |  4   |                   Sector                    |
| Command |  5   |               Sector Size (N)               |
| Command |  6   |                End of Track                 |
| Command |  7   |                Gap 3 Length                 |
| Command |  8   |              Data Length (DTL)              |
| Result  |  0   |        [ST0](#status-register-0-st0)        |
| Result  |  1   |        [ST1](#status-register-1-st1)        |
| Result  |  2   |        [ST2](#status-register-2-st2)        |
| Result  |  3   |                  Cylinder                   |
| Result  |  4   |                    Head                     |
| Result  |  5   |                   Sector                    |
| Result  |  6   |               Sector Size (N)               |

### The Read ID Command

The **Read ID** command is opcode `0Ah`.

The FDC returns the fields of the next **Sector ID** encountered on the track.

The **MT** and **SK** flags are *not* valid for this command and should be `0`.

#### Status Flags Affected

| Flag | Register | Triggering Event |
|------|-------|-------|
| MA | [ST1](#status-register-1-st1) | No **sector ID address mark** (IDAM) was found within two index pulses |

#### Command Format

|  Phase  | Byte |                    Byte                     |
| :-----: |:----:| :-----------------------------------------: |
| Command |0| [Command Code Byte 0](#command-code-byte-0) |
| Command |1| [Command Code Byte 1](#command-code-byte-1) |
| Result  |0|        [ST0](#status-register-0-st0)        |
| Result  |1|        [ST1](#status-register-1-st1)        |
| Result  |2|        [ST2](#status-register-2-st2)        |
| Result  |3|                  Cylinder                   |
| Result  |4|                    Head                     |
| Result  |5|                   Sector                    |
| Result  |6|               Sector Size (N)               |

### The Read Track Command

The **Read Track** command is opcode `02h`.

Unlike what its name might suggest, **Read Track** does not actually read a raw track. Instead, it reads all sectors on a track, regardless of ID or CRC validation.

The **Read Track** command first waits for the index signal. It then returns the data for each sector encountered, in order. The **Sector ID** of the first sector is checked against the values given to the command for the purposes of setting the **ND** bit in [ST1](#status-register-1-st1), but a mismatch is not an error and does not stop command execution.

The **MT** and **SK** flags are *not* valid for this command and should be `0`.

#### Status Flags Affected

| Flag | Register                      | Triggering Event                                         |
| :--- | :---------------------------- | :------------------------------------------------------- |
| ND   | [ST1](#status-register-1-st1) | Sector ID comparison failed (command continues)          |
| DD   | [ST2](#status-register-2-st2) | A bad data field CRC was encountered (command continues) |
| DE   | [ST1](#status-register-1-st1) | A bad field CRC was encountered (command continues)      |

#### Command Format

|  Phase  | Byte |                    Byte                     |
| :-----: |:----:| :-----------------------------------------: |
| Command |0| [Command Code Byte 0](#command-code-byte-0) |
| Command |1| [Command Code Byte 1](#command-code-byte-1) |
| Result  |0|        [ST0](#status-register-0-st0)        |
| Result  |1|        [ST1](#status-register-1-st1)        |
| Result  |2|        [ST2](#status-register-2-st2)        |
| Result  |3|                  Cylinder                   |
| Result  |4|                    Head                     |
| Result  |5|                   Sector                    |
| Result  |6|               Sector Size (N)               |

### The Scan Commands

The three scan commands, **Scan Equal**, **Scan High or Equal**, and **Scan Low or Equal**, behave identically other than the mathematical expression they evaluate for each pair of bytes processed.

In each of the three commands, the FDC performs a comparison (the **scan condition**) between bytes read from the disk and bytes provided by the host. If this comparison is true for the entire sector, the scan condition is said to have been **satisfied** or tha a **scan hit** has occurred, at which point the scan operation will enter the **result phase**.

The value of `FFh` is special, and is treated as a wildcard. If either the byte from the disk or the byte from the host is `FFh` then the comparison will be considered **true**. This allows use of `FFh` by the host to mask the comparison bytes provided to the FDC.

If a sector does not satisfy the scan condition, the FDC will continue with the next sector to scan based on the **STP** step parameter. If **STP** == `1`, this will be the next consecutive sector number. If **STP** == `2`, then the FDC will skip the next consecutive sector number. 

> [!IMPORTANT]
> Regardless of the **STP** parameter, the FDC must be read the last sector on the track as specified by EOT. Unexpectedly encountering the index pulse during the scan operation will result in abnormal termination.

If EOT is reached or terminal count occurs before a scan hit occurs, then the scan operation ends with a **scan not satisfied** condition. In the case of a terminal count, the operation ends after the current byte being compared. 


#### Scan Command Operations

| Code | Command | Effective Operation |
|--|---------|---------------------|
| `11h` | Scan Equal | (Byte from Disk) == (Byte from CPU)|
| `19h` | Scan Low or Equal | (Byte From Disk) ≤ (Byte from CPU)|
| `1Dh` | Scan High or Equal | (Byte From Disk) ≤ (Byte from CPU)|

#### Status Flags Affected

| Flag | Register                      | Triggering Event                                         |
| :--- | :---------------------------- | :------------------------------------------------------- |
| OR   | [ST1](#status-register-1-st1) | An overrun condition occurred during the scan operation  |
| SH   | [ST2](#status-register-2-st2) | The scan condition was satisfied (scan hit)              |
| SN   | [ST2](#status-register-2-st2) | The scan condition was not satisfied                     |
| CM   | [ST2](#status-register-2-st2) | A **deleted data address mark** (DDAM) was encountered   |

#### Command Format

|  Phase  | Byte |                    Byte                     |
| :-----: | :--: | :-----------------------------------------: |
| Command |  0   | [Command Code Byte 0](#command-code-byte-0) |
| Command |  1   | [Command Code Byte 1](#command-code-byte-1) |
| Command |  2   |                  Cylinder                   |
| Command |  3   |                    Head                     |
| Command |  4   |                   Sector                    |
| Command |  5   |               Sector Size (N)               |
| Command |  6   |                End of Track                 |
| Command |  7   |                Gap 3 Length                 |
| Command |  8   |           Sector Step Size (STP)            |
| Result  |  0   |        [ST0](#status-register-0-st0)        |
| Result  |  1   |        [ST1](#status-register-1-st1)        |
| Result  |  2   |        [ST2](#status-register-2-st2)        |
| Result  |  3   |                  Cylinder                   |
| Result  |  4   |                    Head                     |
| Result  |  5   |                   Sector                    |
| Result  |  6   |               Sector Size (N)               |

### The Specify Command

The **Specify** command sets three timing variables for the drive as well as setting the FDC operational mode to **DMA** or **PIO** modes. 


The **Specify** command has no result phase.

#### Command Format

|  Phase  | Byte |                    Byte                     |
| :-----: | :--: | :-----------------------------------------: |
| Command |  0   | [Command Code Byte 0](#command-code-byte-0) |
| Command |  1   | [Specify Timing 0](#command-byte-specify-timing-0) |
| Command |  2   | [Specify Timing 1](#command-byte-specify-timing-1) |

{{#bitfield h4 floppy_controller.toml#command-byte-specify-timing-0}}

{{#bitfield h4 floppy_controller.toml#command-byte-specify-timing-1}}

## Invalid Commands

Any unrecognized or unsupported command code will return a single [ST0](#status-register-0-st0) byte with a **IC** of `10b`, or **abnormal termination**. The value of the ST0 byte in hexadecimal will be `80h`.


## Datasheet

 - (archive.org) [μPD765A Single/Double Density Floppy Disk Controller](https://archive.org/details/ibm_pc_datasheets/Controller%20Chips/NEC%20upd765%20Floppy%20Controller/upd765a/)

## Primary References

 - (archive.org) [IBM 5-1/4" Diskette Drive Adapter](https://archive.org/details/ibm_pc_datasheets/Expansion%20Cards/IBM%205_25%20Diskette%20Drive%20Adapter/)

 - (debs.future.easyspace.com @ web.archive.org) [Programming Floppy Disk Controllers](https://web.archive.org/web/20041010081013/http://debs.future.easyspace.com/Programming/Hardware/FDC/floppy.html)