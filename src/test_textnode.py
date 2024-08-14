import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
      
        self.assertEqual(node, node2)
        
    def test_eq2(self):
        node3 = TextNode("Hello there", "italic")
        node4 = TextNode("Hello there", "italic")
        self.assertEqual(node3,node4)

    def test_eq3(self):
        node3 = TextNode("Hello there", "italic","https://www.olympics.com")
        node4 = TextNode("Hello there", "italic","https://www.olympics.com")
        self.assertEqual(node3,node4)


if __name__ == "__main__":
    unittest.main()