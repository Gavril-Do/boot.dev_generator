import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a test_eq node", TextType.BOLD)
        node2 = TextNode("This is a test_eq node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_eq2(self):
        node = TextNode("this is test_eq2", TextType.BOLD)
        node2 = TextNode("this is also test_eq2", TextType.BOLD)
        self.assertNotEqual(node, node2)
    def test_eq3(self):
        node = TextNode("this is test_eq3", TextType.BOLD)
        node2 = TextNode("this is test_eq3", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    def test_eq4(self):
        node = TextNode("this is test_eq4", TextType.BOLD, 'https://www.boot.dev')
        node2 = TextNode("this is test_eq4", TextType.BOLD, 'https://www.boot.dev')
        self.assertEqual(node, node2)
    def test_repr(self):
        node = TextNode("This is a test_repr node", TextType.BOLD, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a test_repr node, BOLD, https://www.boot.dev)", repr(node)
        )

if __name__ == "__main__":
    unittest.main()