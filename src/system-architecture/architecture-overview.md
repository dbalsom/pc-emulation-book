# IBM PC/XT Architecture Overview

The design of the original IBM 5150 reflected IBM's project requirements to create a low-cost, maintainable system largely comprised of off-the-shelf parts, yet capable of being expanded. They succeeded in that effort far beyond any conceivable expectations - the IBM PC is now recognized as the ancestor of a line of "PC Compatible" systems that continue to be sold to this day.

## CPU

IBM chose the Intel 8088 for the 5150, which is also used in the 5160. The 8088 was a lower-cost variant of the 8086 CPU. While still 16-bit internally, the 8088 only had an 8-bit data bus. This simplified the PC's motherboard design, and made it easy to build a system around Intel's various 8-bit peripheral chips. 

The 8088 has 20 address lines, allowing it to address \\(2^{20}\\) bytes, or 1MB.

IBM chose to reserve addresses above `0xA0000`, leading to the infamous "640KB" memory limit that is often mistakenly blamed on Microsoft.

## Expansion Bus

The 8-bit data bus of the 8088 would also dictate the 8-bit data width of the system's expansion bus. This bus would later be expanded to 16-bits with the IBM 5170 AT, and would later be dubbed the [ISA bus](https://en.wikipedia.org/wiki/Industry_Standard_Architecture) by Compaq[^wiki-isa] and a growing consortium of PC clone manufacturers.

## System Clock

The 5150 has a single main system crystal with a frequency of 14.31818MHz. This frequency is exactly four times the [NTSC](https://en.wikipedia.org/wiki/NTSC) color subcarrier frequency.

The crystal frequency can be expressed as a fraction:

$$f_{crystal} = \frac{315}{22} \text{ MHz} = 14.318181\overline{81} \text{ MHz}$$

This choice was likely made due to the low cost of NTSC-derived clock crystals, as they were being manufactured by the millions to be used in television sets. It also made the PC more easily compatible with North American television sets, making low-cost display option available to PC owners. It also allowed the IBM Color Graphics Adapter to omit a separate crystal.

The CPU frequency of 4.77 MHz is obtained by dividing the system clock by 3: 

$$\frac{14.3181818}{3} = 4.773MHz$$ 

The 8088 was rated for 5MHz operation[^8088-datasheet], so this represents about a 5% underclock.


---

## References

[^8088-datasheet]: Intel Corporation. *8088 8-Bit Hmos Microprocessor*. Intel Corporation, August 1990. Document Number: 231456-006. Available at: [Intel 8088 Data Sheet PDF](https://www.ceibo.com/eng/datasheets/Intel-8088-Data-Sheet.pdf)

[^wiki-isa]: wikipedia.org [Industry Standard Architecture](https://en.wikipedia.org/wiki/Industry_Standard_Architecture).