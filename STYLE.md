# The PC Emulation Book Style Guide 

This is a guide for any potential contributors. I haven't had one yet, but if that's you, welcome!

## References & Citations

This section is first because it is the most important. 

**All text submitted for inclusion into the book should be of original authorship.**

Plagiarism is not simply copying a passage word for word - if you merely rephrase the same idea or thought without attribution, you are still plagiarizing. 

An exception to this strict plagiarism policy are official datasheets or white-papers released by the manufacturer. Tables and diagrams may be translated verbatim from such references as that was their inherent purpose. A link to the datasheet should be provided. I believe this is covered under fair use.

Technical information such as the material contained in this book can be tricky to source as we may have learned many of the facts we wish to document decades ago, and some of the original sources we may wish to cite to that end may be lost or forgotten. In general, this book seeks to use contemporary references that can be accessed on the live web - or at worst, available on the Internet Archive's [Wayback Machine](https://web.archive.org/).

Books, of course, are excellent sources. I would prefer books that are available online in some format, such as [Michael Abrash's Black Book](https://github.com/jagregory/abrash-black-book), or at least still available electronically or in print. If you cite a book nobody can acquire, I may ask to see a scan of the supporting section so I know that the reference supports what you are citing.

This book does not share Wikipedia's 'original research' prohibition. In the effort of improving emulation accuracy, original research is entirely the point.

There are several kinds of 'citation' available in Markdown and mdBook specifically, that I am still working out the standards for.  This is complicated by the fact that this is both a book and a web site.

Here are the basic options:

 - A markdown-style inline link 
     - This is good for linking to the definitions of glossary words when they first appear. Prefer Wikipedia for basic term definitions, unless Wikipedia has no article for that term. 
     - Also useful when directly discussing an external resource.
         - Good:
           > For a rather comprehensive review of the various titles that have used a tweaked text-mode over the years, see [this excellent post on the blog Nerdly Pleasures](https://nerdlypleasures.blogspot.com/2014/09/cga-16-color-rgb-graphics-modes.html).
         - The advantage of this style is it feels collaborative; it gives a shout-out to other retro-computing enthusiasts. This book does not need to go into as much depth as every other resource on the Internet in all cases, so deferring to those who have been all the way down the rabbit-hole is often the best call.

 - An mdbook-style citation
     - This style is appropriate when you are making a claim that directly comes from a unique source.
     - Citations are placed at the end of a line, *after the period*, using the bracket notation `[^1]`.
     - A matching citation entry should appear at the bottom of the page. Ideally, a citation should refer to a specific page number, or html anchor.
     - I'm looking into a custom bibliography system.

  - An HTML link
     - Should be used sparingly. Can be useful to credit/link to sources of inline images within a caption, or wherever else markdown is not supported.

  - A link in the 'Primary Resources' section.
     - The goal of the Primary Resources section is to call out the finest and most comprehensive resources on the subject available on the internet. Ideally they should be active web pages or links to a Wayback Machine snapshot. 
     - These would be the resources you would be using if the PC Emulation Book did not exist. You are still encouraged to use them!
     - Note: These can be used in conjunction with citations. Citations are more specific.

## Tone & Readability

Avoid use of the first person perspective. Use the second-person perspective sparingly.

The overall tone of the book I am going for is 'casual but precise'. Technical documentation can be very dry, so variety in language and presentation can help improve readability. Do not editorialize heavily, but the occasional quip keeps the text feeling human. 

 - Good: 
   > Since an extra row-counting bit has been added, we can now define up to **256** scanlines, easily fitting in our 200-line graphics mode, at the cost of an annoying interleaving scheme.
 - Bad:
   > The functioning of this controller is frustratingly obtuse, and frankly the people who designed it must have been drunk.

## Punctuation

Don't be afraid to use em-dashes (—) where grammatically correct, such as for expressing ranges: `1982—1984` or bracketing parenthetical injections. Use it sparingly — the key point is that if your readers notice the repetition, you're using them too much. Let's try not to sound like AI — that should be pretty easy to do when we're not actually AI.

## Chapter organization

Where appropriate (primarily for chapters on a specific device), include an initial **`At A Glance`** reference at the top of a chapter.  This is the place to put a quick reference of memory and port addresses used, IRQs and DMAs, associated extension ROMs, etc.

## Register Diagrams

All register definitions should use the md-bitfield plugin. Defining registers in an external TOML file and use the file-referencing form:

`{{#bitfield h3 mc6845_registers.toml#r8-interlace-mode}}`

I have plans to process all the register definition files, so having them externally defined is crucial to that goal.

## Diagrams

Any long, technical explanation that becomes somewhat hard to visualize may warrant an accompanying diagram. I recognize there is significant effort involved in making a diagram - especially a good one. Don't worry about matching the level of quality of existing diagrams in this book - we can spiff up any diagrams later. 

## Markdown Style

Each chapter should start with a single major header `#`, and use hierarchical organization of ideas, punctuated by lower-level headers.

Key glossary terms should typically be `**bolded**` when first introduced, or the first time they have been used in a chapter. Don't overdo bolded text in a single paragraph. 

Hexadecimal and binary numbers should be placed within backticks.

The format of hexadecimal numbers should be all capitals, padded with 0 where appropriate, and suffixed with a lowercase `h`.
 - correct: `0FFh`
 - incorrect: `0x0f`

Binary numbers typically do not need a suffix if enough context is provided that the number is binary. If it is unclear, suffix with `b`.

Admonitions can be used sparingly when information is important enough to interrupt normal document flow:

> [!NOTE]
> General information or additional context.

> [!TIP]
> A helpful suggestion or best practice.

> [!IMPORTANT]
> Key information that shouldn't be missed.

> [!WARNING]
> Critical information that highlights a potential risk.

> [!CAUTION]
> Information about potential issues that require caution.

## Accessibility

Try using a [colorblindness simulator](https://daltonlens.org/colorblindness-simulator) online to review any diagrams or illustrations.

The best advice that can be given is: avoid using color *alone* to convey information.  

Animations should avoid bright, flashing imagery.

All images should be included as HTML and include descriptive alt-text.

### Help Needed

I'm not an expert on accessibility. I could use help making the PC Emulation Book more accessible, especially in the areas of compatibility with screen readers, ARIA attributes, etc.



