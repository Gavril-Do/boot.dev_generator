import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_eq2(self):
        node = TextNode("this is a test", TextType.BOLD)
        node2 = TextNode("this is also a test", TextType.BOLD)
        self.assertNotEqual(node, node2)
    def test_eq3(self):
        node = TextNode("this is a test", TextType.BOLD)
        node2 = TextNode("this is a test", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    def test_eq4(self):
        node = TextNode("this is a test", TextType.BOLD, 'https://www.boot.dev')
        node2 = TextNode("this is a test", TextType.BOLD, 'https://www.boot.dev')
        self.assertEqual(node, node2)
    def test_eq5(self):
        node = TextNode("this is a test", TextType.BOLD, 'https://www.boot.dev')
        node2 = TextNode("this is a test", TextType.BOLD, 'https://www.bootdev')
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()