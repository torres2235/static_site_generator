from textnode import TextNode, TextType


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

# def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
#     new_nodes = []
#     for node in old_nodes:
#         if node.text_type is not TextType.TEXT:
#             new_nodes.append(node)
#             continue

#         if delimiter not in node.text:
#             raise Exception("delimiter not found")

#         split_text = node.text.split(delimiter)
#         if len(split_text) != 3:
#             raise Exception("no ending delimiter")

#         new_nodes.append(TextNode(split_text[0], TextType.TEXT))
#         new_nodes.append(TextNode(split_text[1], text_type))
#         new_nodes.append(TextNode(split_text[2], TextType.TEXT))

#         return new_nodes
