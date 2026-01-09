# Summary

[Introduction](./introduction.md)

# Part I: System Architecture

- [Architecture Overview](./system-architecture/architecture-overview.md)

# Part II: The Intel 8088 CPU

- [Intel 8088 CPU](./cpu/8088-cpu.md)
  - [Architecture and Registers](./cpu/architecture.md)
  - [Instruction Set and Execution](./cpu/instructions.md)
  - [Bus Interface and Timing](./cpu/bus-timing.md)

# Part III: Support Chips

- [8259 Programmable Interrupt Controller](./support-chips/pic-8259.md)
- [8253 Programmable Interval Timer](./support-chips/timer-8253.md)
- [8255 Programmable Peripheral Interface](./support-chips/ppi-8255.md)
- [8237 DMA Controller](./support-chips/dma-8237.md)
- [8288 Bus Controller](./support-chips/bus-controller-8288.md)
- [8284 Clock/Ready Generator](./support-chips/clock-generator-8284.md)

# Part IV: Motherboard Logic and Functions

- [DIP switches](./motherboard/dip-switches.md)
- [Keyboard Interface](./motherboard/keyboard-interface.md)
- [DMA Page Registers](./motherboard/dma-page-registers.md)
- [DRAM Refresh](./motherboard/dram-refresh.md)
- [DMA and READY Generation](./motherboard/dma-ready-logic.md)

# Part V: Storage Devices

- [Floppy Disk Controller](./storage-devices/floppy-controller.md)
- [Hard Disk Controllers](./storage-devices/hard-disk-controllers.md)
  - [IBM/Xebec Hard Disk Controler](./storage-devices/ibm-xebec-controller.md)
  - [XTIDE](./storage-devices/xtide-controller.md)

# Part VI: Video Devices
- [Display Concepts](./display-graphics/display-concepts.md)
- [Motorola 6845 CRTC](./display-graphics/6845.md)
- [Monochrome Display Adapter (MDA)](./display-graphics/mda.md)
- [Color Graphics Adapter (CGA)](./display-graphics/cga.md)
- [Video Memory and Timing](./display-graphics/video-memory.md)

# Part VII: Input/Output Devices

- [Model F Keyboard](./io-devices/keyboard.md)
- [The PC Speaker](./io-devices/speaker.md)
- [The Cassette Interface](./io-devices/cassette.md)
- [Serial Ports](./io-devices/serial.md)
- [Parallel Ports](./io-devices/parallel.md)
- [The Game Port](./io-devices/game-port.md)
  - [Joysticks](./io-devices/joysticks.md)
- [Mice](./io-devices/mice.md)
  - [Microsoft Serial Mouse](./io-devices/ms-serial-mouse.md)
  - [Mouse Systems Serial Mouse](./io-devices/mouse-systems-serial-mouse.md)
- [Light Pen](./io-devices/light-pen.md)

# Part VIII: The ROM BIOS

 - [The IBM 5150 BIOS](./bios/5150-bios.md)
 - [The IBM 5160 BIOS](./bios/5160-bios.md)
 - [GLaBIOS](./bios/glabios.md)

# Part IX: Implementation

- [Emulation Architecture](./implementation/architecture.md)
- [CPU Emulation Techniques](./implementation/cpu-emulation.md)
- [Device Synchronization](./implementation/device-sync.md)
- [Performance Optimization](./implementation/performance.md)

# Part X: Testing and Debugging

- [Testing Strategies](./testing-debugging/testing.md)
- [Debugging Tools](./testing-debugging/debugging.md)
- [Compatibility Issues](./testing-debugging/compatibility.md)

# Appendices

- [ASCII Table](./appendices/ascii-table.md)
- [IBM PC Technical Specifications](./appendices/specs.md)
- [Memory Map](./appendices/memory-map.md)
- [BIOS Data Area](./appendices/bios-data-area.md)
- [I/O Port Reference](./appendices/io-ports.md)
- [BIOS Interrupt Reference](./appendices/bios-interrupts.md)

