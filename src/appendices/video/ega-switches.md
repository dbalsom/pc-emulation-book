# EGA DIP Switch Settings

{{#csvtable ega-switches.csv}}

Most EGA clone cards used the same settings - perhaps defining special interpretations of the last four unused settings on the original IBM EGA.

VGA cards or other cards without such DIP switches emulated the closest appropriate DIP HEX value to store in the [BDA](../bios-data-area.md#ega-dip-switches).

Note that DIP switches are read by the PC logically reversed. A switch that is ON reads logical low (0) while a switch that is OFF reads logically high (1).

## Primary Emulation Resources

 - (minuszerodegrees.net) [IBM EGA - Installation Instructions](https://minuszerodegrees.net/ibm_ega/IBM%20EGA%20-%20Installation%20Instructions.pdf)