from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block: str) -> BlockType:
    if "# " in block[0:7]:
        return BlockType.HEADING
    elif "```\n" in block[0:4] and "```" in block[-3:]:
        return BlockType.CODE
    elif block[0] == ">":
        return BlockType.QUOTE
    elif block[:2] == "- ":
        return BlockType.UNORDERED_LIST
    elif block[:3] == "1. ":
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH

def markdown_to_blocks(markdown: str) -> list[str]:
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks