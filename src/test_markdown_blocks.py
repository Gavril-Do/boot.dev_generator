import unittest
from markdown_blocks import *

class TestMarkdownToHTML(unittest.TestCase):
	def test_split_blocks(self):
		inline = "	 # This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n\n* this is the first list item in a list block\n* this is a list item\n* This is another list item\n\n"
		blocks = markdown_to_blocks(inline)
		self.assertEqual(
			blocks, [
				'# This is a heading',
				'This is a paragraph of text. It has some **bold** and *italic* words inside of it.',
				'* this is the first list item in a list block\n* this is a list item\n* This is another list item'
			]
		)

	def test_markdown_to_blocks(self):
		md = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
		blocks = markdown_to_blocks(md)
		self.assertEqual(
			blocks,
			[
				"This is **bolded** paragraph",
				"This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
				"* This is a list\n* with items",
			],
		)

	def test_markdown_to_blocks_newlines(self):
		md = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
		blocks = markdown_to_blocks(md)
		self.assertEqual(
			blocks,
			[
				"This is **bolded** paragraph",
				"This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
				"* This is a list\n* with items",
			],
		)


if __name__ == "__main__":
	unittest.main()
