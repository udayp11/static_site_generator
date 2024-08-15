import unittest

from textnode import TextNode
from split_delimiter import split_nodes_delimiter

class TestSplitDelimiter(unittest.TestCase):
    def test_split(self):
        node = TextNode("This is text with a `code block` word", "text")
        new_nodes = split_nodes_delimiter([node], "`", "code")

        self.assertEqual(new_nodes, [TextNode("This is text with a ", "text"),TextNode("code block", "code"),TextNode(" word", "text"),
])