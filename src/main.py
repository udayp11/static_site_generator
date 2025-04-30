from htmlnode import HTMLNode

from split_delimiter import (split_nodes_delimiter,
                        extract_markdown_images,
                        extract_markdown_links,
                        split_nodes_image,
                        split_nodes_link,
                        text_to_textnodes)
from markdown_to_blocks import (markdown_to_blocks,markdown_to_html_node)

from textnode import (TextNode, TextType)
def main():

    Test_node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    Test_node1 = TextNode("This is a text node", "bold", "https://www.boot.dev")
    Test_node2 = TextNode("This is a text node2", "bold", "https://www.boot.dev")

    #Test_htmlnode = HTMLNode("p","hello","",{"href": "https://www.google.com", "target": "_blank",})
    #text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    text = """
                # This is a heading
    
                This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

                - This is the first list item in a list block
                - This is a list item
                                    """
    print(markdown_to_html_node(text))
    
    
# [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
     #or repr(Test_node)
    #print(Test_node==Test_node1)
    #print(Test_node==Test_node2)

main()