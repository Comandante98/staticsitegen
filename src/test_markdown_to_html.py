import unittest
from markdown_to_html import *

class TestMarkdownToHTML(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_headings(self):
        md = "###### this is a heading"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h6>this is a heading</h6></div>",
        )
    
    def test_quotes(self):
        md = """> Hey im Dante
> this is Gemma
> this is Jack
> and this is Jhonny"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>Hey im Dante this is Gemma this is Jack and this is Jhonny</blockquote></div>",
        )

    def test_unordered_lists(self):
        md = """- Banana
- Apple
- Orange
- Mango"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Banana</li><li>Apple</li><li>Orange</li><li>Mango</li></ul></div>",
        )

    def test_unordered_lists(self):
        md = """1. Argentina
2. Francia
3. Croacia
4. Marruecos"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>Argentina</li><li>Francia</li><li>Croacia</li><li>Marruecos</li></ol></div>",
        )

    def test_codes(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )
    def test_title(self):
        md = "# this is a heading"
        title = extract_title(md)
        self.assertEqual(title, "this is a heading")

    def test_title_error(self):
        with self.assertRaises(Exception):
            md = "### this is a heading"
            title = extract_title(md)


if __name__ == "__main__":
    unittest.main()