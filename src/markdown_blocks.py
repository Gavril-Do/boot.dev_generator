import re
from enum import Enum
from split_nodes import *
from HTMLNode import *


block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"

# convert full markdown doc into single parent HTMLNode
def markdown_to_html_node(markdown):
	blocks = markdown_to_blocks(markdown)
	block_Nodes = []
	for block in blocks:
		html_node = block_to_html_node(block)
		block_Nodes.append(html_node)
	return ParentNode("div", block_Nodes, None)


def block_to_html_node(block):
	block_type = block_to_block_type(block)
	match(block_type):
		case("paragraph"):
			lines = block.split("\n")
			paragraph = " ".join(lines)
			children = text_to_children(paragraph)
			return ParentNode("p", children)
		case("heading"):
			level = 0
			for char in block:
				if char == "#":
					level += 1
				else:
					break
			if level + 1 >= len(block):
				raise ValueError(f"Invalid heading level: {level}")
			text = block[level +1 :]
			children = text_to_children(text)
			return ParentNode(f"h{level}", children)
		case("code"):
			if not block.startswith("```") or not block.endswith("```"):
				raise ValueError("Invalid code block")
			text = block[4:-3]
			children = text_to_children(text)
			code = ParentNode("code", children)
			return ParentNode("pre", [code])
		case("quote"):
			lines = block.split("\n")
			new_lines = []
			for line in lines:
				if not line.startswith(">"):
					raise ValueError("Invalid quote block")
				new_lines.append(line.lstrip(">").strip())
			content = " ".join(new_lines)
			children = text_to_children(content)
			return ParentNode("blockquote", children)
		case("ordered_list"):
			items = block.split("\n")
			html_items = []
			for item in items:
				text = item[3:]
				children = text_to_children(text)
				html_items.append(ParentNode("li", children))
			return ParentNode("ol", html_items)
		case("unordered_list"):
			items = block.split("\n")
			html_items = []
			for item in items:
				text = item[2:]
				children = text_to_children(text)
				html_items.append(ParentNode("li", children))
			return ParentNode("ul", html_items)
		case _:
			raise ValueError("Invlaid block type")

		# based on block type create new HTMLNode with proper data
		# assign proper child HTMLNode objects to block node
			# shared text_to_children function -- take string and return HTMLNode list
	# return block node children under single parent HTML node (div)
	# Quote blocks should be surrounded by a <blockquote> tag
	# Unordered list blocks should be surrounded by a <ul> tag, and each list item should be surrounded by a <li> tag
	# Ordered list blocks should be surrounded by a <ol> tag, and each list item should be surrounded by a <li> tag
	# code blocks should be surrounded by a <code> tag nested in a <pre> tag
	# headings should be surrounded by a <h1> to <h6> tag, depending on the number of # characters
	# paragraphs should be surrounded by a <p> tag

def text_to_children(text):
	text_to_nodes = text_to_textnodes(text)
	nodes_to_html = []
	for node in text_to_nodes:
		nodes_to_html.append(TextNode_to_HTMLNode(node))
	return nodes_to_html

def markdown_to_blocks(markdown):
	blocks = markdown.split("\n\n")
	filtered_blocks = []
	for block in blocks:
		if block == "":
			continue
		block = block.strip()
		filtered_blocks.append(block)
	return filtered_blocks

def block_to_block_type(block):
	lines = block.split("\n")

	if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
		return block_type_heading
	if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
		return block_type_code
	if block.startswith(">"):
		for line in lines:
			if not line.startswith(">"):
				return block_type_paragraph
		return block_type_quote
	if block.startswith("* "):
		for line in lines:
			if not line.startswith("* "):
				return block_type_paragraph
		return block_type_ulist
	if block.startswith("- "):
		for line in lines:
			if not line.startswith("- "):
				return block_type_paragraph
		return block_type_ulist
	if block.startswith("1. "):
		i = 1
		for line in lines:
			if not line.startswith(f"{i}. "):
				return block_type_paragraph
			i += 1
		return block_type_olist
	return block_type_paragraph