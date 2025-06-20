import re
from base import MarkdownProcessor

class ObsidianMarkdownProcessor(MarkdownProcessor):
    def process(self):
        """Apply all processing steps to the content."""
        if self.content is None:
            raise ValueError("No content to process")

        self.remove_urls_in_links()
        self.remove_images()
        self.replace_nbsp()
        self.convert_equals_underlines_to_h1()
        self.convert_horizontal_lines_to_h2()
        self.remove_backslashes()
        self.clean_newlines_around_headers()
        self.clean_newlines_around_alt_headers()
        self.replace_multiple_newlines()
        self.clean_bullet_points()

        return self.content

    def convert_equals_underlines_to_h1(self):
        """Replace headers with equals sign underlines with H1 headers."""
        self.content = re.sub(r'(.*)\n=+\n', r'# \1\n', self.content)
        return self.content

    def convert_horizontal_lines_to_h2(self):
        """Replace any text followed by a horizontal line with that text as an H2 header."""
        self.content = re.sub(r'(.*\n)-{2,}\n', r'## \1\n', self.content)
        return self.content

if __name__ == "__main__":
    processor = ObsidianMarkdownProcessor()
    processor.process_from_command_line()
