import unittest

from HTMLNode import HTMLNode

props = {
		"href": "https://www.google.com", 
		"target": "_blank",
	}
class TestHTMLNode(unittest.TestCase):

	def test(self):
		node = HTMLNode()
	def test1(self):
		node = HTMLNode("this is a tag", 'value', 'children', props)
		node_print = node.props_to_html()
#		print(node_print)
	def test2(self):
		node = HTMLNode("this is a tag", 'value', 'children', props)
		with self.assertRaises(NotImplementedError):
			node_print = node.to_html()



if __name__ == "__main__":
    unittest.main()