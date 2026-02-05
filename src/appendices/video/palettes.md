# Video Palettes

## CGA Text Mode

In color text modes, the CGA card can emit a total of 16 different colors - a combination of the four video signals: red, green, blue, and intensity - a signal that boosts the brightness of the previous three color signals. Note that the intensity bit also boosts the apparent brightness of pure black, creating a dim gray.

> **NOTE:**
> The standard CGA brown color is not actually a color emitted by the CGA card; the conversion of 'dark yellow' to brown occurs via special circuitry within the IBM 5153 Color Display and most CGA-compatible monitors.

### Full RGBI Palette

<table>
<thead>
<tr>
<th>R</th>
<th>G</th>
<th>B</th>
<th>I</th>
<th>Color</th>
<th>Hex</th>
</tr>
</thead>
<tbody>
<tr><td>0</td><td>0</td><td>0</td><td>0</td><td style="background-color: #000000; width: 50px;">&nbsp;</td><td>000000</td></tr>
<tr><td>0</td><td>0</td><td>1</td><td>0</td><td style="background-color: #0000AA; width: 50px;">&nbsp;</td><td>0000AA</td></tr>
<tr><td>0</td><td>1</td><td>0</td><td>0</td><td style="background-color: #00AA00; width: 50px;">&nbsp;</td><td>00AA00</td></tr>
<tr><td>0</td><td>1</td><td>1</td><td>0</td><td style="background-color: #00AAAA; width: 50px;">&nbsp;</td><td>00AAAA</td></tr>
<tr><td>1</td><td>0</td><td>0</td><td>0</td><td style="background-color: #AA0000; width: 50px;">&nbsp;</td><td>AA0000</td></tr>
<tr><td>1</td><td>0</td><td>1</td><td>0</td><td style="background-color: #AA00AA; width: 50px;">&nbsp;</td><td>AA00AA</td></tr>
<tr><td>1</td><td>1</td><td>0</td><td>0</td><td style="background-color: #AA5500; width: 50px;">&nbsp;</td><td>AA5500</td></tr>
<tr><td>1</td><td>1</td><td>1</td><td>0</td><td style="background-color: #AAAAAA; width: 50px;">&nbsp;</td><td>AAAAAA</td></tr>
<tr><td>0</td><td>0</td><td>0</td><td>1</td><td style="background-color: #555555; width: 50px;">&nbsp;</td><td>555555</td></tr>
<tr><td>0</td><td>0</td><td>1</td><td>1</td><td style="background-color: #5555FF; width: 50px;">&nbsp;</td><td>5555FF</td></tr>
<tr><td>0</td><td>1</td><td>0</td><td>1</td><td style="background-color: #55FF55; width: 50px;">&nbsp;</td><td>55FF55</td></tr>
<tr><td>0</td><td>1</td><td>1</td><td>1</td><td style="background-color: #55FFFF; width: 50px;">&nbsp;</td><td>55FFFF</td></tr>
<tr><td>1</td><td>0</td><td>0</td><td>1</td><td style="background-color: #FF5555; width: 50px;">&nbsp;</td><td>FF5555</td></tr>
<tr><td>1</td><td>0</td><td>1</td><td>1</td><td style="background-color: #FF55FF; width: 50px;">&nbsp;</td><td>FF55FF</td></tr>
<tr><td>1</td><td>1</td><td>0</td><td>1</td><td style="background-color: #FFFF55; width: 50px;">&nbsp;</td><td>FFFF55</td></tr>
<tr><td>1</td><td>1</td><td>1</td><td>1</td><td style="background-color: #FFFFFF; width: 50px;">&nbsp;</td><td>FFFFFF</td></tr>
</tbody>
</table>

### The "IBM 5153" Palette

The aforementioned palette represents "ideal" colors - theoretically perfect color outputs. Modern displays have no problem rendering such colors, but original CGA monitors such as the IBM 5153 Color Display had their own eccentricities. 

Taking into account the electrical characteristics of the 5153, a more [visually authentic CGA palette](https://int10h.org/blog/2022/06/ibm-5153-color-true-cga-palette/) can be derived:

<table>
<thead>
<tr>
<th>R</th>
<th>G</th>
<th>B</th>
<th>I</th>
<th>Color</th>
<th>Hex</th>
</tr>
</thead>
<tbody>
<tr><td>0</td><td>0</td><td>0</td><td>0</td><td style="background-color: #000000; width: 50px;">&nbsp;</td><td>000000</td></tr>
<tr><td>0</td><td>0</td><td>1</td><td>0</td><td style="background-color: #0000C4; width: 50px;">&nbsp;</td><td>0000C4</td></tr>
<tr><td>0</td><td>1</td><td>0</td><td>0</td><td style="background-color: #00C400; width: 50px;">&nbsp;</td><td>00C400</td></tr>
<tr><td>0</td><td>1</td><td>1</td><td>0</td><td style="background-color: #00C4C4; width: 50px;">&nbsp;</td><td>00C4C4</td></tr>
<tr><td>1</td><td>0</td><td>0</td><td>0</td><td style="background-color: #C40000; width: 50px;">&nbsp;</td><td>C40000</td></tr>
<tr><td>1</td><td>0</td><td>1</td><td>0</td><td style="background-color: #C400C4; width: 50px;">&nbsp;</td><td>C400C4</td></tr>
<tr><td>1</td><td>1</td><td>0</td><td>0</td><td style="background-color: #C47E00; width: 50px;">&nbsp;</td><td>C47E00</td></tr>
<tr><td>1</td><td>1</td><td>1</td><td>0</td><td style="background-color: #C4C4C4; width: 50px;">&nbsp;</td><td>C4C4C4</td></tr>
<tr><td>0</td><td>0</td><td>0</td><td>1</td><td style="background-color: #4E4E4E; width: 50px;">&nbsp;</td><td>4E4E4E</td></tr>
<tr><td>0</td><td>0</td><td>1</td><td>1</td><td style="background-color: #4E4EDC; width: 50px;">&nbsp;</td><td>4E4EDC</td></tr>
<tr><td>0</td><td>1</td><td>0</td><td>1</td><td style="background-color: #4EDC4E; width: 50px;">&nbsp;</td><td>4EDC4E</td></tr>
<tr><td>0</td><td>1</td><td>1</td><td>1</td><td style="background-color: #4EF3F3; width: 50px;">&nbsp;</td><td>4EF3F3</td></tr>
<tr><td>1</td><td>0</td><td>0</td><td>1</td><td style="background-color: #DC4E4E; width: 50px;">&nbsp;</td><td>DC4E4E</td></tr>
<tr><td>1</td><td>0</td><td>1</td><td>1</td><td style="background-color: #F34EF3; width: 50px;">&nbsp;</td><td>F34EF3</td></tr>
<tr><td>1</td><td>1</td><td>0</td><td>1</td><td style="background-color: #F3F34E; width: 50px;">&nbsp;</td><td>F3F34E</td></tr>
<tr><td>1</td><td>1</td><td>1</td><td>1</td><td style="background-color: #FFFFFF; width: 50px;">&nbsp;</td><td>FFFFFF</td></tr>
</tbody>
</table>

## CGA Graphics Modes

Although much is said - derisively - about the CGA's ugly 'palettes', the IBM CGA card does not actually have what we would typically consider palettes at all. 

In graphics mode, pairs of bits from video memory drive the red and green video output lines **directly**, with no color look-ups performed. The effect of having multiple palettes is produced by miscellaneous logic that determines if and when the blue video output is additionally enabled or not.

When both bits from video memory are 0, the background/overscan color configured in the CGA Color Control register is substituted. Black is not a requirement for any of the CGA's palettes.

The intensity bit, specified in the CGA Color Control register, provides two variations of brightness per palette.

### Default Palette (Blue Disabled)

<div style="display: flex; flex-wrap: wrap; gap: 20px; justify-content: center;">

<div>
<table>
<thead>
<tr>
<th>R</th>
<th>G</th>
<th>B</th>
<th>I</th>
<th>Color</th>
<th>Hex</th>
</tr>
</thead>
<tbody>
<tr><td>0</td><td>0</td><td>0</td><td>0</td><td class="cga-bg-swatch" style="width: 50px;">&nbsp;</td><td>Overscan</td></tr>
<tr><td>0</td><td>1</td><td>0</td><td>0</td><td style="background-color: #00AA00; width: 50px;">&nbsp;</td><td>00AA00</td></tr>
<tr><td>1</td><td>0</td><td>0</td><td>0</td><td style="background-color: #AA0000; width: 50px;">&nbsp;</td><td>AA0000</td></tr>
<tr><td>1</td><td>1</td><td>0</td><td>0</td><td style="background-color: #AA5500; width: 50px;">&nbsp;</td><td>AA5500</td></tr>
</tbody>
</table>
</div>

<div>
<table>
<thead>
<tr>
<th>R</th>
<th>G</th>
<th>B</th>
<th>I</th>
<th>Color</th>
<th>Hex</th>
</tr>
</thead>
<tbody>
<tr><td>0</td><td>0</td><td>0</td><td>1</td><td class="cga-bg-swatch" style="width: 50px;">&nbsp;</td><td>Overscan</td></tr>
<tr><td>0</td><td>1</td><td>0</td><td>1</td><td style="background-color: #55FF55; width: 50px;">&nbsp;</td><td>55FF55</td></tr>
<tr><td>1</td><td>0</td><td>0</td><td>1</td><td style="background-color: #FF5555; width: 50px;">&nbsp;</td><td>FF5555</td></tr>
<tr><td>1</td><td>1</td><td>0</td><td>1</td><td style="background-color: #FFFF55; width: 50px;">&nbsp;</td><td>FFFF55</td></tr>
</tbody>
</table>
</div>


</div>

### Secondary Palette (Blue Enabled)

<div style="display: flex; flex-wrap: wrap; gap: 20px; justify-content: center;">

<div>
<table>
<thead>
<tr>
<th>R</th>
<th>G</th>
<th>B</th>
<th>I</th>
<th>Color</th>
<th>Hex</th>
</tr>
</thead>
<tbody>
<tr><td>0</td><td>0</td><td>0</td><td>0</td><td class="cga-bg-swatch" style="width: 50px;">&nbsp;</td><td>Overscan</td></tr>
<tr><td>0</td><td>1</td><td>1</td><td>0</td><td style="background-color: #00AAAA; width: 50px;">&nbsp;</td><td>00AAAA</td></tr>
<tr><td>1</td><td>0</td><td>1</td><td>0</td><td style="background-color: #AA00AA; width: 50px;">&nbsp;</td><td>AA00AA</td></tr>
<tr><td>1</td><td>1</td><td>1</td><td>0</td><td style="background-color: #AAAAAA; width: 50px;">&nbsp;</td><td>AAAAAA</td></tr>
</tbody>
</table>
</div>

<div>
<table>
<thead>
<tr>
<th>R</th>
<th>G</th>
<th>B</th>
<th>I</th>
<th>Color</th>
<th>Hex</th>
</tr>
</thead>
<tbody>
<tr><td>0</td><td>0</td><td>0</td><td>1</td><td class="cga-bg-swatch" style="width: 50px;">&nbsp;</td><td>Overscan</td></tr>
<tr><td>0</td><td>1</td><td>1</td><td>1</td><td style="background-color: #55FFFF; width: 50px;">&nbsp;</td><td>55FFFF</td></tr>
<tr><td>1</td><td>0</td><td>1</td><td>1</td><td style="background-color: #FF55FF; width: 50px;">&nbsp;</td><td>FF55FF</td></tr>
<tr><td>1</td><td>1</td><td>1</td><td>1</td><td style="background-color: #FFFFFF; width: 50px;">&nbsp;</td><td>FFFFFF</td></tr>
</tbody>
</table>
</div>


</div>

### Alternate Palette (Blue Enabled Except When Red)

Sometimes described as a "hidden" palette, and often considered the most aesthetically pleasing, the cyan-red-white palette was only implemented to provide better contrast when displaying CGA graphics modes on a monochrome composite display, such as a black-and-white television set. It was not implemented for its aesthetics, and thus IBM probably didn't see fit to document it as a color option - after all, later revisions of the CGA could have always disabled the need for it by adjustments to the composite output circuitry. 

This palette is created by miscellaneous logic that enables the blue video output unless the color red is decoded.

<div style="display: flex; flex-wrap: wrap; gap: 20px; justify-content: center;">

<div>
<table>
<thead>
<tr>
<th>R</th>
<th>G</th>
<th>B</th>
<th>I</th>
<th>Color</th>
<th>Hex</th>
</tr>
</thead>
<tbody>
<tr><td>0</td><td>0</td><td>0</td><td>0</td><td class="cga-bg-swatch" style="width: 50px;">&nbsp;</td><td>Overscan</td></tr>
<tr><td>0</td><td>1</td><td>1</td><td>0</td><td style="background-color: #00AAAA; width: 50px;">&nbsp;</td><td>00AAAA</td></tr>
<tr><td>1</td><td>0</td><td>0</td><td>0</td><td style="background-color: #AA0000; width: 50px;">&nbsp;</td><td>AA0000</td></tr>
<tr><td>1</td><td>1</td><td>1</td><td>0</td><td style="background-color: #AAAAAA; width: 50px;">&nbsp;</td><td>AAAAAA</td></tr>
</tbody>
</table>
</div>

<div>
<table>
<thead>
<tr>
<th>R</th>
<th>G</th>
<th>B</th>
<th>I</th>
<th>Color</th>
<th>Hex</th>
</tr>
</thead>
<tbody>
<tr><td>0</td><td>0</td><td>0</td><td>1</td><td class="cga-bg-swatch" style="width: 50px;">&nbsp;</td><td>Overscan</td></tr>
<tr><td>0</td><td>1</td><td>1</td><td>1</td><td style="background-color: #55FFFF; width: 50px;">&nbsp;</td><td>55FFFF</td></tr>
<tr><td>1</td><td>0</td><td>0</td><td>1</td><td style="background-color: #FF5555; width: 50px;">&nbsp;</td><td>FF5555</td></tr>
<tr><td>1</td><td>1</td><td>1</td><td>1</td><td style="background-color: #FFFFFF; width: 50px;">&nbsp;</td><td>FFFFFF</td></tr>
</tbody>
</table>
</div>

</div>

### EGA 6-bit Palette (64 Colors)

The EGA can display any 16 of these 64 colors simultaneously when connected to an EGA monitor and operating in 350 line mode, although there are exceptions that enable use of 6bpp color in 200 line modes with the right hardware.

<table>
<thead>
<tr>
<th>Index</th><th>RI</th><th>GI</th><th>BI</th><th>R</th><th>G</th><th>B</th><th>Color</th><th>Hex</th>
<th>Index</th><th>RI</th><th>GI</th><th>BI</th><th>R</th><th>G</th><th>B</th><th>Color</th><th>Hex</th>
</tr>
</thead>
<tbody>
<tr><td>00</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td style="background-color: #000000; width: 50px;">&nbsp;</td><td>000000</td></td><td>20</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td style="background-color: #550000; width: 50px;">&nbsp;</td><td>550000</td></tr>
<tr><td>01</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td style="background-color: #0000AA; width: 50px;">&nbsp;</td><td>0000AA</td></td><td>21</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td style="background-color: #5500AA; width: 50px;">&nbsp;</td><td>5500AA</td></tr>
<tr><td>02</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td style="background-color: #00AA00; width: 50px;">&nbsp;</td><td>00AA00</td></td><td>22</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td style="background-color: #55AA00; width: 50px;">&nbsp;</td><td>55AA00</td></tr>
<tr><td>03</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td style="background-color: #00AAAA; width: 50px;">&nbsp;</td><td>00AAAA</td></td><td>23</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td style="background-color: #55AAAA; width: 50px;">&nbsp;</td><td>55AAAA</td></tr>
<tr><td>04</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td style="background-color: #AA0000; width: 50px;">&nbsp;</td><td>AA0000</td></td><td>24</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td style="background-color: #FF0000; width: 50px;">&nbsp;</td><td>FF0000</td></tr>
<tr><td>05</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td style="background-color: #AA00AA; width: 50px;">&nbsp;</td><td>AA00AA</td></td><td>25</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td style="background-color: #FF00AA; width: 50px;">&nbsp;</td><td>FF00AA</td></tr>
<tr><td>06</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td style="background-color: #AAAA00; width: 50px;">&nbsp;</td><td>AAAA00</td></td><td>26</td><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td style="background-color: #FFAA00; width: 50px;">&nbsp;</td><td>FFAA00</td></tr>
<tr><td>07</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td style="background-color: #AAAAAA; width: 50px;">&nbsp;</td><td>AAAAAA</td></td><td>27</td><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td style="background-color: #FFAAAA; width: 50px;">&nbsp;</td><td>FFAAAA</td></tr>
<tr><td>08</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td style="background-color: #000055; width: 50px;">&nbsp;</td><td>000055</td></td><td>28</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td style="background-color: #550055; width: 50px;">&nbsp;</td><td>550055</td></tr>
<tr><td>09</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td><td style="background-color: #0000FF; width: 50px;">&nbsp;</td><td>0000FF</td></td><td>29</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td><td style="background-color: #5500FF; width: 50px;">&nbsp;</td><td>5500FF</td></tr>
<tr><td>0A</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td style="background-color: #00AA55; width: 50px;">&nbsp;</td><td>00AA55</td></td><td>2A</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td style="background-color: #55AA55; width: 50px;">&nbsp;</td><td>55AA55</td></tr>
<tr><td>0B</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td style="background-color: #00AAFF; width: 50px;">&nbsp;</td><td>00AAFF</td></td><td>2B</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td style="background-color: #55AAFF; width: 50px;">&nbsp;</td><td>55AAFF</td></tr>
<tr><td>0C</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td style="background-color: #AA0055; width: 50px;">&nbsp;</td><td>AA0055</td></td><td>2C</td><td>1</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td style="background-color: #FF0055; width: 50px;">&nbsp;</td><td>FF0055</td></tr>
<tr><td>0D</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>1</td><td style="background-color: #AA00FF; width: 50px;">&nbsp;</td><td>AA00FF</td></td><td>2D</td><td>1</td><td>0</td><td>1</td><td>1</td><td>0</td><td>1</td><td style="background-color: #FF00FF; width: 50px;">&nbsp;</td><td>FF00FF</td></tr>
<tr><td>0E</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td style="background-color: #AAAA55; width: 50px;">&nbsp;</td><td>AAAA55</td></td><td>2E</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td style="background-color: #FFAA55; width: 50px;">&nbsp;</td><td>FFAA55</td></tr>
<tr><td>0F</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td style="background-color: #AAAAFF; width: 50px;">&nbsp;</td><td>AAAAFF</td></td><td>2F</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td style="background-color: #FFAAFF; width: 50px;">&nbsp;</td><td>FFAAFF</td></tr>
<tr><td>10</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td style="background-color: #005500; width: 50px;">&nbsp;</td><td>005500</td></td><td>30</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td style="background-color: #555500; width: 50px;">&nbsp;</td><td>555500</td></tr>
<tr><td>11</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td style="background-color: #0055AA; width: 50px;">&nbsp;</td><td>0055AA</td></td><td>31</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td style="background-color: #5555AA; width: 50px;">&nbsp;</td><td>5555AA</td></tr>
<tr><td>12</td><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td style="background-color: #00FF00; width: 50px;">&nbsp;</td><td>00FF00</td></td><td>32</td><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td style="background-color: #55FF00; width: 50px;">&nbsp;</td><td>55FF00</td></tr>
<tr><td>13</td><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td><td style="background-color: #00FFAA; width: 50px;">&nbsp;</td><td>00FFAA</td></td><td>33</td><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td><td style="background-color: #55FFAA; width: 50px;">&nbsp;</td><td>55FFAA</td></tr>
<tr><td>14</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td style="background-color: #AA5500; width: 50px;">&nbsp;</td><td>AA5500</td></td><td>34</td><td>1</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td style="background-color: #FF5500; width: 50px;">&nbsp;</td><td>FF5500</td></tr>
<tr><td>15</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td style="background-color: #AA55AA; width: 50px;">&nbsp;</td><td>AA55AA</td></td><td>35</td><td>1</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td style="background-color: #FF55AA; width: 50px;">&nbsp;</td><td>FF55AA</td></tr>
<tr><td>16</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>0</td><td style="background-color: #AAFF00; width: 50px;">&nbsp;</td><td>AAFF00</td></td><td>36</td><td>1</td><td>1</td><td>0</td><td>1</td><td>1</td><td>0</td><td style="background-color: #FFFF00; width: 50px;">&nbsp;</td><td>FFFF00</td></tr>
<tr><td>17</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td><td style="background-color: #AAFFAA; width: 50px;">&nbsp;</td><td>AAFFAA</td></td><td>37</td><td>1</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td><td style="background-color: #FFFFAA; width: 50px;">&nbsp;</td><td>FFFFAA</td></tr>
<tr><td>18</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td style="background-color: #005555; width: 50px;">&nbsp;</td><td>005555</td></td><td>38</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td style="background-color: #555555; width: 50px;">&nbsp;</td><td>555555</td></tr>
<tr><td>19</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td><td style="background-color: #0055FF; width: 50px;">&nbsp;</td><td>0055FF</td></td><td>39</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td><td style="background-color: #5555FF; width: 50px;">&nbsp;</td><td>5555FF</td></tr>
<tr><td>1A</td><td>0</td><td>1</td><td>1</td><td>0</td><td>1</td><td>0</td><td style="background-color: #00FF55; width: 50px;">&nbsp;</td><td>00FF55</td></td><td>3A</td><td>1</td><td>1</td><td>1</td><td>0</td><td>1</td><td>0</td><td style="background-color: #55FF55; width: 50px;">&nbsp;</td><td>55FF55</td></tr>
<tr><td>1B</td><td>0</td><td>1</td><td>1</td><td>0</td><td>1</td><td>1</td><td style="background-color: #00FFFF; width: 50px;">&nbsp;</td><td>00FFFF</td></td><td>3B</td><td>1</td><td>1</td><td>1</td><td>0</td><td>1</td><td>1</td><td style="background-color: #55FFFF; width: 50px;">&nbsp;</td><td>55FFFF</td></tr>
<tr><td>1C</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td style="background-color: #AA5555; width: 50px;">&nbsp;</td><td>AA5555</td></td><td>3C</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td style="background-color: #FF5555; width: 50px;">&nbsp;</td><td>FF5555</td></tr>
<tr><td>1D</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>1</td><td style="background-color: #AA55FF; width: 50px;">&nbsp;</td><td>AA55FF</td></td><td>3D</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td><td>1</td><td style="background-color: #FF55FF; width: 50px;">&nbsp;</td><td>FF55FF</td></tr>
<tr><td>1E</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td><td style="background-color: #AAFF55; width: 50px;">&nbsp;</td><td>AAFF55</td></td><td>3E</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td><td style="background-color: #FFFF55; width: 50px;">&nbsp;</td><td>FFFF55</td></tr>
<tr><td>1F</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td style="background-color: #AAFFFF; width: 50px;">&nbsp;</td><td>AAFFFF</td></td><td>3F</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td style="background-color: #FFFFFF; width: 50px;">&nbsp;</td><td>FFFFFF</td></tr>
</tbody>
</table>

## The Default VGA Palette

The VGA has a total palette of 256 out of 262,144 colors, making a full table a bit impractical. The default VGA palette is shown below.

The VGA still has the 16 Attribute Controller Palette registers, which are used in text mode and 4bpp modes, however they no longer store color information. Instead, they contain indexes into the 256 color registers of the DAC. This DAC lookup is always active. 

The first 16 colors of the default VGA palette correspond to the traditional 16 color RGBI palette, and so the Attribute Palette registers reference the same colors by virtue of being initialized with the values 0-F.  The Attribute Palette registers remain 6 bits, and so they can only reference a total of 64 DAC Color registers. Due to this, the VGA divides the 256 total Color registers into four separate banks, which can be selected independently. 

<table style='border-collapse: collapse;'>
<tr>
<td class='vga-palette-cell' style='background-color: #000000; color: white;'>000000</td><td class='vga-palette-cell' style='background-color: #0000AA; color: white;'>0000AA</td><td class='vga-palette-cell' style='background-color: #00AA00; color: white;'>00AA00</td><td class='vga-palette-cell' style='background-color: #00AAAA; color: white;'>00AAAA</td><td class='vga-palette-cell' style='background-color: #AA0000; color: white;'>AA0000</td><td class='vga-palette-cell' style='background-color: #AA00AA; color: white;'>AA00AA</td><td class='vga-palette-cell' style='background-color: #AA5500; color: white;'>AA5500</td><td class='vga-palette-cell' style='background-color: #AAAAAA; color: black;'>AAAAAA</td><td class='vga-palette-cell' style='background-color: #555555; color: white;'>555555</td><td class='vga-palette-cell' style='background-color: #5555FF; color: white;'>5555FF</td><td class='vga-palette-cell' style='background-color: #55FF55; color: black;'>55FF55</td><td class='vga-palette-cell' style='background-color: #55FFFF; color: black;'>55FFFF</td><td class='vga-palette-cell' style='background-color: #FF5555; color: black;'>FF5555</td><td class='vga-palette-cell' style='background-color: #FF55FF; color: black;'>FF55FF</td><td class='vga-palette-cell' style='background-color: #FFFF55; color: black;'>FFFF55</td><td class='vga-palette-cell' style='background-color: #FFFFFF; color: black;'>FFFFFF</td></tr>
<tr>
<td class='vga-palette-cell' style='background-color: #000000; color: white;'>000000</td><td class='vga-palette-cell' style='background-color: #141414; color: white;'>141414</td><td class='vga-palette-cell' style='background-color: #202020; color: white;'>202020</td><td class='vga-palette-cell' style='background-color: #2C2C2C; color: white;'>2C2C2C</td><td class='vga-palette-cell' style='background-color: #383838; color: white;'>383838</td><td class='vga-palette-cell' style='background-color: #454545; color: white;'>454545</td><td class='vga-palette-cell' style='background-color: #515151; color: white;'>515151</td><td class='vga-palette-cell' style='background-color: #616161; color: white;'>616161</td><td class='vga-palette-cell' style='background-color: #717171; color: white;'>717171</td><td class='vga-palette-cell' style='background-color: #828282; color: black;'>828282</td><td class='vga-palette-cell' style='background-color: #929292; color: black;'>929292</td><td class='vga-palette-cell' style='background-color: #A2A2A2; color: black;'>A2A2A2</td><td class='vga-palette-cell' style='background-color: #B6B6B6; color: black;'>B6B6B6</td><td class='vga-palette-cell' style='background-color: #CBCBCB; color: black;'>CBCBCB</td><td class='vga-palette-cell' style='background-color: #E3E3E3; color: black;'>E3E3E3</td><td class='vga-palette-cell' style='background-color: #FFFFFF; color: black;'>FFFFFF</td></tr>
<tr>
<td class='vga-palette-cell' style='background-color: #0000FF; color: white;'>0000FF</td><td class='vga-palette-cell' style='background-color: #4100FF; color: white;'>4100FF</td><td class='vga-palette-cell' style='background-color: #7D00FF; color: white;'>7D00FF</td><td class='vga-palette-cell' style='background-color: #BE00FF; color: white;'>BE00FF</td><td class='vga-palette-cell' style='background-color: #FF00FF; color: white;'>FF00FF</td><td class='vga-palette-cell' style='background-color: #FF00BE; color: white;'>FF00BE</td><td class='vga-palette-cell' style='background-color: #FF007D; color: white;'>FF007D</td><td class='vga-palette-cell' style='background-color: #FF0041; color: white;'>FF0041</td><td class='vga-palette-cell' style='background-color: #FF0000; color: white;'>FF0000</td><td class='vga-palette-cell' style='background-color: #FF4100; color: white;'>FF4100</td><td class='vga-palette-cell' style='background-color: #FF7D00; color: black;'>FF7D00</td><td class='vga-palette-cell' style='background-color: #FFBE00; color: black;'>FFBE00</td><td class='vga-palette-cell' style='background-color: #FFFF00; color: black;'>FFFF00</td><td class='vga-palette-cell' style='background-color: #BEFF00; color: black;'>BEFF00</td><td class='vga-palette-cell' style='background-color: #7DFF00; color: black;'>7DFF00</td><td class='vga-palette-cell' style='background-color: #41FF00; color: black;'>41FF00</td></tr>
<tr>
<td class='vga-palette-cell' style='background-color: #00FF00; color: black;'>00FF00</td><td class='vga-palette-cell' style='background-color: #00FF41; color: black;'>00FF41</td><td class='vga-palette-cell' style='background-color: #00FF7D; color: black;'>00FF7D</td><td class='vga-palette-cell' style='background-color: #00FFBE; color: black;'>00FFBE</td><td class='vga-palette-cell' style='background-color: #00FFFF; color: black;'>00FFFF</td><td class='vga-palette-cell' style='background-color: #00BEFF; color: black;'>00BEFF</td><td class='vga-palette-cell' style='background-color: #007DFF; color: white;'>007DFF</td><td class='vga-palette-cell' style='background-color: #0041FF; color: white;'>0041FF</td><td class='vga-palette-cell' style='background-color: #7D7DFF; color: black;'>7D7DFF</td><td class='vga-palette-cell' style='background-color: #9E7DFF; color: black;'>9E7DFF</td><td class='vga-palette-cell' style='background-color: #BE7DFF; color: black;'>BE7DFF</td><td class='vga-palette-cell' style='background-color: #DF7DFF; color: black;'>DF7DFF</td><td class='vga-palette-cell' style='background-color: #FF7DFF; color: black;'>FF7DFF</td><td class='vga-palette-cell' style='background-color: #FF7DDF; color: black;'>FF7DDF</td><td class='vga-palette-cell' style='background-color: #FF7DBE; color: black;'>FF7DBE</td><td class='vga-palette-cell' style='background-color: #FF7D9E; color: black;'>FF7D9E</td></tr>
<tr>
<td class='vga-palette-cell' style='background-color: #FF7D7D; color: black;'>FF7D7D</td><td class='vga-palette-cell' style='background-color: #FF9E7D; color: black;'>FF9E7D</td><td class='vga-palette-cell' style='background-color: #FFBE7D; color: black;'>FFBE7D</td><td class='vga-palette-cell' style='background-color: #FFDF7D; color: black;'>FFDF7D</td><td class='vga-palette-cell' style='background-color: #FFFF7D; color: black;'>FFFF7D</td><td class='vga-palette-cell' style='background-color: #DFFF7D; color: black;'>DFFF7D</td><td class='vga-palette-cell' style='background-color: #BEFF7D; color: black;'>BEFF7D</td><td class='vga-palette-cell' style='background-color: #9EFF7D; color: black;'>9EFF7D</td><td class='vga-palette-cell' style='background-color: #7DFF7D; color: black;'>7DFF7D</td><td class='vga-palette-cell' style='background-color: #7DFF9E; color: black;'>7DFF9E</td><td class='vga-palette-cell' style='background-color: #7DFFBE; color: black;'>7DFFBE</td><td class='vga-palette-cell' style='background-color: #7DFFDF; color: black;'>7DFFDF</td><td class='vga-palette-cell' style='background-color: #7DFFFF; color: black;'>7DFFFF</td><td class='vga-palette-cell' style='background-color: #7DDFFF; color: black;'>7DDFFF</td><td class='vga-palette-cell' style='background-color: #7DBEFF; color: black;'>7DBEFF</td><td class='vga-palette-cell' style='background-color: #7D9EFF; color: black;'>7D9EFF</td></tr>
<tr>
<td class='vga-palette-cell' style='background-color: #B6B6FF; color: black;'>B6B6FF</td><td class='vga-palette-cell' style='background-color: #C7B6FF; color: black;'>C7B6FF</td><td class='vga-palette-cell' style='background-color: #DBB6FF; color: black;'>DBB6FF</td><td class='vga-palette-cell' style='background-color: #EBB6FF; color: black;'>EBB6FF</td><td class='vga-palette-cell' style='background-color: #FFB6FF; color: black;'>FFB6FF</td><td class='vga-palette-cell' style='background-color: #FFB6EB; color: black;'>FFB6EB</td><td class='vga-palette-cell' style='background-color: #FFB6DB; color: black;'>FFB6DB</td><td class='vga-palette-cell' style='background-color: #FFB6C7; color: black;'>FFB6C7</td><td class='vga-palette-cell' style='background-color: #FFB6B6; color: black;'>FFB6B6</td><td class='vga-palette-cell' style='background-color: #FFC7B6; color: black;'>FFC7B6</td><td class='vga-palette-cell' style='background-color: #FFDBB6; color: black;'>FFDBB6</td><td class='vga-palette-cell' style='background-color: #FFEBB6; color: black;'>FFEBB6</td><td class='vga-palette-cell' style='background-color: #FFFFB6; color: black;'>FFFFB6</td><td class='vga-palette-cell' style='background-color: #EBFFB6; color: black;'>EBFFB6</td><td class='vga-palette-cell' style='background-color: #DBFFB6; color: black;'>DBFFB6</td><td class='vga-palette-cell' style='background-color: #C7FFB6; color: black;'>C7FFB6</td></tr>
<tr>
<td class='vga-palette-cell' style='background-color: #B6FFB6; color: black;'>B6FFB6</td><td class='vga-palette-cell' style='background-color: #B6FFC7; color: black;'>B6FFC7</td><td class='vga-palette-cell' style='background-color: #B6FFDB; color: black;'>B6FFDB</td><td class='vga-palette-cell' style='background-color: #B6FFEB; color: black;'>B6FFEB</td><td class='vga-palette-cell' style='background-color: #B6FFFF; color: black;'>B6FFFF</td><td class='vga-palette-cell' style='background-color: #B6EBFF; color: black;'>B6EBFF</td><td class='vga-palette-cell' style='background-color: #B6DBFF; color: black;'>B6DBFF</td><td class='vga-palette-cell' style='background-color: #B6C7FF; color: black;'>B6C7FF</td><td class='vga-palette-cell' style='background-color: #000071; color: white;'>000071</td><td class='vga-palette-cell' style='background-color: #1C0071; color: white;'>1C0071</td><td class='vga-palette-cell' style='background-color: #380071; color: white;'>380071</td><td class='vga-palette-cell' style='background-color: #550071; color: white;'>550071</td><td class='vga-palette-cell' style='background-color: #710071; color: white;'>710071</td><td class='vga-palette-cell' style='background-color: #710055; color: white;'>710055</td><td class='vga-palette-cell' style='background-color: #710038; color: white;'>710038</td><td class='vga-palette-cell' style='background-color: #71001C; color: white;'>71001C</td></tr>
<tr>
<td class='vga-palette-cell' style='background-color: #710000; color: white;'>710000</td><td class='vga-palette-cell' style='background-color: #711C00; color: white;'>711C00</td><td class='vga-palette-cell' style='background-color: #713800; color: white;'>713800</td><td class='vga-palette-cell' style='background-color: #715500; color: white;'>715500</td><td class='vga-palette-cell' style='background-color: #717100; color: white;'>717100</td><td class='vga-palette-cell' style='background-color: #557100; color: white;'>557100</td><td class='vga-palette-cell' style='background-color: #387100; color: white;'>387100</td><td class='vga-palette-cell' style='background-color: #1C7100; color: white;'>1C7100</td><td class='vga-palette-cell' style='background-color: #007100; color: white;'>007100</td><td class='vga-palette-cell' style='background-color: #00711C; color: white;'>00711C</td><td class='vga-palette-cell' style='background-color: #007138; color: white;'>007138</td><td class='vga-palette-cell' style='background-color: #007155; color: white;'>007155</td><td class='vga-palette-cell' style='background-color: #007171; color: white;'>007171</td><td class='vga-palette-cell' style='background-color: #005571; color: white;'>005571</td><td class='vga-palette-cell' style='background-color: #003871; color: white;'>003871</td><td class='vga-palette-cell' style='background-color: #001C71; color: white;'>001C71</td></tr>
<tr>
<td class='vga-palette-cell' style='background-color: #383871; color: white;'>383871</td><td class='vga-palette-cell' style='background-color: #453871; color: white;'>453871</td><td class='vga-palette-cell' style='background-color: #553871; color: white;'>553871</td><td class='vga-palette-cell' style='background-color: #613871; color: white;'>613871</td><td class='vga-palette-cell' style='background-color: #713871; color: white;'>713871</td><td class='vga-palette-cell' style='background-color: #713861; color: white;'>713861</td><td class='vga-palette-cell' style='background-color: #713855; color: white;'>713855</td><td class='vga-palette-cell' style='background-color: #713845; color: white;'>713845</td><td class='vga-palette-cell' style='background-color: #713838; color: white;'>713838</td><td class='vga-palette-cell' style='background-color: #714538; color: white;'>714538</td><td class='vga-palette-cell' style='background-color: #715538; color: white;'>715538</td><td class='vga-palette-cell' style='background-color: #716138; color: white;'>716138</td><td class='vga-palette-cell' style='background-color: #717138; color: white;'>717138</td><td class='vga-palette-cell' style='background-color: #617138; color: white;'>617138</td><td class='vga-palette-cell' style='background-color: #557138; color: white;'>557138</td><td class='vga-palette-cell' style='background-color: #457138; color: white;'>457138</td></tr>
<tr>
<td class='vga-palette-cell' style='background-color: #387138; color: white;'>387138</td><td class='vga-palette-cell' style='background-color: #387145; color: white;'>387145</td><td class='vga-palette-cell' style='background-color: #387155; color: white;'>387155</td><td class='vga-palette-cell' style='background-color: #387161; color: white;'>387161</td><td class='vga-palette-cell' style='background-color: #387171; color: white;'>387171</td><td class='vga-palette-cell' style='background-color: #386171; color: white;'>386171</td><td class='vga-palette-cell' style='background-color: #385571; color: white;'>385571</td><td class='vga-palette-cell' style='background-color: #384571; color: white;'>384571</td><td class='vga-palette-cell' style='background-color: #515171; color: white;'>515171</td><td class='vga-palette-cell' style='background-color: #595171; color: white;'>595171</td><td class='vga-palette-cell' style='background-color: #615171; color: white;'>615171</td><td class='vga-palette-cell' style='background-color: #695171; color: white;'>695171</td><td class='vga-palette-cell' style='background-color: #715171; color: white;'>715171</td><td class='vga-palette-cell' style='background-color: #715169; color: white;'>715169</td><td class='vga-palette-cell' style='background-color: #715161; color: white;'>715161</td><td class='vga-palette-cell' style='background-color: #715159; color: white;'>715159</td></tr>
<tr>
<td class='vga-palette-cell' style='background-color: #715151; color: white;'>715151</td><td class='vga-palette-cell' style='background-color: #715951; color: white;'>715951</td><td class='vga-palette-cell' style='background-color: #716151; color: white;'>716151</td><td class='vga-palette-cell' style='background-color: #716951; color: white;'>716951</td><td class='vga-palette-cell' style='background-color: #717151; color: white;'>717151</td><td class='vga-palette-cell' style='background-color: #697151; color: white;'>697151</td><td class='vga-palette-cell' style='background-color: #617151; color: white;'>617151</td><td class='vga-palette-cell' style='background-color: #597151; color: white;'>597151</td><td class='vga-palette-cell' style='background-color: #517151; color: white;'>517151</td><td class='vga-palette-cell' style='background-color: #517159; color: white;'>517159</td><td class='vga-palette-cell' style='background-color: #517161; color: white;'>517161</td><td class='vga-palette-cell' style='background-color: #517169; color: white;'>517169</td><td class='vga-palette-cell' style='background-color: #517171; color: white;'>517171</td><td class='vga-palette-cell' style='background-color: #516971; color: white;'>516971</td><td class='vga-palette-cell' style='background-color: #516171; color: white;'>516171</td><td class='vga-palette-cell' style='background-color: #515971; color: white;'>515971</td></tr>
<tr>
<td class='vga-palette-cell' style='background-color: #000041; color: white;'>000041</td><td class='vga-palette-cell' style='background-color: #100041; color: white;'>100041</td><td class='vga-palette-cell' style='background-color: #200041; color: white;'>200041</td><td class='vga-palette-cell' style='background-color: #300041; color: white;'>300041</td><td class='vga-palette-cell' style='background-color: #410041; color: white;'>410041</td><td class='vga-palette-cell' style='background-color: #410030; color: white;'>410030</td><td class='vga-palette-cell' style='background-color: #410020; color: white;'>410020</td><td class='vga-palette-cell' style='background-color: #410010; color: white;'>410010</td><td class='vga-palette-cell' style='background-color: #410000; color: white;'>410000</td><td class='vga-palette-cell' style='background-color: #411000; color: white;'>411000</td><td class='vga-palette-cell' style='background-color: #412000; color: white;'>412000</td><td class='vga-palette-cell' style='background-color: #413000; color: white;'>413000</td><td class='vga-palette-cell' style='background-color: #414100; color: white;'>414100</td><td class='vga-palette-cell' style='background-color: #304100; color: white;'>304100</td><td class='vga-palette-cell' style='background-color: #204100; color: white;'>204100</td><td class='vga-palette-cell' style='background-color: #104100; color: white;'>104100</td></tr>
<tr>
<td class='vga-palette-cell' style='background-color: #004100; color: white;'>004100</td><td class='vga-palette-cell' style='background-color: #004110; color: white;'>004110</td><td class='vga-palette-cell' style='background-color: #004120; color: white;'>004120</td><td class='vga-palette-cell' style='background-color: #004130; color: white;'>004130</td><td class='vga-palette-cell' style='background-color: #004141; color: white;'>004141</td><td class='vga-palette-cell' style='background-color: #003041; color: white;'>003041</td><td class='vga-palette-cell' style='background-color: #002041; color: white;'>002041</td><td class='vga-palette-cell' style='background-color: #001041; color: white;'>001041</td><td class='vga-palette-cell' style='background-color: #202041; color: white;'>202041</td><td class='vga-palette-cell' style='background-color: #282041; color: white;'>282041</td><td class='vga-palette-cell' style='background-color: #302041; color: white;'>302041</td><td class='vga-palette-cell' style='background-color: #382041; color: white;'>382041</td><td class='vga-palette-cell' style='background-color: #412041; color: white;'>412041</td><td class='vga-palette-cell' style='background-color: #412038; color: white;'>412038</td><td class='vga-palette-cell' style='background-color: #412030; color: white;'>412030</td><td class='vga-palette-cell' style='background-color: #412028; color: white;'>412028</td></tr>
<tr>
<td class='vga-palette-cell' style='background-color: #412020; color: white;'>412020</td><td class='vga-palette-cell' style='background-color: #412820; color: white;'>412820</td><td class='vga-palette-cell' style='background-color: #413020; color: white;'>413020</td><td class='vga-palette-cell' style='background-color: #413820; color: white;'>413820</td><td class='vga-palette-cell' style='background-color: #414120; color: white;'>414120</td><td class='vga-palette-cell' style='background-color: #384120; color: white;'>384120</td><td class='vga-palette-cell' style='background-color: #304120; color: white;'>304120</td><td class='vga-palette-cell' style='background-color: #284120; color: white;'>284120</td><td class='vga-palette-cell' style='background-color: #204120; color: white;'>204120</td><td class='vga-palette-cell' style='background-color: #204128; color: white;'>204128</td><td class='vga-palette-cell' style='background-color: #204130; color: white;'>204130</td><td class='vga-palette-cell' style='background-color: #204138; color: white;'>204138</td><td class='vga-palette-cell' style='background-color: #204141; color: white;'>204141</td><td class='vga-palette-cell' style='background-color: #203841; color: white;'>203841</td><td class='vga-palette-cell' style='background-color: #203041; color: white;'>203041</td><td class='vga-palette-cell' style='background-color: #202841; color: white;'>202841</td></tr>
<tr>
<td class='vga-palette-cell' style='background-color: #2C2C41; color: white;'>2C2C41</td><td class='vga-palette-cell' style='background-color: #302C41; color: white;'>302C41</td><td class='vga-palette-cell' style='background-color: #342C41; color: white;'>342C41</td><td class='vga-palette-cell' style='background-color: #3C2C41; color: white;'>3C2C41</td><td class='vga-palette-cell' style='background-color: #412C41; color: white;'>412C41</td><td class='vga-palette-cell' style='background-color: #412C3C; color: white;'>412C3C</td><td class='vga-palette-cell' style='background-color: #412C34; color: white;'>412C34</td><td class='vga-palette-cell' style='background-color: #412C30; color: white;'>412C30</td><td class='vga-palette-cell' style='background-color: #412C2C; color: white;'>412C2C</td><td class='vga-palette-cell' style='background-color: #41302C; color: white;'>41302C</td><td class='vga-palette-cell' style='background-color: #41342C; color: white;'>41342C</td><td class='vga-palette-cell' style='background-color: #413C2C; color: white;'>413C2C</td><td class='vga-palette-cell' style='background-color: #41412C; color: white;'>41412C</td><td class='vga-palette-cell' style='background-color: #3C412C; color: white;'>3C412C</td><td class='vga-palette-cell' style='background-color: #34412C; color: white;'>34412C</td><td class='vga-palette-cell' style='background-color: #30412C; color: white;'>30412C</td></tr>
<tr>
<td class='vga-palette-cell' style='background-color: #2C412C; color: white;'>2C412C</td><td class='vga-palette-cell' style='background-color: #2C4130; color: white;'>2C4130</td><td class='vga-palette-cell' style='background-color: #2C4134; color: white;'>2C4134</td><td class='vga-palette-cell' style='background-color: #2C413C; color: white;'>2C413C</td><td class='vga-palette-cell' style='background-color: #2C4141; color: white;'>2C4141</td><td class='vga-palette-cell' style='background-color: #2C3C41; color: white;'>2C3C41</td><td class='vga-palette-cell' style='background-color: #2C3441; color: white;'>2C3441</td><td class='vga-palette-cell' style='background-color: #2C3041; color: white;'>2C3041</td><td class='vga-palette-cell' style='background-color: #000000; color: white;'>000000</td><td class='vga-palette-cell' style='background-color: #000000; color: white;'>000000</td><td class='vga-palette-cell' style='background-color: #000000; color: white;'>000000</td><td class='vga-palette-cell' style='background-color: #000000; color: white;'>000000</td><td class='vga-palette-cell' style='background-color: #000000; color: white;'>000000</td><td class='vga-palette-cell' style='background-color: #000000; color: white;'>000000</td><td class='vga-palette-cell' style='background-color: #000000; color: white;'>000000</td><td class='vga-palette-cell' style='background-color: #000000; color: white;'>000000</td></tr>
</table>

## Primary Emulation Resources

- (int10h.org) [The IBM 5153's True CGA Palette and Color Output](https://int10h.org/blog/2022/06/ibm-5153-color-true-cga-palette/)