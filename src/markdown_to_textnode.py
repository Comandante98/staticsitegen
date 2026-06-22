from textnode import *
from regex import *

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for n in old_nodes:
        if n.text_type != TextType.TEXT or n.text.count(delimiter) == 0:
            new_nodes.append(n)
            continue
        if n.text.count(delimiter) % 2 != 0:
            raise Exception("missing a delimiter")
        splited_text = n.text.split(delimiter)
        for i, s in enumerate(splited_text):
            if s != "":
                if i % 2 == 0:
                    new_nodes.append(TextNode(s, TextType.TEXT))
                else:
                    new_nodes.append(TextNode(s, text_type))
    return new_nodes

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for n in old_nodes:
        regex = extract_markdown_images(n.text)
        if regex == []:
            new_nodes.append(n)
            continue
        pre_split = n.text
        for r in regex:
            splited_text = pre_split.split(f"![{r[0]}]({r[1]})", 1)
            if splited_text[0] == "":
                new_nodes.append(TextNode(r[0], TextType.IMAGE, r[1]))
            else:
                new_nodes.append(TextNode(splited_text[0], TextType.TEXT))
                new_nodes.append(TextNode(r[0], TextType.IMAGE, r[1]))
            pre_split = splited_text[-1]
        if len(pre_split) != 0:
            new_nodes.append(TextNode(pre_split, TextType.TEXT))
    return new_nodes



def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for n in old_nodes:
        regex = extract_markdown_links(n.text)
        if regex == []:
            new_nodes.append(n)
            continue
        pre_split = n.text
        for r in regex:
            splited_text = pre_split.split(f"[{r[0]}]({r[1]})", 1)
            if splited_text[0] == "":
                new_nodes.append(TextNode(r[0], TextType.LINK, r[1]))
            else:
                new_nodes.append(TextNode(splited_text[0], TextType.TEXT))
                new_nodes.append(TextNode(r[0], TextType.LINK, r[1]))
            pre_split = splited_text[-1]
        if len(pre_split) != 0:
            new_nodes.append(TextNode(pre_split, TextType.TEXT))
    return new_nodes

def text_to_textnode(text):
    node = TextNode(text, TextType.TEXT)
    node_list = []
    node_list.append(node)
    text_with_bold = split_nodes_delimiter(node_list, "**", TextType.BOLD)
    text_with_italic = split_nodes_delimiter(text_with_bold, "_", TextType.ITALIC)
    text_with_code = split_nodes_delimiter(text_with_italic, "`", TextType.CODE)
    text_with_images = split_nodes_image(text_with_code)
    final_textnode = split_nodes_link(text_with_images)
    return final_textnode

def markdown_to_blocks(markdown):
    blocks = []
    splited = markdown.split("\n\n")
    for b in splited:
        striped_b = b.strip()
        if b != "":
            blocks.append(striped_b)
    return blocks