# ddb-alchemy-markdown-converter
A tool for converting markdown from different sources (D&D Beyond and Obsidian Publish) to Alchemy-proper formatted markdown.

## Features
This repository contains two main scripts:
- `ddb.py`: Formats markdown text copied from D&D Beyond
- `obsidian.py`: Formats markdown text copied from Obsidian Publish websites

Both scripts perform common transformations like:
- Removing URLs in links
- Removing images
- Replacing non-breaking spaces
- Removing backslashes
- Cleaning newlines around headers
- Replacing multiple newlines
- Cleaning bullet points

## Usage

### D&D Beyond Markdown Converter
The `ddb.py` script is specifically designed for formatting markdown copied from D&D Beyond. It includes special handling for:
- Converting horizontal lines to H1 headers
- Decreasing header sizes by one level

To use:
1. Copy and paste markdown from a D&D Beyond article into an `.md` file (e.g., `article.md`)
2. Run the script by executing `python src/ddb.py article.md`

### Obsidian Publish Markdown Converter
The `obsidian.py` script is designed for formatting markdown copied from Obsidian Publish websites. It includes special handling for:
- Converting equals sign underlines to H1 headers
- Converting horizontal lines to H2 headers

To use:
1. Copy and paste markdown from an Obsidian Publish website into an `.md` file (e.g., `article.md`)
2. Run the script by executing `python src/obsidian.py article.md`
