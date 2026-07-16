# Monochrome Display Adapter (MDA)

<div style="text-align: center; margin: 1.5em 0;">
  <img src="../images/photos/mda_card_01.webp"
       alt="A photograph of a full-length ISA card in green, with a DE-9 connector and DB-25 parallel port at the I/O faceplate."
       style="max-width: 100%; max-height: 480px; height: auto;">
  <p style="font-style: italic; margin-top: 0.5em; opacity: 0.8;"><em>The IBM MDA card</em></p>
</div>

The IBM Monochrome Display Adapter (MDA) was one of the first video adapters available for the IBM PC, along with the IBM Color Graphics Adapter and the third-party Hercules video adapter.

> [!IMPORTANT] 
> The MDA is built around the [Motorola MC6845 CRTC](6845.md). Read that chapter first for a basic understanding of how the CRTC is used to define frame geometry and draw the screen.

## At a Glance

| Item                    | Description                                      |
| ----------------------- | ------------------------------------------------ |
| Video memory            | **4KiB** at `B000:0`, mirrored 8x through `B700:0`|
| Expansion ROM           | None                                             |
| Font ROM                | **8KiB** Character generator ROM, 8x14 glyphs    |
| Main display outputs    | TTL monochrome video on DE-9,                    |
| Typical text modes      | **80x25**, 4 shades, **9x14** character cell     |
| Standard Resolution     | **720x350** @ 50Hz                               |
| Standard graphics modes | None                                             |
| I/O address range       | `3B0h`-`3BFh`                                    |
| CRTC address port       | `3B4h` standard, `3B0h`, `3B2h`, `3B6h` alternate*|
| CRTC data port          | `3B5h` standard, `3B1h`, `3B3h`, `3B7h` alternate*|
| MDA control ports       | `3B8h` mode control                              |
| MDA status port         | `3BAh`                                           |
| Parallel port           | `3BCh`-`3BEh`                                    |
| Interrupts              | No display interrupt; printer interface uses `IRQ7` |
| DMA                     | None                                             |

The MDA was intended for use with the **IBM 5151 Personal Computer Display**. This monitor plugged into the back of the PC's power supply and turned on and off with the system. The MDA card itself was only capable of displaying **text mode**, but the monitor itself could display graphics, which cards like the **Hercules Graphics Adapter** took advantage of to provide a tempting upgrade for 5151 owners.

The MDA has 4KiB of DRAM dedicated to video memory — enough to hold a single 80x25 screen's worth of text. It also has an 8KiB font ROM that holds bit patterns for drawing text glyphs.

The MDA's 4KiB of DRAM at segment `B000:0` is incompletely decoded, causing eight mirrors of video memory from `B000:0` through `B700:FFFF`. This ends at the CGA's memory address of `B8000`. Along with the different base IO address, this allowed one to install both an MDA card and a CGA card in the same system for an early dual-monitor setup.

The MDA has no on-board **video BIOS** or expansion ROM. All PC-compatible BIOS implementations must therefore know how to identify, initialize and operate an MDA card in order to provide standard [int 10h](https://en.wikipedia.org/wiki/INT_10H) services.

In text mode, the MDA card was capable of outputting 3 grayscale shades and black, using two output pins of its DE-9 video connector. Some early MDA cards could be coerced into showing 16 colors.[^1]

The MDA contains a 16.257MHz crystal. The refresh rate is approximately 50Hz.

The IBM MDA card included a [parallel printer port](../io-devices/parallel.md). See that section for more details.

> [!NOTE]
> **\*** Incomplete decoding of the CRTC registers means the two CRTC ports are repeated four times. Some software titles may rely on these alternate port numbers.

### MDA Character Glyphs (Standard Font)

The standard MDA character glyphs are shown below.

<!-- cSpell:disable -->
<div class="mda-ascii-table-wrap">
	<table class="mda-ascii-table">
		<tr>
			<th class="corner" aria-hidden="true"></th>
			<th scope="col">0</th>
			<th scope="col">1</th>
			<th scope="col">2</th>
			<th scope="col">3</th>
			<th scope="col">4</th>
			<th scope="col">5</th>
			<th scope="col">6</th>
			<th scope="col">7</th>
			<th scope="col">8</th>
			<th scope="col">9</th>
			<th scope="col">A</th>
			<th scope="col">B</th>
			<th scope="col">C</th>
			<th scope="col">D</th>
			<th scope="col">E</th>
			<th scope="col">F</th>
		</tr>
		<tr>
			<th scope="row">0</th>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="00" aria-label="00" style="background-position: 0px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="01" aria-label="01" style="background-position: -16px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="02" aria-label="02" style="background-position: -32px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="03" aria-label="03" style="background-position: -48px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="04" aria-label="04" style="background-position: -64px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="05" aria-label="05" style="background-position: -80px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="06" aria-label="06" style="background-position: -96px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="07" aria-label="07" style="background-position: -112px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="08" aria-label="08" style="background-position: -128px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="09" aria-label="09" style="background-position: -144px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="0A" aria-label="0A" style="background-position: -160px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="0B" aria-label="0B" style="background-position: -176px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="0C" aria-label="0C" style="background-position: -192px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="0D" aria-label="0D" style="background-position: -208px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="0E" aria-label="0E" style="background-position: -224px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="0F" aria-label="0F" style="background-position: -240px 0px;"></span>
			</td>
		</tr>
		<tr>
			<th scope="row">1</th>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="10" aria-label="10" style="background-position: -256px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="11" aria-label="11" style="background-position: -272px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="12" aria-label="12" style="background-position: -288px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="13" aria-label="13" style="background-position: -304px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="14" aria-label="14" style="background-position: -320px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="15" aria-label="15" style="background-position: -336px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="16" aria-label="16" style="background-position: -352px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="17" aria-label="17" style="background-position: -368px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="18" aria-label="18" style="background-position: -384px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="19" aria-label="19" style="background-position: -400px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="1A" aria-label="1A" style="background-position: -416px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="1B" aria-label="1B" style="background-position: -432px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="1C" aria-label="1C" style="background-position: -448px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="1D" aria-label="1D" style="background-position: -464px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="1E" aria-label="1E" style="background-position: -480px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="1F" aria-label="1F" style="background-position: -496px 0px;"></span>
			</td>
		</tr>
		<tr>
			<th scope="row">2</th>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="20" aria-label="20" style="background-position: -512px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="21" aria-label="21" style="background-position: -528px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="22" aria-label="22" style="background-position: -544px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="23" aria-label="23" style="background-position: -560px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="24" aria-label="24" style="background-position: -576px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="25" aria-label="25" style="background-position: -592px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="26" aria-label="26" style="background-position: -608px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="27" aria-label="27" style="background-position: -624px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="28" aria-label="28" style="background-position: -640px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="29" aria-label="29" style="background-position: -656px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="2A" aria-label="2A" style="background-position: -672px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="2B" aria-label="2B" style="background-position: -688px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="2C" aria-label="2C" style="background-position: -704px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="2D" aria-label="2D" style="background-position: -720px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="2E" aria-label="2E" style="background-position: -736px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="2F" aria-label="2F" style="background-position: -752px 0px;"></span>
			</td>
		</tr>
		<tr>
			<th scope="row">3</th>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="30" aria-label="30" style="background-position: -768px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="31" aria-label="31" style="background-position: -784px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="32" aria-label="32" style="background-position: -800px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="33" aria-label="33" style="background-position: -816px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="34" aria-label="34" style="background-position: -832px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="35" aria-label="35" style="background-position: -848px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="36" aria-label="36" style="background-position: -864px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="37" aria-label="37" style="background-position: -880px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="38" aria-label="38" style="background-position: -896px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="39" aria-label="39" style="background-position: -912px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="3A" aria-label="3A" style="background-position: -928px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="3B" aria-label="3B" style="background-position: -944px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="3C" aria-label="3C" style="background-position: -960px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="3D" aria-label="3D" style="background-position: -976px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="3E" aria-label="3E" style="background-position: -992px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="3F" aria-label="3F" style="background-position: -1008px 0px;"></span>
			</td>
		</tr>
		<tr>
			<th scope="row">4</th>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="40" aria-label="40" style="background-position: -1024px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="41" aria-label="41" style="background-position: -1040px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="42" aria-label="42" style="background-position: -1056px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="43" aria-label="43" style="background-position: -1072px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="44" aria-label="44" style="background-position: -1088px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="45" aria-label="45" style="background-position: -1104px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="46" aria-label="46" style="background-position: -1120px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="47" aria-label="47" style="background-position: -1136px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="48" aria-label="48" style="background-position: -1152px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="49" aria-label="49" style="background-position: -1168px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="4A" aria-label="4A" style="background-position: -1184px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="4B" aria-label="4B" style="background-position: -1200px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="4C" aria-label="4C" style="background-position: -1216px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="4D" aria-label="4D" style="background-position: -1232px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="4E" aria-label="4E" style="background-position: -1248px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="4F" aria-label="4F" style="background-position: -1264px 0px;"></span>
			</td>
		</tr>
		<tr>
			<th scope="row">5</th>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="50" aria-label="50" style="background-position: -1280px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="51" aria-label="51" style="background-position: -1296px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="52" aria-label="52" style="background-position: -1312px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="53" aria-label="53" style="background-position: -1328px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="54" aria-label="54" style="background-position: -1344px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="55" aria-label="55" style="background-position: -1360px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="56" aria-label="56" style="background-position: -1376px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="57" aria-label="57" style="background-position: -1392px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="58" aria-label="58" style="background-position: -1408px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="59" aria-label="59" style="background-position: -1424px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="5A" aria-label="5A" style="background-position: -1440px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="5B" aria-label="5B" style="background-position: -1456px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="5C" aria-label="5C" style="background-position: -1472px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="5D" aria-label="5D" style="background-position: -1488px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="5E" aria-label="5E" style="background-position: -1504px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="5F" aria-label="5F" style="background-position: -1520px 0px;"></span>
			</td>
		</tr>
		<tr>
			<th scope="row">6</th>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="60" aria-label="60" style="background-position: -1536px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="61" aria-label="61" style="background-position: -1552px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="62" aria-label="62" style="background-position: -1568px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="63" aria-label="63" style="background-position: -1584px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="64" aria-label="64" style="background-position: -1600px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="65" aria-label="65" style="background-position: -1616px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="66" aria-label="66" style="background-position: -1632px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="67" aria-label="67" style="background-position: -1648px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="68" aria-label="68" style="background-position: -1664px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="69" aria-label="69" style="background-position: -1680px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="6A" aria-label="6A" style="background-position: -1696px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="6B" aria-label="6B" style="background-position: -1712px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="6C" aria-label="6C" style="background-position: -1728px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="6D" aria-label="6D" style="background-position: -1744px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="6E" aria-label="6E" style="background-position: -1760px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="6F" aria-label="6F" style="background-position: -1776px 0px;"></span>
			</td>
		</tr>
		<tr>
			<th scope="row">7</th>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="70" aria-label="70" style="background-position: -1792px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="71" aria-label="71" style="background-position: -1808px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="72" aria-label="72" style="background-position: -1824px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="73" aria-label="73" style="background-position: -1840px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="74" aria-label="74" style="background-position: -1856px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="75" aria-label="75" style="background-position: -1872px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="76" aria-label="76" style="background-position: -1888px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="77" aria-label="77" style="background-position: -1904px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="78" aria-label="78" style="background-position: -1920px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="79" aria-label="79" style="background-position: -1936px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="7A" aria-label="7A" style="background-position: -1952px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="7B" aria-label="7B" style="background-position: -1968px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="7C" aria-label="7C" style="background-position: -1984px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="7D" aria-label="7D" style="background-position: -2000px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="7E" aria-label="7E" style="background-position: -2016px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="7F" aria-label="7F" style="background-position: -2032px 0px;"></span>
			</td>
		</tr>
		<tr>
			<th scope="row">8</th>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="80" aria-label="80" style="background-position: -2048px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="81" aria-label="81" style="background-position: -2064px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="82" aria-label="82" style="background-position: -2080px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="83" aria-label="83" style="background-position: -2096px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="84" aria-label="84" style="background-position: -2112px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="85" aria-label="85" style="background-position: -2128px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="86" aria-label="86" style="background-position: -2144px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="87" aria-label="87" style="background-position: -2160px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="88" aria-label="88" style="background-position: -2176px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="89" aria-label="89" style="background-position: -2192px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="8A" aria-label="8A" style="background-position: -2208px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="8B" aria-label="8B" style="background-position: -2224px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="8C" aria-label="8C" style="background-position: -2240px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="8D" aria-label="8D" style="background-position: -2256px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="8E" aria-label="8E" style="background-position: -2272px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="8F" aria-label="8F" style="background-position: -2288px 0px;"></span>
			</td>
		</tr>
		<tr>
			<th scope="row">9</th>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="90" aria-label="90" style="background-position: -2304px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="91" aria-label="91" style="background-position: -2320px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="92" aria-label="92" style="background-position: -2336px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="93" aria-label="93" style="background-position: -2352px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="94" aria-label="94" style="background-position: -2368px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="95" aria-label="95" style="background-position: -2384px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="96" aria-label="96" style="background-position: -2400px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="97" aria-label="97" style="background-position: -2416px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="98" aria-label="98" style="background-position: -2432px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="99" aria-label="99" style="background-position: -2448px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="9A" aria-label="9A" style="background-position: -2464px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="9B" aria-label="9B" style="background-position: -2480px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="9C" aria-label="9C" style="background-position: -2496px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="9D" aria-label="9D" style="background-position: -2512px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="9E" aria-label="9E" style="background-position: -2528px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="9F" aria-label="9F" style="background-position: -2544px 0px;"></span>
			</td>
		</tr>
		<tr>
			<th scope="row">A</th>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="A0" aria-label="A0" style="background-position: -2560px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="A1" aria-label="A1" style="background-position: -2576px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="A2" aria-label="A2" style="background-position: -2592px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="A3" aria-label="A3" style="background-position: -2608px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="A4" aria-label="A4" style="background-position: -2624px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="A5" aria-label="A5" style="background-position: -2640px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="A6" aria-label="A6" style="background-position: -2656px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="A7" aria-label="A7" style="background-position: -2672px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="A8" aria-label="A8" style="background-position: -2688px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="A9" aria-label="A9" style="background-position: -2704px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="AA" aria-label="AA" style="background-position: -2720px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="AB" aria-label="AB" style="background-position: -2736px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="AC" aria-label="AC" style="background-position: -2752px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="AD" aria-label="AD" style="background-position: -2768px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="AE" aria-label="AE" style="background-position: -2784px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="AF" aria-label="AF" style="background-position: -2800px 0px;"></span>
			</td>
		</tr>
		<tr>
			<th scope="row">B</th>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="B0" aria-label="B0" style="background-position: -2816px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="B1" aria-label="B1" style="background-position: -2832px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="B2" aria-label="B2" style="background-position: -2848px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="B3" aria-label="B3" style="background-position: -2864px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="B4" aria-label="B4" style="background-position: -2880px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="B5" aria-label="B5" style="background-position: -2896px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="B6" aria-label="B6" style="background-position: -2912px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="B7" aria-label="B7" style="background-position: -2928px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="B8" aria-label="B8" style="background-position: -2944px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="B9" aria-label="B9" style="background-position: -2960px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="BA" aria-label="BA" style="background-position: -2976px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="BB" aria-label="BB" style="background-position: -2992px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="BC" aria-label="BC" style="background-position: -3008px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="BD" aria-label="BD" style="background-position: -3024px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="BE" aria-label="BE" style="background-position: -3040px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="BF" aria-label="BF" style="background-position: -3056px 0px;"></span>
			</td>
		</tr>
		<tr>
			<th scope="row">C</th>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="C0" aria-label="C0" style="background-position: -3072px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="C1" aria-label="C1" style="background-position: -3088px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="C2" aria-label="C2" style="background-position: -3104px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="C3" aria-label="C3" style="background-position: -3120px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="C4" aria-label="C4" style="background-position: -3136px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="C5" aria-label="C5" style="background-position: -3152px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="C6" aria-label="C6" style="background-position: -3168px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="C7" aria-label="C7" style="background-position: -3184px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="C8" aria-label="C8" style="background-position: -3200px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="C9" aria-label="C9" style="background-position: -3216px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="CA" aria-label="CA" style="background-position: -3232px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="CB" aria-label="CB" style="background-position: -3248px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="CC" aria-label="CC" style="background-position: -3264px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="CD" aria-label="CD" style="background-position: -3280px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="CE" aria-label="CE" style="background-position: -3296px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="CF" aria-label="CF" style="background-position: -3312px 0px;"></span>
			</td>
		</tr>
		<tr>
			<th scope="row">D</th>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="D0" aria-label="D0" style="background-position: -3328px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="D1" aria-label="D1" style="background-position: -3344px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="D2" aria-label="D2" style="background-position: -3360px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="D3" aria-label="D3" style="background-position: -3376px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="D4" aria-label="D4" style="background-position: -3392px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="D5" aria-label="D5" style="background-position: -3408px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="D6" aria-label="D6" style="background-position: -3424px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="D7" aria-label="D7" style="background-position: -3440px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="D8" aria-label="D8" style="background-position: -3456px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="D9" aria-label="D9" style="background-position: -3472px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="DA" aria-label="DA" style="background-position: -3488px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="DB" aria-label="DB" style="background-position: -3504px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="DC" aria-label="DC" style="background-position: -3520px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="DD" aria-label="DD" style="background-position: -3536px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="DE" aria-label="DE" style="background-position: -3552px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="DF" aria-label="DF" style="background-position: -3568px 0px;"></span>
			</td>
		</tr>
		<tr>
			<th scope="row">E</th>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="E0" aria-label="E0" style="background-position: -3584px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="E1" aria-label="E1" style="background-position: -3600px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="E2" aria-label="E2" style="background-position: -3616px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="E3" aria-label="E3" style="background-position: -3632px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="E4" aria-label="E4" style="background-position: -3648px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="E5" aria-label="E5" style="background-position: -3664px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="E6" aria-label="E6" style="background-position: -3680px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="E7" aria-label="E7" style="background-position: -3696px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="E8" aria-label="E8" style="background-position: -3712px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="E9" aria-label="E9" style="background-position: -3728px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="EA" aria-label="EA" style="background-position: -3744px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="EB" aria-label="EB" style="background-position: -3760px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="EC" aria-label="EC" style="background-position: -3776px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="ED" aria-label="ED" style="background-position: -3792px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="EE" aria-label="EE" style="background-position: -3808px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="EF" aria-label="EF" style="background-position: -3824px 0px;"></span>
			</td>
		</tr>
		<tr>
			<th scope="row">F</th>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="F0" aria-label="F0" style="background-position: -3840px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="F1" aria-label="F1" style="background-position: -3856px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="F2" aria-label="F2" style="background-position: -3872px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="F3" aria-label="F3" style="background-position: -3888px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="F4" aria-label="F4" style="background-position: -3904px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="F5" aria-label="F5" style="background-position: -3920px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="F6" aria-label="F6" style="background-position: -3936px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="F7" aria-label="F7" style="background-position: -3952px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="F8" aria-label="F8" style="background-position: -3968px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="F9" aria-label="F9" style="background-position: -3984px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="FA" aria-label="FA" style="background-position: -4000px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="FB" aria-label="FB" style="background-position: -4016px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="FC" aria-label="FC" style="background-position: -4032px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="FD" aria-label="FD" style="background-position: -4048px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="FE" aria-label="FE" style="background-position: -4064px 0px;"></span>
			</td>
			<td class="glyph-cell">
				<span class="glyph" tabindex="0" title="FF" aria-label="FF" style="background-position: -4080px 0px;"></span>
			</td>
		</tr>
	</table>
</div>
<!-- cSpell:enable -->


A visualization of the character font ROM is shown below, with bytes reversed and wrapping vertically to fit into a square image. The first half of the ROM is dedicated to the MDA's 8x14 font, which is encoded into 8x16 cells for alignment. Each cell is split into two 8x8 parts within the ROM due to addressing logic.

The same character ROM image is used for both MDA and CGA, so the CGA fonts follow the MDA font in the latter half of the ROM.

<div style="text-align: center; margin: 1.5em 0;">
  <img src="../images/bitmaps/5788005.u33.png"
       alt="A visualization of the CGA's character font ROM"
       data-modal-rendering="pixelated"
       style="max-height: 480px;"
       onclick="openModal(this)">
  <p style="font-style: italic; margin-top: 0.5em; opacity: 0.8;"><em>The MDA/CGA character font ROM (byte-reversed)</em></p>
</div>

The character font ROM is not accessible from the host PC. It can only be read by the MDA itself.

## Box Drawing Characters

Character codes `C0h—DFh` receive special treatment. When one of these characters is being rasterized, the eighth column is repeated to form the ninth column on the display. This allows the box drawing characters to connect seamlessly together across a 9-pixel character cell. 

<div style="text-align: center; margin: 1.5em 0;">
  <img src="../images/diagrams/mda_box_drawing_01.svg"
       alt="A diagram showing how the MDA duplicates the 8th column of the character glyph for box drawing characters"
       style="max-width: 100%; max-height: 640px; height: auto;">
  <p style="font-style: italic; margin-top: 0.5em; opacity: 0.8;"><em>MDA box drawing character rendering</em></p>
</div>

Note that `B0h—B2h` do not receive this treatment, so areas shaded with these characters will still have one pixel gaps between each character glyph.

## The MDA Registers

{{#bitfield h3 mda_registers.toml#mode-control-register}}

> [!CAUTION]
> IBM warns that the first thing that must be done to initialize the MDA is to set bit 0 of the mode control register to 1. 

Bit `0` of the mode control register selects the MDA's **dot clock**. When set to `1`, the onboard 16.257MHz crystal is used. If set to `0`, the clock is taken from an unpopulated pad. If the MDA's video memory is accessed while this bit is `0`, the MDA card will fail to drive the `IO_CH_READY` pin on the ISA bus high, and the CPU will hang. It is unclear what IBM's original intent for implementing this was, but perhaps they were simply keeping their options open for a future variant that supported additional resolutions and would have subsequently required a second clock source.

{{#bitfield h3 mda_registers.toml#status-register}}

The MDA's status register is very different from the CGA. The first bit reflects the HS pin from the 6845, delayed by one character clock. This differs from the CGA, which reports the inverted DE pin from the 6845. 

The MDA also lacks the vertical sync status bit. Instead, it has a type of *video mux* bit, **LVIDEO**. Querying bit 3 can test if an active pixel of any "color" other than black is being output. The IBM BIOS primarily uses this as a test during POST to ensure that the card is functioning. 

> [!TIP]
> When writing MDA emulation, implementing the **LVIDEO** bit may seem daunting. It is generally sufficient to set the latch if any pixel was output in the previous character clock (or even scanline) instead of requiring pixel-perfect accuracy. The IBM BIOS draws a row of solid block characters and tests that the bit is set immediately at the start of the frame. It is unknown if any software besides the BIOS POST relies on this bit for proper functionality.

## Light Pen

The very earliest models of the MDA card include a header to attach a light pen, similar to the CGA. This was removed on all subsequent versions of the card — the entire footprint was removed, not just left unpopulated, and in addition, the strobe signal to the 6845 and the two status bits for light pen operation were also disconnected and will always return `0`.

The P39 phosphors used in most monochrome displays were incompatible with early light pens for the PC, which may have influenced IBM's decision to remove light pen support from the MDA.

## Display Timings

The MDA has a 16.257MHz crystal. 

We can calculate the typical display field of the MDA from its normal CRTC parameters:

$$H_{\text{total}} = (R0 + 1) \times 9 = (97 + 1) \times 9 = 882$$

$$V_{\text{total}} = (R4 + 1) \times (R9 + 1) + R5 = (25 + 1) \times 14 + 6 = 370$$

$$\text{display field} = 882 \times 370$$

The horizontal and vertical refresh rates can then be derived:

$$f_{hsync} = \frac{16{,}257{,}000}{882} = 18.43 \text{ kHz}$$

$$f_{refresh} = \frac{16{,}257{,}000}{882 \times 370} = 49.82 \text{ Hz}$$

## BIOS Video Mode

The MDA typically uses standard `int10h` video mode `7`.

## CRTC Parameters

For the MDA's standard text mode, the MC6845 CRTC needs to be configured with the correct parameters for registers **R0-R11**. The standard CRTC parameters are given below.

<style>
.crtc-params-table {
  border-collapse: collapse;
}
.crtc-params-table th,
.crtc-params-table td {
  padding: 2px 6px;
}
</style>

<table class="crtc-params-table">
  <thead>
    <tr>
      <th rowspan="2">Register</th>
      <th rowspan="2">Name</th>
      <th class="header-group" colspan="1">Text Mode</th>
    </tr>
    <tr>
      <th class="header-group-member header-group-first header-group-last">80 Column</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>R0</th>
      <td>HorizontalTotal</td>
      <td>97</td>
    </tr>
    <tr>
      <th>R1</th>
      <td>HorizontalDisplayed</td>
      <td>80</td>
    </tr>
    <tr>
      <th>R2</th>
      <td>HorizontalSyncPosition</td>
      <td>82</td>
    </tr>
    <tr>
      <th>R3</th>
      <td>SyncWidth</td>
      <td>15</td>
    </tr>
    <tr>
      <th>R4</th>
      <td>VerticalTotal</td>
      <td>25</td>
    </tr>
    <tr>
      <th>R5</th>
      <td>VerticalTotalAdjust</td>
      <td>6</td>
    </tr>
    <tr>
      <th>R6</th>
      <td>VerticalDisplayed</td>
      <td>25</td>
    </tr>
    <tr>
      <th>R7</th>
      <td>VerticalSync</td>
      <td>25</td>
    </tr>
    <tr>
      <th>R8</th>
      <td>InterlaceMode</td>
      <td>2</td>
    </tr>
    <tr>
      <th>R9</th>
      <td>MaximumScanLineAddress</td>
      <td>13</td>
    </tr>
    <tr>
      <th>R10</th>
      <td>CursorStart</td>
      <td>11</td>
    </tr>
    <tr>
      <th>R11</th>
      <td>CursorEnd</td>
      <td>12</td>
    </tr>
  </tbody>
</table>

## Primary References

 - (seasip.org) [Monochrome Display Adapter: Notes](https://www.seasip.info/VintagePC/mda.html)
 - (minuszerodegress.net) [IBM Monochrome Display and Printer Adapter (MDA)](https://www.minuszerodegrees.net/5150_5160/cards/5150_5160_cards.htm#mda)

[^1]: VCFed forum thread, [Why did IBM create color MDA and just abandoned it?](https://forum.vcfed.org/index.php?threads/why-did-ibm-create-color-mda-and-just-abandoned-it.1252459/), April 2025.
