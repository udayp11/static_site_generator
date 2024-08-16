from htmlnode import HTMLNode

from split_delimiter import extract_markdown_images,extract_markdown_links

from textnode import (TextNode, text_type_text,
                        text_type_bold,
                        text_type_italic,
                        text_type_code)
def main():

    Test_node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    Test_node1 = TextNode("This is a text node", "bold", "https://www.boot.dev")
    Test_node2 = TextNode("This is a text node2", "bold", "https://www.boot.dev")

    Test_htmlnode = HTMLNode("p","hello","",{"href": "https://www.google.com", "target": "_blank",})
    print(Test_node)
    print(Test_htmlnode)
    
    
# [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
     #or repr(Test_node)
    #print(Test_node==Test_node1)
    #print(Test_node==Test_node2)


main()