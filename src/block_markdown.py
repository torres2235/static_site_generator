from textnode import TextNode, TextType
import re

def markdown_to_blocks(markdown: str) -> list[str]:
    blocks = markdown.split("\n\n")
    for i in range(len(blocks)):
        blocks[i] = blocks[i].removesuffix("\n").removeprefix("\n")
    return blocks