# Custom mdbook plugins

## mdbook-bitfield

The `mdbook-bitfield` plugin converts TOML bitfield definitions into SVG diagrams and associated markdown blocks.

There are two ways to generate a bitfield diagram from a TOML specification:
 - An inline TOML bitfield definition can be specified using `` ```bitfield`` to start a code block.
 - A bitfield can be rendered from a definition in an external file via the syntax `{{#bitfield filename.toml#specific-register-definition}}`
 - To emit a heading before an external bitfield, add `h2` through `h6` before the filename, such as `{{#bitfield h3 filename.toml#specific-register-definition}}`.

## mdbook-csvtable

The `mdbook-csvtable` plugin renders a relative link to a CSV file as a markdown table.
A link takes the format ```{{#csvtable [filename.csv]}}```

## mdbook-overbar

The `mdbook-overbar` plugin converts active-low signal names written with a leading slash into a span with the `pcbook-overbar` class.

For example, `/RESET` becomes `<span class="pcbook-overbar">RESET</span>`.

The plugin only matches all-caps alphanumeric names with underscores. It skips fenced code blocks, inline code spans, Markdown links, URLs, and raw HTML tags.
