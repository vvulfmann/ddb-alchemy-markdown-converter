import re
import sys

class MarkdownProcessor:
    def __init__(self, filename=None):
        """Initialize the processor with an optional filename."""
        if filename:
            self.set_filename(filename)
        else:
            self.filename = None
            self.content = None

    def set_filename(self, filename):
        """Set the filename to process."""
        self.filename = filename
        self.content = None

    def process_from_command_line(self):
        """Process a file specified as a command line argument."""
        # Check if the script was run with a command line argument
        if len(sys.argv) != 2:
            print("Usage: python script.py <filename>")
            sys.exit(1)

        # Get the filename from the command line arguments
        self.set_filename(sys.argv[1])
        self.read_file()
        self.process()
        self.write_file()

    def read_file(self):
        """Read the content of the file."""
        if not self.filename:
            raise ValueError("Filename not set")

        # Open the file in read mode and read its content
        with open(self.filename, 'r') as file:
            self.content = file.read()

        return self.content

    def write_file(self):
        """Write the processed content back to the file."""
        if not self.filename or self.content is None:
            raise ValueError("Filename not set or content not processed")

        # Open the file in write mode and overwrite it with the updated content
        with open(self.filename, 'w') as file:
            file.write(self.content)

    def process(self):
        """Apply all processing steps to the content."""
        if self.content is None:
            raise ValueError("No content to process")

        self.remove_urls_in_links()
        self.remove_images()
        self.replace_nbsp()
        self.remove_backslashes()
        self.clean_newlines_around_headers()
        self.clean_newlines_around_alt_headers()
        self.replace_multiple_newlines()
        self.clean_bullet_points()

        return self.content

    def remove_urls_in_links(self):
        """Remove URLs in links, keeping only the link text."""
        self.content = re.sub(r'\[(.*?)]\(.*?\)', r'\1', self.content)
        return self.content

    def remove_images(self):
        """Remove images from the content."""
        self.content = re.sub(r'!\[.*?]\(.*?\)', '', self.content)
        return self.content

    def replace_nbsp(self):
        """Replace NBSP characters with normal space characters."""
        self.content = self.content.replace('\xa0', ' ')
        return self.content

    def remove_backslashes(self):
        """Remove all backslashes from the content."""
        self.content = re.sub(r'\\', '', self.content)
        return self.content

    def clean_newlines_around_headers(self):
        """Remove unnecessary newlines between markdown headers and the subsequent text."""
        self.content = re.sub(r'(^|[^\n])(#+ .*)\n\n+', r'\1\2\n', self.content)
        self.content = re.sub(r'(^|\n)(#+ .*)\n\n+', r'\1\2\n', self.content)
        return self.content

    def clean_newlines_around_alt_headers(self):
        """Remove unnecessary newlines between alternate style headers and the subsequent text."""
        self.content = re.sub(r'(.*\n[=\-]+\n)\n+', r'\1', self.content)
        return self.content

    def replace_multiple_newlines(self):
        """Replace multiple consecutive newlines with a single newline."""
        self.content = re.sub(r'\n{3,}', '\n\n', self.content)
        return self.content

    def clean_bullet_points(self):
        """Clean up newlines between bullet points."""
        for _ in range(3):  # Run multiple passes to catch nested cases
            # Remove unnecessary newlines between markdown bullet points (*, -, +)
            self.content = re.sub(r'([*\-+] .*)\n\n+([*\-+] )', r'\1\n\2', self.content)

            # Remove unnecessary newlines between markdown numbered bullet points (1., 1), etc.)
            self.content = re.sub(r'(\d+[.)] .*)\n\n+(\d+[.)] )', r'\1\n\2', self.content)

            # Remove unnecessary newlines between mixed bullet points (regular followed by numbered)
            self.content = re.sub(r'([*\-+] .*)\n\n+(\d+[.)] )', r'\1\n\2', self.content)

            # Remove unnecessary newlines between mixed bullet points (numbered followed by regular)
            self.content = re.sub(r'(\d+[.)] .*)\n\n+([*\-+] )', r'\1\n\2', self.content)

        return self.content
