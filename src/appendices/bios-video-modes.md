# BIOS Video Modes

This table is courtesy of [minuszerodegrees.net]((https://www.minuszerodegrees.net/video/bios_video_modes.htm)).

<style type="text/css">
<!--
.sync_freqs_1 {background-color:#CCFFCC;}
.sync_freqs_2 {background-color:#FFFFEE;}
.sync_freqs_3 {background-color:#CCFFFF;}
.sync_freqs_4 {background-color:#FFCC99;}
.sync_freqs_5 {background-color:#FFCCFF;}
.dash_entry__ {background-color:#B4B4B4;}
.video-modes-table {
    font-size: 0.85em;
}
.video-modes-table td {
    padding: 2px 4px;
}
.video-modes-table th {
    padding: 2px 4px;
}
-->
</style>

<div class="video-modes-table">

<table style="width:1000px;">
  <tr>
	<td class="sync_freqs_1" style="width:30px;">&nbsp;</td>
	<td style="width:2000px;">&nbsp; = HSYNC: positive at 18.43 kHz, VSYNC: negative at 50 Hz</td>
  </tr>
  <tr>
	<td class="sync_freqs_2">&nbsp;</td>
	<td>&nbsp; = HSYNC: positive at 15.7 kHz, VSYNC: positive at 60 Hz &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(a.k.a. <a href="https://www.minuszerodegrees.net/mda_cga_ega/mda_cga_ega.htm#ega12">EGA Mode 1</a>)</td>
  </tr>
  <tr>
	<td class="sync_freqs_3">&nbsp;</td>
	<td>&nbsp; = HSYNC: positive at 21.85 kHz, VSYNC: negative at 60 Hz &nbsp;&nbsp;&nbsp;(a.k.a. <a href="https://www.minuszerodegrees.net/mda_cga_ega/mda_cga_ega.htm#ega12">EGA Mode 2</a> or EGA High Resolution)</td>
  </tr>
  <tr>
	<td class="sync_freqs_4">&nbsp;</td>
	<td>&nbsp; = HSYNC: 31.5 kHz, VSYNC: 70 Hz</td>
  </tr>
  <tr>
	<td class="sync_freqs_5">&nbsp;</td>
	<td>&nbsp; = HSYNC: 31.5 kHz, VSYNC: 60 Hz</td>
  </tr>
</table>
<br>

<table class="styTablePadded_1_4px_center" style="overflow:hidden; white-space:nowrap;">
       <tr>
         <th style="text-align:center; width: 50px;">&nbsp;</th>
         <th style="text-align:center; width: 70px;">Text /<br>Graphics</th>
         <th style="text-align:center; width:100px;">Size</th>
         <th style="text-align:center; width:120px;">Mono / Color /<br>Grayscale</th>
         <th style="text-align:center; width:120px;">IBM MDA card</th>
         <th style="text-align:center; width:120px;">IBM EGA<br>with<br>MDA monitor<br>(see note 1)</th>
         <th style="text-align:center; width:120px;">IBM CGA card</th>
         <th style="text-align:center; width:120px;">IBM PCjr /<br>Tandy 1000</th>
         <th style="text-align:center; width:140px;">IBM EGA card<br>with<br>CGA monitor<br>(see note 1)</th>
         <th style="text-align:center; width:140px;">IBM EGA card<br>with<br>EGA monitor</th>
         <th style="text-align:center; width:140px;">MCGA</th>
         <th style="text-align:center; width:140px;">Standard<br>VGA</th>
       </tr>
       <tr>
         <th>00h</th>
         <td>Text</td>
         <td>40x25 chars</td>
         <td>Grayscale</td>
         <td class="dash_entry__">-</td>
         <td class="dash_entry__">-</td>
         <td class="sync_freqs_2">Yes<br>shades:16<br>320x200<br>char:8x8</td>
         <td class="sync_freqs_2">Yes<br>shades:16<br>320x200<br>char:8x8</td>
         <td class="sync_freqs_2">Yes<br>shades:16<br>320x200<br>char:8x8</td>
         <td class="sync_freqs_3">Yes<br>shades:16<br>320x350<br>char:8x14</td>
         <td class="sync_freqs_4">Yes<br>shades:16<br>320x400<br>char:8x16</td>
         <td class="sync_freqs_4">Yes<br>shades:16<br>360x400<br>char:9x16</td>
       </tr>
       <tr>
         <th>01h</th>
         <td>Text</td>
         <td>40x25 chars</td>
         <td>Color</td>
         <td class="dash_entry__">-</td>
         <td class="dash_entry__">-</td>
         <td class="sync_freqs_2">Yes<br>Colors:16<br>320x200<br>char:8x8</td>
         <td class="sync_freqs_2">Yes<br>Colors:16<br>320x200<br>char:8x8</td>
         <td class="sync_freqs_2">Yes<br>Colors:16<br>320x200<br>char:8x8</td>
         <td class="sync_freqs_3">Yes<br>Colors:16<br>320x350<br>char:8x14</td>
         <td class="sync_freqs_4">Yes<br>Colors:16<br>320x400<br>char:8x16</td>
         <td class="sync_freqs_4">Yes<br>Colors:16<br>360x400<br>char:9x16</td>
       </tr>
       <tr>
         <th>02h</th>
         <td>Text</td>
         <td>80x25 chars</td>
         <td>Grayscale</td>
         <td class="dash_entry__">-</td>
         <td class="dash_entry__">-</td>
         <td class="sync_freqs_2">Yes<br>shades:16<br>640x200<br>char:8x8</td>
         <td class="sync_freqs_2">Yes<br>shades:16<br>640x200<br>char:8x8</td>
         <td class="sync_freqs_2">Yes<br>shades:16<br>640x200<br>char:8x8</td>
         <td class="sync_freqs_3">Yes<br>shades:16<br>640x350<br>char:8x14</td>
         <td class="sync_freqs_4">Yes<br>shades:16<br>640x400<br>char:8x16</td>
         <td class="sync_freqs_4">Yes<br>shades:16<br>720x400<br>char:9x16</td>
       </tr>
       <tr>
         <th>03h</th>
         <td>Text</td>
         <td>80x25 chars</td>
         <td>Color</td>
         <td class="dash_entry__">-</td>
         <td class="dash_entry__">-</td>
         <td class="sync_freqs_2">Yes<br>Colors:16<br>640x200<br>char:8x8</td>
         <td class="sync_freqs_2">Yes<br>Colors:16<br>640x200<br>char:8x8</td>
         <td class="sync_freqs_2">Yes<br>Colors:16<br>640x200<br>char:8x8</td>
         <td class="sync_freqs_3">Yes<br>Colors:16<br>640x350<br>char:8x14</td>
         <td class="sync_freqs_4">Yes<br>Colors:16<br>640x400<br>char:8x16</td>
         <td class="sync_freqs_4">Yes<br>Colors:16<br>720x400<br>char:9x16</td>
       </tr>
       <tr>
         <th>04h</th>
         <td>Graphics</td>
         <td>320x200</td>
         <td>Color</td>
         <td class="dash_entry__">-</td>
         <td class="dash_entry__">-</td>
         <td class="sync_freqs_2">Yes<br>Colors:4</td>
         <td class="sync_freqs_2">Yes<br>Colors:4</td>
         <td class="sync_freqs_2">Yes<br>Colors:4</td>
         <td class="sync_freqs_2">Yes<br>Colors:4</td>
         <td class="sync_freqs_4">Yes<br>Colors:4</td>
         <td class="sync_freqs_4">Yes<br>Colors:4</td>
       </tr>
       <tr>
         <th>05h</th>
         <td>Graphics</td>
         <td>320x200</td>
         <td>Grayscale</td>
         <td class="dash_entry__">-</td>
         <td class="dash_entry__">-</td>
         <td class="sync_freqs_2">Yes<br>shades:4</td>
         <td class="sync_freqs_2">Yes<br>shades:4</td>
         <td class="sync_freqs_2">Yes<br>shades:4</td>
         <td class="sync_freqs_2">Yes<br>shades:4</td>
         <td class="sync_freqs_4">Yes<br>shades:4</td>
         <td class="sync_freqs_4">Yes<br>shades:4</td>
       </tr>
       <tr>
         <th>06h</th>
         <td>Graphics</td>
         <td>640x200</td>
         <td>Mono</td>
         <td class="dash_entry__">-</td>
         <td class="dash_entry__">-</td>
         <td class="sync_freqs_2">Yes</td>
         <td class="sync_freqs_2">Yes</td>
         <td class="sync_freqs_2">Yes</td>
         <td class="sync_freqs_2">Yes</td>
         <td class="sync_freqs_4">Yes</td>
         <td class="sync_freqs_4">Yes</td>
       </tr>
       <tr>
         <th>07h</th>
         <td>Text</td>
         <td>80x25 chars</td>
         <td>Mono</td>
         <td class="sync_freqs_1">Yes<br>720x350<br>char:9x14</td>
         <td class="sync_freqs_1">Yes<br>720x350<br>char:9x14<br>(see note 2)</td>
         <td class="dash_entry__">-</td>
         <td class="dash_entry__">-</td>
         <td class="dash_entry__">-</td>
         <td class="dash_entry__">-</td>
         <td class="dash_entry__">-</td>
         <td class="dash_entry__">-</td>
       </tr>
       <tr>
         <th>08h</th>
         <td>Graphics</td>
         <td>160x200</td>
         <td>Color</td>
         <td class="dash_entry__">-</td>
         <td class="dash_entry__">-</td>
         <td class="dash_entry__">-</td>
         <td class="sync_freqs_2">Yes<br>Colors:16</td>
         <td class="dash_entry__">-</td>
         <td class="dash_entry__">-</td>
         <td class="dash_entry__">-</td>
         <td class="dash_entry__">-</td>
       </tr>
       <tr>
         <th>09h</th>
         <td>Graphics</td>
         <td>320x200</td>
         <td>Color</td>
         <td class="dash_entry__">-</td>
         <td class="dash_entry__">-</td>
         <td class="dash_entry__">-</td>
         <td class="sync_freqs_2">Yes<br>Colors:16</td>
         <td class="dash_entry__">-</td>
         <td class="dash_entry__">-</td>
         <td class="dash_entry__">-</td>
         <td class="dash_entry__">-</td>
       </tr>
       <tr>
         <th>0Ah</th>
         <td>Graphics</td>
         <td>640x200</td>
         <td>Color</td>
         <td class="dash_entry__">-</td>
         <td class="dash_entry__">-</td>
         <td class="dash_entry__">-</td>
         <td class="sync_freqs_2">Yes<br>Colors:4</td>
         <td class="dash_entry__">-</td>
         <td class="dash_entry__">-</td>
         <td class="dash_entry__">-</td>
         <td class="dash_entry__">-</td>
       </tr>
       <tr>
         <th>0Bh</th>
         <td>&nbsp;</td>
         <td>&nbsp;</td>
         <td>&nbsp;</td>
         <td class="dash_entry__">-</td>
         <td class="dash_entry__"><span style="font-style:italic;">[EGA internal use]</span></td>
         <td class="dash_entry__">-</td>
         <td class="dash_entry__">-</td>
         <td class="dash_entry__"><span style="font-style:italic;">[EGA internal use]</span></td>
         <td class="dash_entry__"><span style="font-style:italic;">[EGA internal use]</span></td>
         <td class="dash_entry__">-</td>
         <td class="dash_entry__">-</td>
       </tr>
       <tr>
         <th>0Ch</th>
         <td>&nbsp;</td>
         <td>&nbsp;</td>
         <td>&nbsp;</td>
         <td class="dash_entry__">-</td>
         <td class="dash_entry__"><span style="font-style:italic;">[EGA internal use]</span></td>
         <td class="dash_entry__">-</td>
         <td class="dash_entry__">-</td>
         <td class="dash_entry__"><span style="font-style:italic;">[EGA internal use]</span></td>
         <td class="dash_entry__"><span style="font-style:italic;">[EGA internal use]</span></td>
         <td class="dash_entry__">-</td>
         <td class="dash_entry__">-</td>
       </tr>
       <tr>
         <th>0Dh</th>
         <td>Graphics</td>
         <td>320x200</td>
         <td>Color</td>
         <td class="dash_entry__">-</td>
         <td class="dash_entry__">-</td>
         <td class="dash_entry__">-</td>
         <td class="dash_entry__">-</td>
         <td class="sync_freqs_2">Yes<br>Colors:16</td>
         <td class="sync_freqs_2">Yes<br>Colors:16</td>
         <td class="dash_entry__">-</td>
         <td class="sync_freqs_4">Yes<br>Colors:16</td>
       </tr>
       <tr>
         <th>0Eh</th>
         <td>Graphics</td>
         <td>640x200</td>
         <td>Color</td>
         <td class="dash_entry__">-</td>
         <td class="dash_entry__">-</td>
         <td class="dash_entry__">-</td>
         <td class="dash_entry__">-</td>
         <td class="sync_freqs_2">Yes<br>Colors:16</td>
         <td class="sync_freqs_2">Yes<br>Colors:16</td>
         <td class="dash_entry__">-</td>
         <td class="sync_freqs_4">Yes<br>Colors:16</td>
       </tr>
       <tr>
         <th>0Fh</th>
         <td>Graphics</td>
         <td>640x350</td>
         <td>Mono</td>
         <td class="dash_entry__">-</td>
         <td class="sync_freqs_1">Yes</td>
         <td class="dash_entry__">-</td>
         <td class="dash_entry__">-</td>
         <td class="dash_entry__">-</td>
         <td class="dash_entry__">-</td>
         <td class="dash_entry__">-</td>
         <td class="sync_freqs_4">Yes</td>
       </tr>
       <tr>
         <th>10h</th>
         <td>Graphics</td>
         <td>640x350</td>
         <td>Color</td>
         <td class="dash_entry__">-</td>
         <td class="dash_entry__">-</td>
         <td class="dash_entry__">-</td>
         <td class="dash_entry__">-</td>
         <td class="dash_entry__">-</td>
         <td class="sync_freqs_3">Yes<br>Colors:<br>4 for 64KB<br>16 for 128KB<br>(see note 3)</td>
         <td class="dash_entry__">-</td>
         <td class="sync_freqs_4">Yes<br>Colors:16</td>
       </tr>
       <tr>
         <th>11h</th>
         <td>Graphics</td>
         <td>640x480</td>
         <td>Mono</td>
         <td class="dash_entry__">-</td>
         <td class="dash_entry__">-</td>
         <td class="dash_entry__">-</td>
         <td class="dash_entry__">-</td>
         <td class="dash_entry__">-</td>
         <td class="dash_entry__">-</td>
         <td class="sync_freqs_5">Yes</td>
         <td class="sync_freqs_5">Yes</td>
       </tr>
       <tr>
         <th>12h</th>
         <td>Graphics</td>
         <td>640x480</td>
         <td>Color</td>
         <td class="dash_entry__">-</td>
         <td class="dash_entry__">-</td>
         <td class="dash_entry__">-</td>
         <td class="dash_entry__">-</td>
         <td class="dash_entry__">-</td>
         <td class="dash_entry__">-</td>
         <td class="dash_entry__">-</td>
         <td class="sync_freqs_5">Yes<br>Colors:16</td>
       </tr>
       <tr>
         <th>13h</th>
         <td>Graphics</td>
         <td>320x200</td>
         <td>Color</td>
         <td class="dash_entry__">-</td>
         <td class="dash_entry__">-</td>
         <td class="dash_entry__">-</td>
         <td class="dash_entry__">-</td>
         <td class="dash_entry__">-</td>
         <td class="dash_entry__">-</td>
         <td class="sync_freqs_4">Yes<br>Colors:256</td>
         <td class="sync_freqs_4">Yes<br>Colors:256</td>
       </tr>
</table>
</div>

<br>
<br>
<br>

#### Note 1:
Changing the monitor type on an IBM EGA card requires that switches on the IBM EGA card be changed.

#### Note 2:
Register and attribute behaviour is not quite the same as an MDA card. For more info, read the first page of the document [here](https://www.minuszerodegrees.net/video/PC%20Magazine%20Article%20-%20The%20EGA%20board%20-%20March1986.pdf).

#### Note 3:
4 Colors if 64KB of RAM fitted to EGA video card; 16 Colors if 128KB (or more) of RAM fitted.

## Primary Emulation Resources

 - (minuszerodegrees.net) [BIOS Video Modes](https://www.minuszerodegrees.net/video/bios_video_modes.htm)