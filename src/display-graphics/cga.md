# The IBM Color Graphics Adapter (CGA)

The IBM CGA card was one of the first video adapters available for the IBM PC/XT, along with the IBM Monochrome Display Adapter and the Hercules video adapter.

The CGA could be connected to a regular North American television set via its composite output connector. A digital DE-9 connection eventually allowed it to be connected to the IBM 5153 Color Display, once that was finally released. IBM left owners of the CGA waiting a bit for a proper monitor - it was only released in 1983, two years after the CGA's debut.

The CGA has 16KB of DRAM dedicated to video memory, and a 4KB font ROM that holds bit patterns for drawing text glyphs.

In text mode, the CGA card was capable of outputting 16 colors. In graphics mode, it was limited to 3 palettes of 3 fixed colors each, with a selectable background color.  The CGA also had a high-resolution mode, with a single, selectable foreground color on black.

Like the MDA, the CGA is built around the [Motorola MC6845 CRTC](6845.md). See that section first for a basic understanding of how that chip is used to define display geometry.

## Display Timings

Unlike the MDA, the CGA does not have its own crystal. IBM designed the main system crystal of the PC itself around the NTSC display standard with the apparent intent of simplifying the production of the CGA and other television-compatible peripherals.

The 5150 has a single main system crystal with a frequency of 14.31818MHz. This frequency is exactly four times the [NTSC](https://en.wikipedia.org/wiki/NTSC) color subcarrier frequency.

The crystal frequency can be expressed as a fraction:

$$f_{crystal} = \frac{315}{22} \text{ MHz} = 14.318181\overline{81} \text{ MHz}$$

The CGA's output is almost but not quite entirely NTSC-conforming.  A real NTSC signal provides two interlaced fields of 262.5 scanlines, whereas the CGA outputs 262 progressive scanlines at approximately 60fps. This 565 vs 564 scanline difference is minor enough for television sets to ignore.

The CGA produces a display field of \\(912 \times 262\\) or \\(238,944\\) hdots. 

The true refresh rate of the CGA can be calculated as:

$$f_{refresh} = \frac{14{,}318{,}181}{238{,}944} = 59.92 \text{ Hz}$$ 

This is 99.87% of 60Hz, meaning that if you sync your emulator to 60Hz you will run about 0.1% too fast.  

## Video Memory

The 16KB of DRAM the CGA card has is not expandable. It also **single-ported**, meaning that only either the CPU or the CGA can access the video memory at any given time. This is a bit of a problem, as the CGA needs to be reading video memory constantly as it rasterizes the screen.

The CGA has some circuitry for attempting to marshall the CPU's access to video memory, but perhaps due to limitations in board space, this circuitry was only implemented for the card's slower low-resolution modes. In high-resolution text mode, attempts to access video memory by the CPU while the CGA is rasterizing the active display area will result in what is called "snow" - random glitches where the CGA reads the wrong data while attempting to read character glyphs or attribute bytes. IBM worked around this in BIOS routines that scrolled the screen - such as when you execute the `DIR` command in DOS by rapidly disabling and re-enabling the display, causing noticable flicker.





