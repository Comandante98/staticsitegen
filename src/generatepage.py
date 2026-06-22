import os
from markdown_to_html import *
from htmlnode import *
from pathlib import Path

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    source = open(from_path).read()
    template = open(template_path).read()
    node = markdown_to_html_node(source)
    html = node.to_html()
    title = extract_title(source)
    r1 = template.replace("{{ Title }}", title)
    r2 = r1.replace("{{ Content }}", html)
    r3 = r2.replace('href="/', f'href="{basepath}')
    r4 = r3.replace('src="/', f'src="{basepath}')
    d = os.path.dirname(dest_path)
    os.makedirs(d, exist_ok=True)
    open(dest_path, mode='w').write(r4)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    files = os.listdir(dir_path_content)
    for f in files:
        joined = os.path.join(dir_path_content, f)
        joined_dest = os.path.join(dest_dir_path, f)
        if os.path.isfile(joined):
            html_path = Path(joined_dest).with_suffix(".html")
            generate_page(joined, template_path, html_path, basepath)
        else:
            generate_pages_recursive(joined, template_path, joined_dest, basepath)