# The IBM Color Graphics Adapter (CGA)

The IBM CGA card was one of the first video adapters available for the IBM PC/XT, along with the IBM Monochrome Display Adapter and the Hercules video adapter.

The CGA could be connected to a regular North American television set via its composite output connector. A digital DE-9 connection eventually allowed it to be connected to the IBM 5153 Color Display, once that was finally released. IBM left owners of the CGA waiting a bit for a proper monitor - it was only released in 1983, two years after the CGA's debut.

The CGA has 16KB of DRAM dedicated to video memory, and a 4KB font ROM that holds bit patterns for drawing text glyphs.

In text mode, the CGA card was capable of outputting 16 colors. In graphics mode, it was limited to 3 palettes of 3 fixed colors each, with a selectable background color.  The CGA also had a high-resolution mode, with a single, selectable foreground color on black.

Like the MDA, the CGA is built around the [Motorola MC6845 CRTC](6845.md). See that section first for a basic understanding of how that chip is used to define display geometry.

## Display Timings

Unlike the MDA, the CGA does not have its own crystal. IBM designed the main system crystal of the PC itself around the NTSC display standard, with the apparent intent of simplifying the production of the CGA and other television-compatible peripherals.

The 5150 has a single main system crystal with a frequency of 14.31818MHz. This frequency is exactly four times the [NTSC](https://en.wikipedia.org/wiki/NTSC) color subcarrier frequency.

The crystal frequency can be expressed as a fraction:

$$f_{crystal} = \frac{315}{22} \text{ MHz} = 14.318181\overline{81} \text{ MHz}$$

The CGA's output is almost but not quite entirely NTSC-conforming.  A real NTSC signal provides two interlaced fields of 262.5 scanlines, whereas the CGA outputs 262 progressive scanlines at approximately 60fps. This 565 vs 564 scanline difference is minor enough for television sets to ignore.

The CGA produces a display field of \\(912 \times 262\\) or \\(238,944\\) hdots. 

The exact vertical refresh rate of the CGA can be calculated as:

$$f_{refresh} = \frac{14{,}318{,}181}{238{,}944} = 59.92 \text{ Hz}$$ 

The horizontal retrace rate can be calculated as:

$$f_{hsync} = \frac{14{,}318{,}181}{912} = 15.70 \text{ kHz}$$

This is a significant number in that you will often hear monitors capable of displaying 200-line resolution modes produced by the CGA and EGA video cards described as [15KHz displays](https://www.dosdays.co.uk/topics/15khz_monitors.php).

## Dot Clock

The 14.31818Mhz clock of the CGA can be used directly as the dot clock, which is the case in the card's high resolution text mode. Alternatively, it can be divided by two to produce a 7.159Mhz dot clock, which is done in the card's lower resolution modes. When using the native clock or **hclock** the card typically outputs 640 pixels per scanline. When using the halved clock or **lclock**, the card typically outputs 320 pixels per scanline, as the effective width of each pixel is doubled since the raster beam continues to scan out the screen at the same rate. 

With either clock, the number of vertical scanlines remains the same, but the horizontal timings programmed into the CRTC must be adjusted to account for the lower clock when the clock divisor is in use.

## Video Memory

The 16KB of DRAM on the CGA is not expandable. It also **single-ported**, meaning that only either the CPU or the CGA can access the video memory at any given time. This is a bit of a problem as the CGA needs to be reading video memory constantly as it rasterizes the screen.

The CGA has some circuitry for attempting to marshall the CPU's access to video memory, but perhaps due to limitations in board space, this circuitry was only implemented for the card's low-resolution modes where the **lclock** is used. In high-resolution text mode, attempts to access video memory by the CPU while the CGA is rasterizing the active display area will result in what is called **snow** - random glitches where the CGA reads the wrong data while attempting to read character glyphs or attribute bytes. IBM worked around this in BIOS routines that scrolled the screen - such as when you execute the `DIR` command in DOS by rapidly disabling and re-enabling the display, causing noticable flicker.

## Operational Modes

The CGA has two main modes of operation, text mode and graphics mode. 

### Text Mode

In text mode, video memory is organized conceptually as a grid of **character cells**, the dimensions of which are directly configured on the CRTC. Typically, this will be a rectangular grid of 80x25 characters. Each logical cell is comprised of a pair of bytes in video memory, the first byte being a **character code** and the second byte being a **character attribute**. The character code indicates what character glyph to display. For a list of all character codes and their corresponding glyphs, see the [ASCII table](../appendices/ascii-table.md) appendix.

The character code, combined with the vertical line counter of the CRTC, is used to resolve a byte contained in the CGA's **font ROM** representing 8 pixels (or **span**) of a character glyph. The character attribute byte then describes the colors to use for the foreground and background as the glyph span is drawn. 

Since each character cell requires two bytes, it takes 4KB of memory to display an 80x25 text mode screen. This means up to four text-mode screens can fit in the CGA's 16KB of memory, and a program can switch between each screen by adjusting the CRTC's start address registers. Multiple screens present in video memory are often called **video pages**, and switching between them may be referred to as **page-switching** or **page-flipping** when used for fast animation. Alternatively, a single large screen of up to 80x100 could be stored in memory and the visible 80x25 region panned down through it by adjusting the start address registers one row at a time.

## Primary Emulation Resources

 - (seasip.info) [Colour Graphics Adapter: Notes](https://www.seasip.info/VintagePC/cga.html)




