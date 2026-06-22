from textnode import *
from copystatic import *
from generatepage import *

def main():
    basepath = sys.argv
    if len(basepath) == 1:
        basepath = "/"
    else:
        basepath = sys.argv[1]
    copy("./static", "./docs", True)
    generate_pages_recursive("./content", "template.html", "./docs", basepath)

if __name__ == "__main__":
    main()