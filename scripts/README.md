# Custom mdbook plugins

## mdbook-bitfield

The `mdbook-bitfield` plugin converts inline blocks of toml that define a bitfield diagram into SVG.
An inline bitfield definition is created by using `\```toml_bitfield` to start a code block.

## mdbook-csvtable

The `mdbook-csvtable` plugin renders a relative link to a CSV file as a markdown table.
A link takes the format ```{{#csvtable [filename.csv]}}```