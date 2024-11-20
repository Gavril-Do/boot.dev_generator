from textnode import *


def split_nodes_delimiter(old_nodes, delimiter, text_type):
	return_node_list = []
	if type(old_nodes) != list:
		raise ValueError("must be a list")
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
