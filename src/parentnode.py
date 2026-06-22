from htmlnode import *

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError
        if self.children == None:
            raise ValueError("missing children")
        html = f"<{self.tag}>"
        for c in self.children:
            html += f"{c.to_html()}"
        html += f"</{self.tag}>"
        return html
