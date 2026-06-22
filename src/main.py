from textnode import *
from copystatic import *
from generatepage import *

def main():
    copy("./static", "./public", True)
    generate_pages_recursive("content/", "template.html", "public")

if __name__ == "__main__":
    main()