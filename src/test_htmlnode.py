import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node =  HTMLNode("p","hello","",{"href": "https://www.google.com", "target": "_blank",})
        node2  = HTMLNode("p","hello","",{"href": "https://www.google.com", "target": "_blank",})

        self.assertEqual(node.props_to_html(),node2.props_to_html())

    def test_failed_props(self):

        node =  HTMLNode("a","namaste","",{"href": "https://www.olympics.com", "target": "_blank",})
        node2  = HTMLNode("p","hello","",{"href": "https://www.google.com", "target": "_blank",})

        self.assertNotEqual(node.props_to_html(),node2.props_to_html())

    def test_repr(self):

        node =  HTMLNode("p","hello","",{"href": "https://www.google.com", "target": "_blank",})
        node2  = HTMLNode("p","hello","",{"href": "https://www.google.com", "target": "_blank",})

        self.assertEqual(repr(node),repr(node2))
    
    def test_to_html(self):

        node =  HTMLNode("p","hello","",{"href": "https://www.google.com", "target": "_blank",})
        with self.assertRaises(NotImplementedError):node.to_html()

    def test_to_leafnode(self):

        node =  LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(),node2.to_html())

    def test_to_html_no_children(self):

        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")


    def test_to_html_no_tag(self):

        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")


    def test_ParentNode(self):

        node = ParentNode("p",
            [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
              ],
            )

        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )



    

if __name__ == "__main__":
    unittest.main()

