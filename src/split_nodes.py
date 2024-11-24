from textnode import *
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
	return_node_list = []
	if type(old_nodes) != list:
		raise ValueError("must be iterable object")
	for node in old_nodes:
		if node.text_type != TextType.TEXT:
			return_node_list.append(node)
			continue
		split_nodes = []
		sections = node.text.split(delimiter)
		if len(sections) % 2 == 0:
			raise Exception("Invalid markdown: formatted section not closed")
		for i in range(len(sections)):
			if sections[i] == "":
				continue
			if i % 2 == 0:
				split_nodes.append(TextNode(sections[i], TextType.TEXT))
			else:
				split_nodes.append(TextNode(sections[i], text_type))
		return_node_list.extend(split_nodes)
	return return_node_list

images_regex = re.compile(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", re.X)
def extract_markdown_images(text):
	tuple_list = re.findall(images_regex, text)
	return tuple_list

links_regex = re.compile(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", re.X)
def extract_markdown_links(text):
	tuple_list = re.findall(links_regex, text)
	return tuple_list

def split_nodes_image(old_nodes):
	new_nodes = []
	for node in old_nodes:
		if node.text_type != TextType.TEXT:
			new_nodes.append(node)
			continue
		original_text = node.text
		images = extract_markdown_images(original_text)
		if len(images) == 0:
			new_nodes.append(node)
			continue
		for image in images:
			sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
			if len(sections) != 2:
				raise ValueError("Invalid markdown: formatted section not closed")
			if sections[0] != "":
				new_nodes.append(TextNode((sections[0]), TextType.TEXT))
			new_nodes.append(
				TextNode(
					image[0],
					TextType.IMAGE,
					image[1],
				)
			)
			original_text = sections[1]
		if original_text != "":
			new_nodes.append(TextNode(original_text, TextType.TEXT))
	return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        original_text = node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(
				TextNode(
					link[0],
					TextType.LINK,
					link[1]
				)
			)
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes