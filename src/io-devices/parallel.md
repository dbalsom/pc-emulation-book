# Parallel Ports

The parallel port as we know it was originally designed by [Centronics Data Computer Corporation](https://en.wikipedia.org/wiki/Centronics). 

Therefore, you will sometimes hear the parallel port described as the "Centronics" port or interface.

The parallel port, in contrast to the serial port, has eight data lines, or 8-bits in "parallel".

```bitfield
name = "Status Register"
bits = 8
description = "Buffered status pins from the printer."

[[register]]
name = "Status"
address = "X79h, X7Dh"
width = 8

[[fields]]
name = "/BUSY"
lsb = 7
width = 1
description = "0: The printer is busy and cannot accept data.<br>1: The printer is not busy and can receive data."

[[fields]]
name = "/ACK"
lsb = 6
width = 1
description = "0: The printer has acknowledged the last character and is ready to receive another.<br>1: The printer is processing (busy)."

[[fields]]
name = "PE"
lsb = 5
width = 1
description = "0: The printer reports it has paper.<br>1: The printer reports it is out of paper."

[[fields]]
name = "SLCT"
lsb = 4
width = 1
description = "0: The printer has not been selected (Printer offline)<br>1: The printer has been selected (Select/Online button pressed)"

[[fields]]
name = "/ERROR"
lsb = 3
width = 1
description = "0: The printer has encountered an error condition.<br>1: The printer reports no current error condition."

[[fields]]
name = "Unused"
lsb = 0
width = 3
description = "Unused"
```

```bitfield
name = "Control Register"
bits = 8
description = "Set control signals from the CPU to the printer."

[[register]]
name = "Control"
address = "X7Ah, X7Eh"
width = 8

[[fields]]
name = "Unused"
lsb = 5
width = 3
description = "Unused"

[[fields]]
name = "IRQEN"
lsb = 4
width = 1
description = "0: Disable interrupts.<br>1: Enable interrupts triggered by a rising edge of the /ACK pin."

[[fields]]
name = "SLCT_IN"
lsb = 3
width = 1
description = "0: Leave printer unselected.<br>1: Select the printer."

[[fields]]
name = "/INIT"
lsb = 2
width = 1
description = "0: Initialize the printer.<br>1: Do nothing."

[[fields]]
name = "ALF"
lsb = 1
width = 1
description = "0: Do not line-feed automatically.<br>1: Line-feed automatically."

[[fields]]
name = "STR"
lsb = 0
width = 1
description = "Data clock strobe to feed data into the printer."
```
