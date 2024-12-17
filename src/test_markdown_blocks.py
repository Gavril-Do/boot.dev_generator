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
	
	def test_block_to_block_types(self):
		block = "# heading"
		self.assertEqual(block_to_block_type(block), block_type_heading)
		block = "```\ncode\n```"
		self.assertEqual(block_to_block_type(block), block_type_code)
		block = "> quote\n> more quote"
		self.assertEqual(block_to_block_type(block), block_type_quote)
		block = "* list\n* items"
		self.assertEqual(block_to_block_type(block), block_type_ulist)
		block = "1. list\n2. items"
		self.assertEqual(block_to_block_type(block), block_type_olist)
		block = "paragraph"
		self.assertEqual(block_to_block_type(block), block_type_paragraph)

	def test_text_to_children(self):
		md = "This is **text** with an *italic* word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)"
		nodes = [
			LeafNode(None, "This is ", None),
			LeafNode("b", "text", None),
			LeafNode(None, " with an ", None),
			LeafNode("i", "italic", None),
			LeafNode(None, " word and a ", None),
			LeafNode("code", "code block", None),
			LeafNode(None, " and an ", None),
			LeafNode("img", "", {'src': 'https://i.imgur.com/zjjcJKZ.png', 'alt': 'image'}),
			LeafNode(None, " and a ", None),
			LeafNode("a", "link", {'href': 'https://boot.dev'})
		]
		children = text_to_children(md)
		# print(children)
		for i in range(len(children)):
			# print(children[i])
			self.assertEqual(
				children[i].to_html(),
				nodes[i].to_html()
			)

	def test_markdown_to_html_node(self):
		md = "This is **text** with an *italic* word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)"
		node = markdown_to_html_node(md)
		# print(node.to_html())
		self.assertEqual(
			node.to_html(),
			'<div><p>This is <b>text</b> with an <i>italic</i> word and a <code>code block</code> and an <img src="https://i.imgur.com/zjjcJKZ.png" alt="image"></img> and a <a href="https://boot.dev">link</a></p></div>'
		)

	def test_paragraph(self):
		md = """
This is **bolded** paragraph
text in a p
tag here

"""

		node = markdown_to_html_node(md)
		html = node.to_html()
		self.assertEqual(
			html,
			"<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
		)

	def test_paragraphs(self):
		md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here

"""

		node = markdown_to_html_node(md)
		html = node.to_html()
		self.assertEqual(
			html,
			"<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
		)

	def test_lists(self):
		md = """
- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items

"""

		node = markdown_to_html_node(md)
		html = node.to_html()
		self.assertEqual(
			html,
			"<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
		)

	def test_headings(self):
		md = """
# this is an h1

this is paragraph text

## this is an h2
"""

		node = markdown_to_html_node(md)
		html = node.to_html()
		self.assertEqual(
			html,
			"<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
		)

	def test_blockquote(self):
		md = """
> This is a
> blockquote block

this is paragraph text

"""

		node = markdown_to_html_node(md)
		html = node.to_html()
		self.assertEqual(
			html,
			"<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
		)
	def test_codeblock(self):
		md = """
```
This is a code block
```

this is paragraph text

"""

		node = markdown_to_html_node(md)
		html = node.to_html()
		self.assertEqual(
			html,
			"<div><pre><code>This is a code block\n</code></pre><p>this is paragraph text</p></div>",
		)


if __name__ == "__main__":
	unittest.main()
