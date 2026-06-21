# IBM PC/XT Architecture Overview

The design of the original IBM 5150 reflected IBM's project requirements to create a low-cost, maintainable system largely comprised of off-the-shelf parts, yet capable of being expanded. They succeeded in that effort far beyond any conceivable expectations - the IBM PC is now recognized as the ancestor of a line of "PC Compatible" systems that continue to be sold to this day.

## CPU

IBM chose the Intel 8088 for the 5150, which is also used in the 5160. The 8088 was a lower-cost variant of the 8086 CPU. While still 16-bit internally, the 8088 only had an 8-bit data bus. This simplified the PC's motherboard design, and made it easy to build a system around Intel's various 8-bit peripheral chips. 

The 8088 has 20 address lines, allowing it to address \\(2^{20}\\) bytes, or 1MB.

IBM chose to reserve addresses above `0xA0000`, leading to the infamous "640KB" memory limit that is often mistakenly blamed on Microsoft.

## Memory

Depending on the model and revision, the PC could be fitted with up to 256K of RAM on the motherboard. Memory expansion cards to bring a system up to the maximum 640KB were quite commonplace in the latter years of the PC's life. **Multi-function cards** provided RAM upgrades along with extra peripherals such as printer, serial, and game ports.

The memory used in the PC is common [dynamic RAM](https://en.wikipedia.org/wiki/Dynamic_random-access_memory) (DRAM). The PC lacks dedicated refresh circuitry to maintain the contents of DRAM, and must use some of its accessory hardware to perform this task. The process of DRAM refresh makes the entire system approximately 6% slower.

## Timer

The PC contains an [Intel 8253 Programmable Interrupt Timer](../support-chips/timer-8253.md) with three timing channels.  

### Timer Channel 0 

The first channel, 0, is dedicated to maintaining the system clock via the BIOS. The PC has no real-time clock or battery-backup, so the date and time must be entered when booting the system. The time-of-day clock is maintained in software, and was notoriously inaccurate. For these reasons, **real-time clock** modules were popular upgrades, often found on multi-function cards. Timer channel 0 is connected to IRQ0 and is the only channel that can generate **timer interrupts*.

### Timer Channel 1

The second channel, 1, is dedicated to the operation of refreshing the system's DRAM and generally cannot be used by programs.

### Timer Channel 2

The third channel, 2, is the only channel connected to the PC Speaker. Programming this channel allows sounds to be played, but it can also be used as a general timing facility.

## DMA

The PC has an [Intel 8237 Direct Memory Access Controller](../support-chips/dma-8237.md). DMA is a method by which expansion cards can read and write to memory without needing the CPU to participate in the transfer, which can make timing-critical operations such as floppy-disk access more reliable, especially if the CPU is busy. DMA was used to operate the PC's floppy drives, and was often used by add-on hard disk controllers. The PC has three DMA channels, one of which is dedicated to the process of DRAM refresh, leaving only two available.

## Interrupts

The PC has an [Intel 8259 Programmable Interrupt Controller](../support-chips/pic-8259.md) with 8 interrupt lines. Interrupts are a way for components of a hardware system to request attention from the CPU.

## Expansion Bus

The 8-bit data bus of the 8088 would also dictate the 8-bit data width of the system's expansion bus. This bus would later be expanded to 16-bits with the IBM 5170 AT, and would later be dubbed the [ISA bus](https://en.wikipedia.org/wiki/Industry_Standard_Architecture) by Compaq[^wiki-isa] and a growing consortium of PC clone manufacturers.

## System Crystal

The 5150 has a single main system crystal with a frequency of 14.31818MHz. This frequency is exactly four times the [NTSC](https://en.wikipedia.org/wiki/NTSC) color subcarrier frequency.

The crystal frequency can be expressed as a fraction:

$$f_{crystal} = \frac{315}{22} \text{ MHz} = 14.31818\overline{18} \text{ MHz}$$

This choice was likely made due to the low cost of NTSC-derived clock crystals, as they were being manufactured by the millions to be used in television sets. It also made the PC more easily compatible with North American television sets, making low-cost display option available to PC owners. It also allowed the IBM Color Graphics Adapter to omit a separate crystal.

## CPU Clock

The CPU frequency of 4.77 MHz is obtained by dividing the system clock by 3: 

$$\frac{14.3181818}{3} = 4.773\text{ MHz}$$ 

The 8088 was rated for 5MHz operation[^8088-datasheet], so this represents about a 5% underclock.

## The PC vs XT

The IBM model 5160 (XT) is very similar to the model 5150 PC, with a few differences:

 - Eight expansion slots vs the PC's five
 - The minimum installed RAM was increased to 128K
 - The underutilized cassette interface port was dropped
 - Slight changes to DRAM refresh logic
 - ROM chip size was increased from 8K to 32K
 - A larger, 130W power supply to accommodate hard drives



---

## References

[^8088-datasheet]: Intel Corporation. *8088 8-Bit Hmos Microprocessor*. Intel Corporation, August 1990. Document Number: 231456-006. Available at: [Intel 8088 Data Sheet PDF](https://www.ceibo.com/eng/datasheets/Intel-8088-Data-Sheet.pdf)

[^wiki-isa]: wikipedia.org [Industry Standard Architecture](https://en.wikipedia.org/wiki/Industry_Standard_Architecture).