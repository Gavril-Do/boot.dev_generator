import unittest
from split_nodes import *

from textnode import TextNode, TextType

class TestInlineMarkdown(unittest.TestCase):
	def test_delim_bold(self):
		node = TextNode("This is text with a **bolded** word", TextType.TEXT)
		new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
		self.assertListEqual(
			[
				TextNode("This is text with a ", TextType.TEXT),
				TextNode("bolded", TextType.BOLD),
				TextNode(" word", TextType.TEXT),
			],
			new_nodes,
		)

	def test_delim_bold_double(self):
		node = TextNode(
			"This is text with a **bolded** word and **another**", TextType.TEXT
		)
		new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
		self.assertListEqual(
			[
				TextNode("This is text with a ", TextType.TEXT),
				TextNode("bolded", TextType.BOLD),
				TextNode(" word and ", TextType.TEXT),
				TextNode("another", TextType.BOLD),
			],
			new_nodes,
		)

	def test_delim_bold_multiword(self):
		node = TextNode(
			"This is text with a **bolded word** and **another**", TextType.TEXT
		)
		new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
		self.assertListEqual(
			[
				TextNode("This is text with a ", TextType.TEXT),
				TextNode("bolded word", TextType.BOLD),
				TextNode(" and ", TextType.TEXT),
				TextNode("another", TextType.BOLD),
			],
			new_nodes,
		)

	def test_delim_italic(self):
		node = TextNode("This is text with an *italic* word", TextType.TEXT)
		new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
		self.assertListEqual(
			[
				TextNode("This is text with an ", TextType.TEXT),
				TextNode("italic", TextType.ITALIC),
				TextNode(" word", TextType.TEXT),
			],
			new_nodes,
		)

	def test_delim_bold_and_italic(self):
		node = TextNode("**bold** and *italic*", TextType.TEXT)
		new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
		new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)
		self.assertEqual(
			[
				TextNode("bold", TextType.BOLD),
				TextNode(" and ", TextType.TEXT),
				TextNode("italic", TextType.ITALIC),
			],
			new_nodes,
		)

	def test_delim_code(self):
		node = TextNode("This is text with a `code block` word", TextType.TEXT)
		new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
		self.assertListEqual(
			[
				TextNode("This is text with a ", TextType.TEXT),
				TextNode("code block", TextType.CODE),
				TextNode(" word", TextType.TEXT),
			],
			new_nodes,
		)
		
class TestExtractImages(unittest.TestCase):
	def testextractimages1(self):
		text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
		self.assertEqual(
			extract_markdown_images(text),
			[('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')]
		)
	def testextractimages2(self):
		text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
		self.assertEqual(
			extract_markdown_images(text),
			[]
		)
	def testextractimages3(self):
		text = "This is some text with an image: ![to boot dev](https://www.boot.dev) (and something that might look like an image)."
		self.assertEqual(
			extract_markdown_images(text),
			[('to boot dev', 'https://www.boot.dev')]
		)
	def test_extract_markdown_images(self):
		matches = extract_markdown_images(
			"This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
		)
		self.assertListEqual([('image', 'https://i.imgur.com/zjjcJKZ.png')], matches)
		
class TestExtractLinks(unittest.TestCase):
	def testextractlinks1(self):
		text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
		self.assertEqual(
			extract_markdown_links(text),
			[]
		)
	def testextractlinks2(self):
		text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
		self.assertEqual(extract_markdown_links(text), [('to boot dev', 'https://www.boot.dev'), ('to youtube', 'https://www.youtube.com/@bootdotdev')])

	def testextractlinks3(self):
		text = "This is some text with a link: [to boot dev](https://www.boot.dev) (and something that might look like a link)."
		self.assertEqual(extract_markdown_links(text), [('to boot dev', 'https://www.boot.dev')])

	def test_extract_markdown_links(self):
		matches = extract_markdown_links("This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev)")
		self.assertListEqual([('link', 'https://boot.dev'), ('another link', 'https://blog.boot.dev')], matches)

class TestSplitNodesImages(unittest.TestCase):
	def test_split_image(self):
		node = TextNode(
			"This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
			TextType.TEXT,
		)
		new_nodes = split_nodes_image([node])
		self.assertListEqual(
			[
				TextNode("This is text with an ", TextType.TEXT),
				TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
			],
			new_nodes,
		)

	def test_split_image_single(self):
		node = TextNode(
			"![image](https://www.example.COM/IMAGE.PNG)",
			TextType.TEXT,
		)
		new_nodes = split_nodes_image([node])
		self.assertListEqual(
			[
				TextNode("image", TextType.IMAGE, "https://www.example.COM/IMAGE.PNG"),
			],
			new_nodes,
		)

	def test_split_images(self):
		node = TextNode(
			"This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
			TextType.TEXT,
		)
		new_nodes = split_nodes_image([node])
		self.assertListEqual(
			[
				TextNode("This is text with an ", TextType.TEXT),
				TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
				TextNode(" and another ", TextType.TEXT),
				TextNode(
					"second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
				),
			],
			new_nodes,
		)

	def test_split_links(self):
		node = TextNode(
			"This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows",
			TextType.TEXT,
		)
		new_nodes = split_nodes_link([node])
		self.assertListEqual(
			[
				TextNode("This is text with a ", TextType.TEXT),
				TextNode("link", TextType.LINK, "https://boot.dev"),
				TextNode(" and ", TextType.TEXT),
				TextNode("another link", TextType.LINK, "https://blog.boot.dev"),
				TextNode(" with text that follows", TextType.TEXT),
			],
			new_nodes,
		)

	def test_text_to_textnodes(self):
		nodes = text_to_textnodes(
			"This is **text** with an *italic* word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)"
		)
		self.assertListEqual(
			[
				TextNode("This is ", TextType.TEXT),
				TextNode("text", TextType.BOLD),
				TextNode(" with an ", TextType.TEXT),
				TextNode("italic", TextType.ITALIC),
				TextNode(" word and a ", TextType.TEXT),
				TextNode("code block", TextType.CODE),
				TextNode(" and an ", TextType.TEXT),
				TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
				TextNode(" and a ", TextType.TEXT),
				TextNode("link", TextType.LINK, "https://boot.dev"),
			],
			nodes,
		)

if __name__ == "__main__":
	unittest.main()
