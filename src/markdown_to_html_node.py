from htmlnode import HTMLNode
from textnode import TextNode, TextType
from block_markdown import (
    block_to_block_type, 
    markdown_to_blocks,
    BlockType
)
from inline_markdown import (
    split_nodes_delimiter,
    split_nodes_image,
    split_nodes_link,
    text_to_textnodes
)

def markdown_to_html_node(markdown: str) -> HTMLNode:
    blocks = markdown_to_blocks(markdown)

    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.HEADING:
            new_html_node = HTMLNode("h1", block)