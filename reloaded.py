import re
import sys

# Check if the script was run with a command line argument
if len(sys.argv) != 2:
    print("Usage: python test.py <filename>")
    sys.exit(1)

# Get the filename from the command line arguments
filename = sys.argv[1]

# Open the file in read mode and read its content
with open(filename, 'r') as file:
    content = file.read()

# Use a regular expression to remove the URLs in links, keeping the link text
content = re.sub(r'\[(.*?)]\(.*?\)', r'\1', content)

# Remove images
content = re.sub(r'!\[.*?]\(.*?\)', '', content)

# Replace NBSP characters with normal space characters
content = content.replace('\xa0', ' ')

# Replace headers with equals sign underlines with H1 headers
content = re.sub(r'(.*)\n=+\n', r'# \1\n', content)

# Replace any text followed by a horizontal line with that text as an H2 header
content = re.sub(r'(.*\n)-{2,}\n', r'## \1\n', content)

# Remove all backslashes
content = re.sub(r'\\', '', content)

# Remove unnecessary newlines between markdown headers and the subsequent text
content = re.sub(r'(^|[^\n])(#+ .*)\n\n+', r'\1\2\n', content)
content = re.sub(r'(^|\n)(#+ .*)\n\n+', r'\1\2\n', content)

# Remove unnecessary newlines between alternate style headers (with = or -) and the subsequent text
content = re.sub(r'(.*\n[=\-]+\n)\n+', r'\1', content)

# Replace multiple consecutive newlines with a single newline
content = re.sub(r'\n{3,}', '\n\n', content)

# Open the file in write mode and overwrite it with the updated content
with open(filename, 'w') as file:
    file.write(content)
