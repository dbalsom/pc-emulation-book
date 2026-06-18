# Electronics Concepts

You don't need to have a degree in Electronics Engineering to emulate the PC, but from time to time certain electrical concepts do come up, especially when discussing the schematics for the system. A complete overview of basic electronics theory is out of scope, but here are some refresher concepts.

## Resistance

[Resistance](https://en.wikipedia.org/wiki/Electrical_resistance_and_conductance) is a measurement of **opposition to the flow of electric current**. If you viewed electric current was water flowing through a flexible hose, pinching the hose would be analogous to increasing resistance. Resistance is often expressed as the symbol R, and the SI unit for resistance is the ohm (Ω). A common component with a specified resistance in ohms is called a **resistor**. 

On the PC, resistors appear as small, cylindrical objects with colored stripes. These stripes specify the resistance value. You can use a [resistor calculator](https://www.calculator.net/resistor-calculator.html) to determine the exact value from the color codes.

## Capacitance

[Capacitance](https://en.wikipedia.org/wiki/Capacitance) is a measure of the ability to store electric charge. Capacitance is often expressed as the symbol C and its SI unit is the farad (F). A common component with a specified capacitance in farads is called a **capacitor**. Capacitors on the original PC are typically used for power filtering - including the PC's infamous tantalum capacitors with a penchant for tiny explosions. Capacitors are also fundamental to the operation of the PC's game port and joysticks.

## Inductance 

[Inductance](https://en.wikipedia.org/wiki/Inductance) is a property of a conductor that resists changes in current flow. Flowing current in a conductor generates a magnetic field. Changes in current through the conductor create or **induce** a corresponding voltage that opposes this change. In the PC, this is typically encountered in the operation of the speaker, and the **deflection yoke** in the monitor. The principle of inductance and electromagnetism are also central to the operation of relays and electric motors.

## Impedance

[Impedance](https://en.wikipedia.org/wiki/Electrical_impedance) is the effective opposition a circuit presents to current in an AC or time-varying signal. Digital circuits are powered by DC, but their fast signal transitions behave like time-varying signals, so impedance effects still matter. Impedance is often expressed as the symbol Z. It's SI unit is also the ohm (Ω), but values for impedance can be given as [complex numbers](https://en.wikipedia.org/wiki/Complex_number). Don't let that scare you - discussion of impedance here will be limited to broad concepts.

Impedance typically comes up in context of characterizing a chip's output pins. In digital logic, typically a signal can be either logically high (a state equivalent to binary 1), or logically low (a state equivalent to binary 0).  However, a third state is possible, which is "neither 1 nor 0." In this state, the output pin has a very high impedance, or Z value. Thus this state is often called **High-Z**. In this state the pin will not source or sink much current, if any. It is almost as if the pin is disconnected from the circuit. 

An output pin that can enter a high-impedance or high-Z state is said to be a **tri-state** output. The main purpose of a tri-state output is to enable multiple **bus drivers** to attach to the same wire without electrical complications. Consider a video card with on-board video memory - its bus drivers must allow the CPU to read and write to this memory, but the video card needs to do so as well. The Output Enable (/OE) pin on a bus driver chip can allow one bus driver to 'detach' from the bus allowing the other access. 

Impedance is not always a desirable phenomenon. Long traces with high speed clocks can experience ringing or reflections due to **impedance mismatch**. The actual details are not salient to emulation discussions, but for this reason **termination resistors** are often employed on bus and clock lines to compensate for impedance mismatches and reduce undesirable effects.

**Terminators** were employed with many early electrical communications standards. **Termination packs** often needed to be installed in floppy drives, and special termination connectors attached to SCSI device chains and the ends of coaxial Ethernet cables.

## Push-Pull Output Drivers

A chip's pins are typically some kind of input pin or output pin, or both - in which case the pin is said to be **bidirectional**. 

A typical output pin is called a push-pull output. When a pin is an output pin and is emitting a logical `1`, it desires to drive its connected wire up to some standard voltage level. For the TTL logic in the PC, this is somewhere above about 2.4V. This causes the output pin to be a **source** of current. When an output pin is a logical `0`, it must attempt to do the opposite, or **sink** current, until the voltage level on the connected wire drops such that a connected input pin would read it as a logical `0`. 

It is important that multiple output drivers connected to the same wire not be active at the same time, or one may attempt to source current directly into another that is sinking it. This would cause very high power consumption and potential damage to the circuit.

## Open-Collector Outputs

Another form of output pin involves connecting the output directly to a transistor with its emitter connected to ground. An open-collector output cannot drive a high output voltage, so a [pull-up resistor](#pull-ups) is needed for each open-collector output pin. This can be thought of as a switch that connects the output pin to ground. When implemented with a MOSFET, this is called an **open-drain** output. 

One advantage of these sorts of outputs is that multiple open-collector or open-drain outputs can be connected to the same wire safely. Open-collector outputs are used to implement the PC's [keyboard interface](../motherboard/keyboard-interface.md) as well as to drive the PC's speaker.

## Floating Lines and Open Bus

If no driver is connected to a wire, or all the drivers connected to a wire are in the High-Z state, the conductor may be said to be **floating**.  If an input pin is connected to the same wire and attempts to read the logical value of a floating wire, the result may be unpredictable. With TTL logic chips such as the 74LS series that the PC is largely constructed of, these floating inputs will typically trend to a logical `1`. However, this is not guaranteed. When an entire bus of several wires is floating, this condition is called an **open bus**. Sometimes an open bus can effectively store the last value written to it due to capacitance in the wires themselves. 

Thankfully, unlike some video game console systems, nothing I have encountered on the PC relies on exact emulation of the PC's open bus behavior.

An open bus can be encountered in certain circumstances, like attempting to read an IO address for which no hardware device answers. A meaningless value will be returned.

## Pull-Ups

One way to prevent an open bus scenario is to connect bus wires to resistors connected to a positive voltage. These resistors usually have a large value, typically 4.7kΩ to 10kΩ. This produces a weak current flow but brings the wire up to the positive voltage where an attached input pin will read it as `1`. If an open-collector output is attached to the wire and switches on, a small amount of current will flow from the positive supply, through the resistor into the collector, pulling the wire low until the wire will read as `0` to an attached input pin. 

## Pull-Downs

In a similar fashion, a pull-down resistor is a resistor that connects a wire to ground. This produces a reliable low voltage that will be read as a logical `0`. Pull-down resistors are often used on transistor bases or MOSFET gates so the device remains off when no other signal is actively driving it. They can also be used with switches, 




