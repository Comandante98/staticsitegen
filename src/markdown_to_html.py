from markdown_to_textnode import split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnode, markdown_to_blocks
from blocktype import *
from textnode import *
from parentnode import *

def markdown_to_html_node(markdown):
    block_list = []
    blocks = markdown_to_blocks(markdown)
    for b in blocks:
        if block_to_block_type(b) == BlockType.PARAGRAPH:
            p = block_to_paragraph(b)
            block_list.append(p)
        elif block_to_block_type(b) == BlockType.HEADING:
            h = block_to_heading(b)
            block_list.append(h)
        elif block_to_block_type(b) == BlockType.QUOTE:
            q = block_to_quote(b)
            block_list.append(q)
        elif block_to_block_type(b) == BlockType.UNORDERED:
            ul = block_to_unordered(b)
            block_list.append(ul)
        elif block_to_block_type(b) == BlockType.ORDERED:
            ol = block_to_ordered(b)
            block_list.append(ol)
        else:
            c = block_to_code(b)
            block_list.append(c)
    
    return ParentNode("div", block_list)


def text_to_children(text):
    children = []
    textnode = text_to_textnode(text)
    for t in textnode:
        children.append(text_node_to_html_node(t))
    return children


def block_to_paragraph(p):
    paragraph = " ".join(p.split("\n"))
    children = text_to_children(paragraph)
    node = ParentNode("p", children)
    return node

def block_to_heading(h):
    count = 0
    for char in h:
        if char == "#":
            count += 1
        else:
            break
    text = h[count + 1:]
    children = text_to_children(text)
    node = ParentNode(f"h{count}", children)
    return node

def block_to_quote(q):
    splitted = q.split("\n")
    stripped = []
    for s in splitted:
        stripped.append(s.strip("> "))
    quotes = " ".join(stripped)
    children = text_to_children(quotes)
    node = ParentNode("blockquote", children)
    return node

def block_to_unordered(ul):
    unordered = ul.split("\n")
    li_nodes = []
    for u in unordered:
        text = u.strip("- ")
        children = text_to_children(text)
        li_nodes.append(ParentNode("li", children))
    node = ParentNode("ul", li_nodes)
    return node

def block_to_ordered(ol):
    ordered = ol.split("\n")
    li_nodes = []
    for o in ordered:   
        text = o[3:]
        children = text_to_children(text)
        li_nodes.append(ParentNode("li", children))
    node = ParentNode("ol", li_nodes)
    return node

def block_to_code(c):
    code_tag = []
    pre_tag = []
    chopped = c[4:-3]
    raw_node = TextNode(chopped, TextType.TEXT)
    child = text_node_to_html_node(raw_node)
    code_tag.append(child)
    pre_tag.append(ParentNode("code", code_tag))
    node = ParentNode("pre", pre_tag)
    return node

def extract_title(markdown):
    block_list = []
    blocks = markdown_to_blocks(markdown)
    for b in blocks:
        if block_to_block_type(b) == BlockType.HEADING and b.startswith("# "):
            return b[2:]
    raise Exception("No heading matching the criteria found")
