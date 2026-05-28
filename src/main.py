from textnode import *

def main():
    testnode = TextNode("This is some anchor text", TextType.FORMATED_LINK, "https://www.boot.dev") 
    print(testnode)

if __name__ == "__main__":
    main()