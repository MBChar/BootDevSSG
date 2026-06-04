import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_url(self):
        node = TextNode("This is a link", TextType.LINK, "http://example.com")
        self.assertEqual(node.url, "http://example.com")

    def test_not_eq(self):
        node = TextNode("this is a text node", TextType.TEXT)
        node2 = TextNode("this is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_not_eq_different_texttype(self):
        node = TextNode("this is a text node", TextType.TEXT)
        node2 = TextNode("this is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = TextNode.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

if __name__ == "__main__":
    unittest.main()