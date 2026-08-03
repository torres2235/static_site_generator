from textnode import TextNode, TextType
import re


def split_nodes_delimiter(
    old_nodes: list[TextNode], delimiter: str, text_type: TextType
) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text : str) -> list([tuple[str,str]]):
    image = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return image

def extract_markdown_links(text : str) -> list([tuple[str,str]]):
    link = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return link


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        images = extract_markdown_images(old_node.text)
        split_nodes = []
        section = old_node.text
        for image in images:
            split_section = section.split(f"![{image[0]}]({image[1]})", 1)
            if len(split_section) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if split_section[0] != "":
                split_nodes.append(TextNode(split_section[0], TextType.TEXT))
            split_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
            section = split_section[1]
        if section != "":
            split_nodes.append(TextNode(section, TextType.TEXT))
        new_nodes.extend(split_nodes)
    return new_nodes


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        links = extract_markdown_links(old_node.text)
        split_nodes = []
        section = old_node.text
        for link in links:
            split_section = section.split(f"[{link[0]}]({link[1]})", 1)
            if len(split_section) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if split_section[0] != "":
                split_nodes.append(TextNode(split_section[0], TextType.TEXT))
            split_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            section = split_section[1]
        if section != "":
            split_nodes.append(TextNode(section, TextType.TEXT))
        new_nodes.extend(split_nodes)
    return new_nodes


def text_to_textnodes(text):
    new_textnode = TextNode(text, TextType.TEXT)
    split_bold = split_nodes_delimiter([new_textnode], "**", TextType.BOLD)
    split_italic = split_nodes_delimiter(split_bold, "_", TextType.ITALIC)
    split_code = split_nodes_delimiter(split_italic, "`", TextType.CODE)
    split_images = split_nodes_image(split_code)
    split_links = split_nodes_link(split_images)

    return split_links