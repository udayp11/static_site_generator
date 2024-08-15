import unittest

from textnode import TextNode, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
      
        self.assertEqual(node, node2)
        
    def test_eq2(self):
        node = TextNode("Hello there", "italic")
        node2 = TextNode("Hello there", "italic")
        self.assertEqual(node,node2)

    def test_not_equal(self):
        node = TextNode("Namaste", "italic")
        node2 = TextNode("Hello there", "italic")
        self.assertNotEqual(node,node2)

    def test_eq3(self):
        node = TextNode("Hello there", "italic","https://www.olympics.com")
        node2 = TextNode("Hello there", "italic","https://www.olympics.com")
        self.assertEqual(node,node2)

    def test_text_node_to_html_node(self):
        node = TextNode("Hello there", "italic","https://www.olympics.com")
        node2 = TextNode("Hello there", "italic","https://www.olympics.com")
        self.assertEqual(node,node2)

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text_node(self):
        node = TextNode("This is a text node", "text")
        html_node = text_node_to_html_node(node)
        self.assertEqual("This is a text node",html_node.value)

    def test_bold_node(self):
        node = TextNode("This is a text node", "bold")
        html_node = text_node_to_html_node(node)
        self.assertEqual("b",html_node.tag)
        self.assertEqual("This is a text node",html_node.value)
    
    def test_image(self):
        node = TextNode("This is a image", "image","https://www.tennis.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual("img",html_node.tag)
        self.assertEqual(html_node.props,{"src":"https://www.tennis.com","alt":"This is a image"})


if __name__ == "__main__":
    unittest.main()