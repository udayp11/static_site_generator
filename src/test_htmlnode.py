import unittest

from htmlnode import HTMLNode

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
        

    

if __name__ == "__main__":
    unittest.main()

