import re
from base import MarkdownProcessor

class DDBMarkdownProcessor(MarkdownProcessor):
    def process(self):
        """Apply all processing steps to the content."""
        if self.content is None:
            raise ValueError("No content to process")

        self.remove_urls_in_links()
        self.remove_images()
        self.replace_nbsp()
        self.convert_horizontal_lines_to_h1()
        self.remove_backslashes()
        self.decrease_header_sizes()
        self.clean_newlines_around_headers()
        self.clean_newlines_around_alt_headers()
        self.replace_multiple_newlines()
        self.clean_bullet_points()

        return self.content

    def convert_horizontal_lines_to_h1(self):
        """Replace any text followed by a horizontal line with that text as an H1 header."""
        self.content = re.sub(r'(.*\n)-{2,}\n', r'# \1\n', self.content)
        return self.content

    def decrease_header_sizes(self):
        """Find all headers and decrease their size by 1."""
        # Find all the headers in the markdown file
        headings = re.findall(r'\n(#+ .*)', self.content)

        for heading in headings:
            # Determine the current size of the heading
            size = heading.count('#')

            # If the heading size is not already 1 (which is the largest size)
            if size > 1:
                # Decrease the size by 1
                new_heading = heading.replace('#', '', 1)

                # Replace the original heading with the new heading in the content
                self.content = self.content.replace(heading, new_heading)

        return self.content

if __name__ == "__main__":
    processor = DDBMarkdownProcessor()
    processor.process_from_command_line()
