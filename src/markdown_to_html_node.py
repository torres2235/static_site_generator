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
    