

class HTMLNode:
	def __init__(self, tag=None, value=None, children=None, props=None):
		self.tag = tag
		self.value = value
		self.children = children
		self.props = props

	def to_html(self):
		raise NotImplementedError
	
	# Return string that represents the HTML attributes of the node
	def props_to_html(self):
		props_dict = self.props.copy()
		string = ""
		for each in props_dict:
			if string == "":
				string = f' {each}="{props_dict[each]}"'
			else:
				string = string + f' {each}="{props_dict[each]}"'
		return string
	

	# print HTMLNode object to see it's tag, value, children, props for debug
	def __repr__(self):
		return f"HTMLNode(tag='{self.tag}', value='{self.value}', children='{self.children}', props='{self.props})'"
	
class LeafNode(HTMLNode):
	def __init__(self, tag, value, props=None):
		super().__init__(tag, value, None, props)

	# render HTML tag
	def to_html(self):
		tag_convert = convert_tag(self.tag)
		if self.value == None:
			raise ValueError
		if self.tag == None:
			return f"{self.value}"
		match(self.tag):
			case("p"):
				return f"{tag_convert[0]}{self.value}{tag_convert[1]}"
			case("a"):
				return f'<{self.tag} {list(self.props)[0]}="{self.props[list(self.props)[0]]}">{self.value}{tag_convert[1]}'

def convert_tag(tag, value=None):
	if type(tag) != str:
		raise ValueError
	return f"<{tag}>", f"</{tag}>"