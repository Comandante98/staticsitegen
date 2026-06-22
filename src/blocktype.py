from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED = "unordered_list"
    ORDERED = "ordered_list"

def block_to_block_type(markdown):
    if "# " in markdown[0:7]:
        return BlockType.HEADING
    if markdown.startswith("```\n") and markdown.endswith("```"):
        return BlockType.CODE
    quote = True
    for qline in markdown.splitlines():
        if qline.startswith(">") == False:
            quote = False
            break
    if quote:
        return BlockType.QUOTE
    unordered = True
    for uline in markdown.splitlines():
        if uline.startswith("- ") == False:
            unordered = False
            break
    if unordered:
        return BlockType.UNORDERED
    c = 1
    ordered = True
    for oline in markdown.splitlines():
        if oline.startswith(f"{c}. ") == False:
            ordered = False
            break
        c += 1
    if ordered:
        return BlockType.ORDERED
    return BlockType.PARAGRAPH