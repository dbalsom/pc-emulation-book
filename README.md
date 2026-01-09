# The PC Emulation Book

[Read the current preliminary version](https://book.martypc.net/) - Warning, there's not a ton of content completed.

Inspired by [Pandocs](https://gbdev.io/pandocs/) documentation for Gameboy emulator authors, this book is the start of what will be a long, laborious project of documenting everything you need to know to emulate an original IBM PC.

This book will (initially) describe two models of IBM machine due to their extreme commonalities:

 - The IBM Model 5150 Personal Computer
 - The IBM Model 5160 Personal Computer XT

In the future, who knows what it might grow to cover.

## Who are you and what are your qualifications to write a guide to PC emulation?

Humbly, I am the author of the IBM PC emulator [MartyPC](https://github.com/dbalsom/martypc). I would never claim that MartyPC is the best or most accurate emulator on earth, or that its device implementations are perfect. But in years that I have spent developing it I have learned a great deal about the IBM PC hardware, often the result of performing direct hardware research on one of the IBM 5150s I personally own. To run the demo [Area 5150](https://www.pouet.net/prod.php?which=91938) like MartyPC can, requires cycle-accurate emulation of many of the system components of the IBM PC, something I only achieved after hours of poring over captures from a 32-channel logic analyzer.

During development of MartyPC, I became jealous of the comprehensive documentation archives that many console emulation platforms enjoy. "There should be something like this for PC" was a constant, nagging thought. I always knew I wanted to do something about it. This is that something.

## Contribution Guidelines

I could certainly use help documenting everything - there's a lot of material to cover. However, I am forced to be extremely picky to maintain the quality level I am aiming for.

 - Editorial work is always appreciated. If you find a grammatical issue or find certain phrasing awkward, please suggest corrections or improvements.
 - Please, no AI-generated text. If I wanted to include AI written chapters I could have asked ChatGPT myself to write the whole thing.
 - Diagrams should ideally be in SVG format and display well using either light or dark themes. We can inject CSS into the SVG to change the colors per-theme, if necessary.
 - No scrapes / dumps of text from books or websites still under copyright protection (without explicit and documented permission).
    - Ideally, all text in the book should be of original authorship. This is our opportunity to clarify material, remove ambiguities, and create the clearest, most helpful documentation on the a particular topic available.
 - Please be knowledgable about the topic of your contributions. If you've never programmed or emulated a serial port, perhaps you should not write a chapter on the serial port. Yes, anyone can read and translate a datasheet, but the point of this work is to go beyond. And as any emulator author can tell you, the datasheets can lie.

## License

 - Except where otherwise noted, all content in this book is released into the public domain under Creative Commons CC0 1.0. See LICENSE. 

## Special Thanks To

 - modem7 of [minuszerodegrees.net](https://www.minuszerodegrees.net/), which remains the single best resource documenting the IBM 5150 and 5160 (and more)
 - The late David Jurgens for authoring [HELPPC](https://helppc.netcore2k.net/)
 - Ralf Brown for his many contributions [documenting the PC](https://www.cs.cmu.edu/~ralf/files.html)
 - Ken Shirriff for documenting all the things silicon
 - reenigne for being an amazing code wizard
 - Trixter for the constant encouragement and deep historical knowledge