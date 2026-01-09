# Display Concepts

The main displays for the IBM PC were [cathode-ray tube (CRT)](https://en.wikipedia.org/wiki/Cathode_ray_tube) monitors and television sets.

A CRT works by directing a beam of electrons at a screen coated with phosphor within a vacuum-sealed glass tube. The phosphor glows when struck by the electron beam, emitting light visible from the front side of the glass. The beam can be moved around (or **deflected**) by magnets, since electrons have a charge. Some CRTs could move the beam around in arbitrary ways to draw lines - these were called [vector displays](https://en.wikipedia.org/wiki/Vector_monitor). You may be familiar with them used in early arcade games like [Asteroids](https://en.wikipedia.org/wiki/Asteroids_(video_game)) or the [Vectrex](https://en.wikipedia.org/wiki/Vectrex) video game console.

Most, if not all home computer displays were [raster displays](https://en.wikipedia.org/wiki/Raster_graphics). In a raster display, the electron beam is moved across the screen in a succession of lines called **scanlines**, usually starting in the upper-left corner. When the electron beam reached the right side of the screen, it was shut off briefly and the magnets set to deflect the beam back to the left side, slightly lower down on the screen, ready to draw the next scanline. In this manner the entire screen can be drawn, until the bottom-right corner of the screen is reached. After that, the beam must be turned off again and the deflection set to return the beam back to the upper left corner.  This process repeats at frequency anywhere from 50Hz to 70Hz or more, depending on the adapter and monitor. 

The phosphors on the screen only stay fully lit during the period at which the electron beam is directly illuminating them, after which they start to fade.  Different phosphors faded more slowly than others - the phosphors used in older monochrome monitors faded slowly enough that scrolling text could leave "smears" on the screen.  Fast responding phosphors were more preferable for this reason. To a high speed camera, a CRT will look like a bright line trailed by a fading image, however quirks of human perception means that we perceive a raster-scanned display as having a fixed, steady image. That said, many people experience eye strain using monitors with lower refresh rates. 

## Terminology

 - **pixel:** - (Picture Element) This is usually the smallest addressable element of a raster display, determined by the capabilities of the display and display adapter.
 - **hdot:** - (Horizontal dot) This is essentially the time-based unit equivalent to a pixel, but a pixel need not be drawn during every hdot.
 - **dot clock:** - The frequency at which the video card produces pixels. By slowing down the dot clock, the effective horizontal resolution of a card can be decreased, making each pixel wider. The display timings of the card must be reconfigured to account for this.
 - **horizontal blanking period:** - The period in which the electron beam is turned off at the left and right edges of the screen or beyond.
 - **vertical blanking period:** - The period in which the display is turned off at the top and bottom edges of the screen or beyond.
 - **horizontal retrace:** - The period in which the electron beam is being moved from the right side of the screen to the left side. Occurs during the horizontal blanking period. Also called a **horizontal refresh**.
 - **vertical retrace:** - The period in which the electron beam is being moved from the bottom-right of the screen to the top-left side. Occurs duing the vertical blanking period. Also called a **vertical refresh**.
 - **horizontal front porch:** - The period of the horizontal blanking period immediately before the horizontal retrace period.
 - **horizontal back porch:** - The period of the horizontal blanking period immediately after the horizontal retrace period.
 - **vertical front porch:** - The period of the vertical blanking period immediately before the vertical retrace period.
 - **vertical back porch:** - The period of the verttical blanking period immediately after the vertical retrace period.
 - **hsync:** - A signal the display adapter may send to the monitor to initiate the horizontal retrace period.
 - **vsync:** - A signal the display adapter may send to the monitor to initiate the vertical retrace period.
 - **horizontal refresh rate:** - The frequency at which the monitor displays an entire scanline, ending in an hsync. Expressed in KHz.
 - **vertical refresh rate:** - The frequency at which the monitor displays an entire frame, ending in a vsync. Expressed in Hz.
 - **overscan:**
    - On analog television sets, the [overscan](https://en.wikipedia.org/wiki/Overscan) is part of the video signal that may be hidden by the display's bezels. 
    - On digital computer monitors, 'overscan' typically refers to the part of the video signal which lies outside of the region where addressable pixels are displayed, which may lie partially within the borders of the monitor's bezels, and partially outside it. The overscan can often be set to a particular color, depending on the adapter.

