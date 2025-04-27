from textnode import TextNode, TextType

def main():
    node = TextNode("Anchor test", TextType.LINK, "https://www.boot.dev")
    print(node)

main()