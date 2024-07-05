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

# Replace any text followed by a horizontal line with that text as an H1 header
content = re.sub(r'(.*\n)-{2,}\n', r'# \1\n', content)

# Remove all markdown backslashes
content = re.sub(r'\\', '', content)

# Find all the headers in the markdown file
headings = re.findall(r'\n(#+ .*)', content)

for heading in headings:
    # Determine the current size of the heading
    size = heading.count('#')

    # If the heading size is not already 1 (which is the largest size)
    if size > 1:
        # Decrease the size by 1
        new_heading = heading.replace('#', '', 1)

        # Replace the original heading with the new heading in the content
        content = content.replace(heading, new_heading)

# Open the file in write mode and overwrite it with the updated content
with open(filename, 'w') as file:
    file.write(content)
