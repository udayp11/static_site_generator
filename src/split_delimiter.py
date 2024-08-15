from textnode import TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):

    list_of_leafnode = []
    list_delimiter = ["*","**","`"]
    
    list_of_leafnode = []

    for node in old_nodes:
        if node.text_type != "text":
            list_of_leafnode.append(node)
        elif delimiter not in list_delimiter:
            raise Exception("matching delimiter not found")
        else:
            string_node = node.text.split(delimiter)
            i = 0
            for str in string_node:
                if str == "":
                    i = 1
                else:
                    if i == 0:
                        list_of_leafnode.append(TextNode(str, node.text_type))
                        i = 1
                    else:
                        list_of_leafnode.append(TextNode(str, text_type))
                        i = 0

    return list_of_leafnode

