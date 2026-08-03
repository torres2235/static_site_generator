import unittest
from block_markdown import (
    markdown_to_blocks,
    block_to_block_type,
    BlockType
)
class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    
    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_type_heading(self):
        block1 = "# Testing heading"
        block2 = "## Testing heading"
        block3 = "### Testing heading"
        block4 = "#### Testing heading"
        block5 = "##### Testing heading"
        block6 = "###### Testing heading"
        block7 = "####### Testing paragraph"

        block_types = [
            block_to_block_type(block1),
            block_to_block_type(block2),
            block_to_block_type(block3),
            block_to_block_type(block4),
            block_to_block_type(block5),
            block_to_block_type(block6),
            block_to_block_type(block7),
        ]
        self.assertEqual(
            block_types,
            [
                BlockType.HEADING,
                BlockType.HEADING,
                BlockType.HEADING,
                BlockType.HEADING,
                BlockType.HEADING,
                BlockType.HEADING,
                BlockType.PARAGRAPH,
            ]
        )

    def test_block_type_code(self):
        block="```\nThis section here should be block type code```"

        block_type = block_to_block_type(block)

        self.assertEqual(
            block_type,
            BlockType.CODE
        )

    def test_block_type_quote(self):
        block=">This section here should be block type quote"

        block_type = block_to_block_type(block)

        self.assertEqual(
            block_type,
            BlockType.QUOTE
        )

    def test_block_type_ulist(self):
        block="- This section here should be block type unordered list"

        block_type = block_to_block_type(block)

        self.assertEqual(
            block_type,
            BlockType.UNORDERED_LIST
        )

    def test_block_type_olist(self):
        block="1. This section here should be block type ordered list"

        block_type = block_to_block_type(block)

        self.assertEqual(
            block_type,
            BlockType.ORDERED_LIST
        )

if __name__ == "__main__":
    unittest.main()