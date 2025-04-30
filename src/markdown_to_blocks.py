from enum import Enum

from split_delimiter import text_to_textnodes
from htmlnode import ParentNode
from textnode import TextType,TextNode,text_node_to_html_node


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    updated_blocks = []
    for block in blocks:
        if len(block.strip()) != 0:
            updated_blocks.append(block.strip())
        

    return updated_blocks

def block_to_block_type(block):
    lines = block.split("\n")
    if lines[0].startswith(("# ","## ","### ","#### ","##### ","###### ")):
        return BlockType.HEADING
    if lines[0].startswith("```") and lines[len(lines)-1].endswith("```"):
        return BlockType.CODE
    if lines[0].startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if lines[0].startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.ULIST

    if lines[0].startswith("1. "):
        
        for i in range(0, len(lines)):
            if not lines[i].startswith(f"{i+1}. "):
                return BlockType.PARAGRAPH
        return BlockType.OLIST
    return BlockType.PARAGRAPH

def markdown_to_html_node(markdown):

    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        children.append(block_to_html_node(block))
    

    return ParentNode("div",children,None)

def block_to_html_node(block):
    block_type = block_to_block_type(block)

    if block_type == BlockType.QUOTE:
        return quote_to_html_node(block)

    if block_type == BlockType.PARAGRAPH:
        return paragraph_to_html_node(block)

    if block_type == BlockType.HEADING:
        return heading_to_html_node(block)

    if block_type == BlockType.OLIST:
        return olist_to_html_node(block)

    if block_type == BlockType.ULIST:
        return ulist_to_html_node(block)

    if block_type == BlockType.CODE:
        return code_to_html_node(block)
    raise ValueError("Invalid block type")


def text_to_children(text):

    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children

def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p",children)

def heading_to_html_node(block):
    count = 0

    for char in block:
        if char == "#":
            count += 1
        else:
            break
    new_block = block[count +1:].strip()

    children = text_to_children(new_block)
    return ParentNode(f"h{count}",children)

def olist_to_html_node(block):
    lines = block.split("\n")
    olist_html = []
    for line in lines:
        text = line[3:]
        children = text_to_children(text)
        olist_html.append(ParentNode("li", children))
    return ParentNode("ol", olist_html)

def ulist_to_html_node(block):
    lines = block.split("\n")
    ulist_html = []
    for line in lines:
        text = line[2:]
        children = text_to_children(text)
        ulist_html.append(ParentNode("li", children))
    return ParentNode("ul", ulist_html)

def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("invalid code block")
    text = block[4:-3]
    raw_text_node = TextNode(text, TextType.TEXT)
    child = text_node_to_html_node(raw_text_node)
    code = ParentNode("code", [child])
    return ParentNode("pre", [code])


def quote_to_html_node(block):
    lines = block.split("\n")
    updated_lines = []
    for line in lines:
        if line.startswith(">"):
            trimmed = line[1:]
            trimmed = trimmed.lstrip()
            updated_lines.append(trimmed)
        else:
            updated_lines.append(line)
    final_lines = " ".join(updated_lines)

    node_of_quote = ParentNode("blockquote",text_to_children(final_lines))
    return node_of_quote



