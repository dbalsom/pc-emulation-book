# Composite Video

The IBM CGA card supported [composite video](https://en.wikipedia.org/wiki/Composite_video) output via a female [RCA connector](https://en.wikipedia.org/wiki/RCA_connector).

Composite video is a standard by which *luminance*, *chrominance* and synchronization signals such as VSYNC and HSYNC are modulated together on a single wire. Obviously this requires some tradeoffs in image quality. Later video standards, such as [S-Video](https://en.wikipedia.org/wiki/S-Video) and [Component video](https://en.wikipedia.org/wiki/Component_video) would improve picture quality by separating these signals onto individual conductors.

An in-depth discussion of the NTSC video display standard is out of scope for this book. Instead, we will discuss the particular aspects of the CGA card's composite video output that are relevant for emulation.

> [!WARNING]
> The various color diagrams used in this chapter are for intended for conceptual visualization only. They are not mathematically rigorous.

## The Color Burst

The NTSC broadcast television standard was originally black and white. When color was added to the broadcast signal, it needed to be added in a way that was backwards compatible with black and white television sets. One way this was accomplished was by adding a signal called the *color burst* that only color television sets would understand.

The *color burst* is a 3.57954MHz reference clock signal emitted during the *back porch* of a scanline. It is a sine wave about 2.5 microseconds in duration that provides a *phase reference* for decoding color for that particular scanline. You can see the color burst from an IBM CGA card captured on an oscilloscope below.

<div style="text-align: center; margin: 1.5em 0;">
  <img src="../images/scope_captures/ntsc_color_burst_01.png"
       alt="A screenshot of an oscilloscope readout showing the CGA composite output signal at HSYNC, with a color burst immediately following."
       style="max-width: 100%; max-height: 480px; height: auto;"
       onclick="openModal(this)">
  <p style="font-style: italic; margin-top: 0.5em; opacity: 0.8;"><em>The CGA color burst</em></p>
</div>

Without a color burst signal, the composite video signal for that scanline will be interpreted as luminance only, producing a grayscale picture.

## Additive Chrominance

To allow for color to be *added* to an existing luminance-only signal, we must take the color signal and subtract luminance from it, producing a signal called *chrominance*. This signal is generally represented by two axes. One possible way to represent a chrominance signal is with a *blue* axis (with yellow as its complement) and a *red* axis (with green as its complement). If we call the luminance component Y, these two axes become **B-Y** and **R-Y**, since we have subtracted the luminance component from each.

Two proportional terms can be established:

$$
U \propto B' - Y'
$$

$$
V \propto R' - Y'
$$

This is the basic derivation of the [Y'UV color space](https://en.wikipedia.org/wiki/Y%E2%80%B2UV).


## Phase and the Unit Circle

Color is encoded in a composite signal by comparing the phase offset of the color signal contained within the 3.57954MHz color carrier with the reference phase of the color burst. 

We can map YUV colors to the [unit circle](https://en.wikipedia.org/wiki/Unit_circle), assigning an angle to each color. This produces the YUV color wheel. The color burst represents a reference at 180 on this wheel, mapping to the color yellow. Sometimes you will see the color burst referred to as the *yellow burst* as a consequence.

<div style="text-align: center; margin: 1.5em 0;">
  <img src="../images/diagrams/color_wheel_01.svg"
       alt="A YUV color wheel, with blue on the right, red at the top at 90 degrees, yellow on the left at 180 degrees, and green at the bottom at 270 degrees (approximate)."
       style="max-width: 100%; max-height: 480px; height: auto;">
  <p style="font-style: italic; margin-top: 0.5em; opacity: 0.8;"><em>The YUV color wheel (approximate)</em></p>
</div>

## YIQ Color Space

Actual NTSC video broadcasts do not directly encode color in the YUV color space. Instead, a rotated color space is used, primarily centered on an axis called **I** along which most human skin-tones fall. Engineers designing the NTSC video standard could then dedicate more video bandwidth to this axis. **I** is referred to as the *in-phase component*, and **Q**, being 90° from **I** is called the *quadrature component*. This is the [YIQ color space](https://en.wikipedia.org/wiki/YIQ).

<div style="text-align: center; margin: 1.5em 0;">
  <img src="../images/diagrams/color_wheel_yiq_01.svg"
       alt="A YUV color wheel, with blue on the right, red at the top at 90 degrees, yellow on the left at 180 degrees, and green at the bottom at 270 degrees (approximate). The I and Q axes of the YIQ color space are overlaid in orange and purple, respectively.."
       style="max-width: 100%; max-height: 480px; height: auto;">
  <p style="font-style: italic; margin-top: 0.5em; opacity: 0.8;"><em>The YUV color wheel with IQ axes (approximate)</em></p>
</div>

## The CGA Composite Color Clocks

The CGA produces six square waves representing six unique *color clocks*. These represent a 3-bit or 8 color "palette", with black and white not requiring a dedicated clock as they represent a constant low and high logic level, respectively.

A octal 74LS151 multiplexer selects one of the color clocks depending on the internally generated **B**, **G** and **R** color signals. Note that intensity is not used for color clock selection, but contributes to luma instead.

| B | G | R | Clock |
|---|---|---|-------|
| 0 | 0 | 0 | Black |
| 1 | 0 | 0 | Blue |
| 0 | 1 | 0 | Green |
| 1 | 1 | 0 | Cyan |
| 0 | 0 | 1 | Red |
| 1 | 0 | 1 | Magenta |
| 0 | 1 | 1 | Yellow |
| 1 | 1 | 1 | White |

Each clock is shifted out of phase in respect to the color burst, which is equivalent to the yellow color clock.

<div style="text-align: center; margin: 1.5em 0;">
  <img src="../images/diagrams/cga_color_clocks_01.svg"
       alt="A diagram of the six unique color clocks in the IBM CGA's composite generation circuitry, and their phase relationships mapped to a YUV color wheel."
       style="max-width: 100%; max-height: 800px; height: auto;"
       onclick="openModal(this)">
  <p style="font-style: italic; margin-top: 0.5em; opacity: 0.8;"><em>The IBM CGA composite color clocks</em></p>
</div>

This mapping enables a ballpark reproduction of the CGA's standard graphics palettes on a composite monitor, with the exception that yellow makes a reapparance where the IBM 5153 monitor would have produced brown. The CGA's infamous magenta also becomes more of a purple shade.

<div style="text-align: center; margin: 1.5em 0;">
  <img src="../images/photos/alleycat_composite_01.jpg"
       alt="A photograph of the PC Booter game AlleyCat running in composite on a Commodore 1084D monitor"
       style="max-width: 50%; height: auto;"
       onclick="openModal(this)">
  <p style="font-style: italic; margin-top: 0.5em; opacity: 0.8;"><em>"AlleyCat" by Bill Williams in CGA Composite</em></p>
</div>

In medium-resolution graphics mode, two pixels fit into a single NTSC *color cycle*. Therefore where high frequency contrast changes occur, color fringing can be observed. These fringes are generally called *color artifacts*. 

<div style="text-align: center; margin: 1.5em 0;">
  <img src="../images/photos/alleycat_composite_artifacts_01.jpg"
       alt="A close-up zoom into a photograph of the PC Booter game AlleyCat running in composite on a Commodore 1084D monitor, showing colored fringes around the trash can sprite"
       style="max-width: 50%; height: auto;"
       onclick="openModal(this)">
  <p style="font-style: italic; margin-top: 0.5em; opacity: 0.8;"><em>Composite color artifacting</em></p>
</div>

Although color artifacting was usually undesireable when displaying graphics designed for RGBI monitors, clever artists could intentionally use pairs of pixels that produce specific *artifact colors*. If done carefully, the result can be acceptable on both RGBI and composite displays. Notice in this screenshot from [*The Ancient Art of War at Sea*](https://www.mobygames.com/game/188/the-ancient-art-of-war-at-sea/) how the stripes in the RGBI graphics produce solid colors on a composite display, notably turning a magenta beard into an actual brown.

<div style="text-align: center; margin: 1.5em 0;">
  <img src="../images/screenshots/cga_composite_aowas_01.png"
       alt="A side-by-side comparison of a screenshot from The Ancient Art of War At Sea showing a screen that looks acceptable in both RGBI and composite, taking advantage of artifact color for an improved palette"
       style="max-width: 80%; max-height: 480px;"
       onclick="openModal(this)">
  <p style="font-style: italic; margin-top: 0.5em; opacity: 0.8;"><em>Intentional color artifacting in "The Ancient Art of War at Sea"</em></p>
</div>

Individual pixels will no longer render as white, instead transmuted into a specific color depending on their phase relationship. Notice here how the single-pixel stars in the background of fourth and six panels become yellow-orange and blue. This particular type of color artifacting will be very familiar to anyone familiar with the Apple II.

## Composite and High-Resolution Graphics Mode

Like the Apple II, it is possible to produce a color composite video signal using the CGA's high-resolution monochrome video mode, relying solely on the effect of color artifacting.

With double the horizontal resolution, four pixels in high-resolution graphics mode fit into a single NTSC color cycle, producing an effective 4-bit or 16-color "palette."





## 80-Column Text Mode Caveats

In 80-column text mode, the IBM CGA card disables the color burst, at least when using the standard CRTC register values. The cause of this is U64, a 74LS164 8-bit shift register that generates the trigger for the color burst generation circuitry. It requires 7 **lclocks** to fire. In both 80-column and 40-column text mode, the CRTC's HSYNC width register **R3** is set to 10. Given the faster character clock in 80-column text mode, this equates to only **5 lclocks** and thus the color burst never triggers.

This is actually a good thing for most users, as it turns 80-column text mode from what would be a smeary, technicolor mess into a fairly usable grayscale signal. Clones of the IBM CGA did not always behave in a similar manner, so switching into 40-column text mode was a useful workaround for a readable DOS prompt.
