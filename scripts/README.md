# Custom mdbook plugins

## mdbook-bitfield

The `mdbook-bitfield` plugin converts TOML bitfield definitions into SVG diagrams and associated markdown blocks.

There are two ways to generate a bitfield diagram from a TOML specification:
 - An inline TOML bitfield definition can be specified using `` ```bitfield`` to start a code block.
 - A bitfield can be rendered from a definition in an external file via the syntax `{{#bitfield filename.toml#specific-register-definition}}`

## mdbook-csvtable

The `mdbook-csvtable` plugin renders a relative link to a CSV file as a markdown table.
A link takes the format ```{{#csvtable [filename.csv]}}```
