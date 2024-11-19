from textnode import *

class HTMLNode:
	def __init__(self, tag=None, value=None, children=None, props=None):
		self.tag = tag
		self.value = value
		self.children = children
		self.props = props

	def to_html(self):
		raise NotImplementedError("to_html method not implemented")
	
	# Return string that represents the HTML attributes of the node
	def props_to_html(self):
		if self.props == None:
			return ""
		string = ""
		for each in self.props:
			string += f' {each}="{self.props[each]}"'
		return string
	
	# print HTMLNode object to see it's tag, value, children, props for debug
	def __repr__(self):
		return f"HTMLNode(tag='{self.tag}', value='{self.value}', children='{self.children}', props='{self.props}')"
	
class ParentNode(HTMLNode):
	def __init__(self, tag, children, props=None):
		super().__init__(tag, None, children, props)

	def to_html(self):
		if self.tag == None or self.tag == "":
			raise ValueError(f"Invalid HTML: no tag")
		if self.children == None or self.children == []:
			raise ValueError(f"Invalid HTML: no children")
		node_str = ""
		for each in self.children:
			node_str += each.to_html()
		return f"<{self.tag}{self.props_to_html()}>{node_str}</{self.tag}>"
	
	def __repr__(self):
		return f"ParentNode(tag={self.tag}, children={self.children}, {self.props})"
	
class LeafNode(HTMLNode):
	def __init__(self, tag, value, props=None):
		super().__init__(tag, value, None, props)

	# render HTML tag
	def to_html(self):
		if self.value == None:
			raise ValueError(f"Invalid HTML: no value")
		if self.tag == None:
			return self.value
		# if self.props == None:
		# 	return f"<{self.tag}>{self.value}</{self.tag}>"
		return_string = f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
		return return_string
	
	def __repr__(self):
		return f"LeafNode({self.tag}, {self.value}, {self.props})"
	
def TextNode_to_HTMLNode(text_node):
	match(text_node.text_type):
		case(TextType.TEXT):
			return LeafNode(None, text_node.text)
		case(TextType.BOLD):
			return LeafNode("b", text_node.text)
		case(TextType.ITALIC):
			return LeafNode("i", text_node.text)
		case(TextType.CODE):
			return LeafNode("code", text_node.text)
		case(TextType.LINK):
			return LeafNode("a", text_node.text, {"href": text_node.url})
		case(TextType.IMAGE):
			return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
		case _:
			raise ValueError(f"Invalid text type: {text_node.text_type}")
		