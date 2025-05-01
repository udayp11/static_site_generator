import re

from textnode import (TextNode,TextType)

def text_to_textnodes(text):
    nodes = [TextNode(text,TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes,"**",TextType.BOLD)
    nodes = split_nodes_delimiter(nodes,"_",TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes,"`",TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
   
    return nodes

def split_nodes_delimiter(old_nodes, delimiter, text_type):

    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        split_nodes = []

        string_nodes = node.text.split(delimiter)

        if len(string_nodes) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(string_nodes)):
            if string_nodes[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(string_nodes[i],TextType.TEXT))
            else :
                split_nodes.append(TextNode(string_nodes[i],text_type))
        new_nodes.extend(split_nodes)

    return new_nodes

def split_nodes_image(old_nodes):

    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        content = node.text
        string_images = extract_markdown_images(content)

        if len(string_images) == 0:
            new_nodes.append(node)
            continue

        for image in string_images:
            split_parts = content.split(f'![{image[0]}]({image[1]})',1)
            if split_parts[0] != "":
                new_nodes.append(
                    TextNode(split_parts[0],TextType.TEXT)

                )

            new_nodes.append(
                TextNode(
                    image[0],
                    TextType.IMAGE,
                    image[1]
                )
            )
            content = split_parts[1]
        if content != "":
            new_nodes.append(TextNode(content,TextType.TEXT))

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)

            continue

        content = node.text

        string_links = extract_markdown_links(content)

        for link in string_links:
            split_parts = content.split(f"[{link[0]}]({link[1]})",1)
            if split_parts[0] != "":
                new_nodes.append(TextNode(split_parts[0],TextType.TEXT))

            new_nodes.append(TextNode(
                    link[0],
                    TextType.LINK,
                    link[1]
                ))
            content = split_parts[1]
            
        if content != "":
            new_nodes.append(TextNode(content,TextType.TEXT))
    return new_nodes

        

def extract_markdown_images(text):
    
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)",text)

    return matches

def extract_markdown_links(text):

    matches = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)",text)

    return matches






