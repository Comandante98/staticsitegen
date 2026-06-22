import unittest
from blocktype import *

class TestBlockType(unittest.TestCase):
    def test_heading(self):
        markdown = "###### this is a heading"
        blocktype = block_to_block_type(markdown)
        self.assertEqual(blocktype, BlockType.HEADING)
    
    def test_code(self):
        markdown = """```

this is some random code

more code blablabla
```"""
        blocktype = block_to_block_type(markdown)
        self.assertEqual(blocktype, BlockType.CODE)

    def test_quote(self):
        markdown = """>Hey im Dante
> this is Gemma
>this is Jack
> and this is Jhonny"""
        blocktype = block_to_block_type(markdown)
        self.assertEqual(blocktype, BlockType.QUOTE)
    
    def test_unordered(self):
        markdown = """- Banana
- Apple
- Orange
- Mango"""
        blocktype = block_to_block_type(markdown)
        self.assertEqual(blocktype, BlockType.UNORDERED)
    
    def test_ordered(self):
        markdown = """1. Argentina
2. Francia
3. Croacia
4. Marruecos"""
        blocktype = block_to_block_type(markdown)
        self.assertEqual(blocktype, BlockType.ORDERED)

    def test_paragraph(self):
        markdown = "This is just a paragraph, LMAO"
        blocktype = block_to_block_type(markdown)
        self.assertEqual(blocktype, BlockType.PARAGRAPH)



if __name__ == "__main__":
    unittest.main()