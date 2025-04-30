import unittest

from textnode import TextNode, TextType,text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
      
        self.assertEqual(node, node2)
        
    def test_eq2(self):
        node = TextNode("Hello there", TextType.ITALIC)
        node2 = TextNode("Hello there", TextType.ITALIC)
        self.assertEqual(node,node2)

    def test_not_equal(self):
        node = TextNode("Namaste", TextType.ITALIC)
        node2 = TextNode("Hello there", TextType.ITALIC)
        self.assertNotEqual(node,node2)

    def test_eq3(self):
        node = TextNode("Hello there", TextType.ITALIC,"https://www.olympics.com")
        node2 = TextNode("Hello there",TextType.ITALIC,"https://www.olympics.com")
        self.assertEqual(node,node2)

    def test_text_node_to_html_node(self):
        node = TextNode("Hello there", TextType.ITALIC,"https://www.olympics.com")
        node2 = TextNode("Hello there", TextType.ITALIC,"https://www.olympics.com")
        self.assertEqual(node,node2)

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text_node(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag,None)
        self.assertEqual("This is a text node",html_node.value)

    def test_bold_node(self):
        node = TextNode("This is a text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual("b",html_node.tag)
        self.assertEqual("This is a text node",html_node.value)
    
    def test_image(self):
        node = TextNode("This is a image", TextType.IMAGE,"https://www.tennis.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual("img",html_node.tag)
        self.assertEqual(html_node.props,{"src":"https://www.tennis.com","alt":"This is a image"})
        


if __name__ == "__main__":
    unittest.main()