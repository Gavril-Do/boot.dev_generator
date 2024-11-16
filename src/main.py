from textnode import *

def main():
	textnode = TextNode('this is a test', TextType.BOLD, "https://www.boot.dev")
	print(textnode.__repr__)

main()