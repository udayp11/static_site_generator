from textnode import TextNode

from htmlnode import HTMLNode


def main():

    Test_node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    Test_node1 = TextNode("This is a text node", "bold", "https://www.boot.dev")
    Test_node2 = TextNode("This is a text node2", "bold", "https://www.boot.dev")

    Test_htmlnode = HTMLNode("p","hello","",{"href": "https://www.google.com", "target": "_blank",})
    print(Test_node)
    print(Test_htmlnode)
     #or repr(Test_node)
    #print(Test_node==Test_node1)
    #print(Test_node==Test_node2)


main()