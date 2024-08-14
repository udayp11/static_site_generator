from textnode import TextNode

def main():

    Test_node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    Test_node1 = TextNode("This is a text node", "bold", "https://www.boot.dev")
    Test_node2 = TextNode("This is a text node2", "bold", "https://www.boot.dev")
    print(Test_node) #or repr(Test_node)
    #print(Test_node==Test_node1)
    #print(Test_node==Test_node2)


main()