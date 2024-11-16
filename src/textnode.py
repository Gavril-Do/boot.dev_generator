from enum import Enum

class NodeType(Enum):
	NORMAL = 'normal'
	BOLD = 'bold'
	ITALIC = 'italic'
	CODE = 'code'
	LINK = 'link'
	IMAGE = 'image'

class TextNode:
	def __init__(self, text, text_type, url):
		self.text = text
		self.text_type = text_type
		self.url = url

	# returns true if *all* of the poperties of two TextNode objects are equal
	def __eq__(self, object):
		if self.repr == object.repr:
			return True
			

	# returns string representation of the TextNode object
	def __repr__(self):
		return f"TextNode({self.text}, {self.text_type.value}, {self.url})"