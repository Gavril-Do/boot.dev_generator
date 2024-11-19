from HTMLNode import *

tag1 = "b"
tag2 = "i"
tag3 = "p"
tag4 = "a"


value1 = "This is a value"
value2 = "this is another value"
value3 = "this is a third value"

props1 = {
	"href": "https://www.google.com", 
	"target": "_blank",
}
props2 = {
	"href": "https://www.boot.dev",
}
props3 = {
	"target": "_blank",
}
props4 = {
	"rel": "stylesheet",
	"href": "styles.css"
}

title = LeafNode("title", "Why Frontend Development Sucks")
h1_1 = LeafNode("h1", "Front-end Development is the Worst")
para_1 = LeafNode("p", "Look, front-end development is for script kiddies and soydevs who can't handle the real programming. I mean,\nit's just a bunch of divs and spans, right? And css??? It's like, 'Oh, I want this to be red, but not thaaaaat\nred.' What a joke.")
para_2 = LeafNode("p", "Real programmers code, not silly markup languages. They code on Arch Linux, not Mac OS, and certainly not\nWindows. They use Vim, not VS Code. They use C, not HTML. Come to the\n<a href='https://www.boot.dev'>backend</a>, where the real programming\nhappens.")

Head_1 = ParentNode("head", title, props4)
body_1 = ParentNode("body", (h1_1, para_1, para_2))
html_1 = ParentNode("html", (Head_1, body_1))

children2 = [
	ParentNode(
    	"p",
    	[
     		LeafNode("b", "Bold text", props3),
      		LeafNode(None, "Normal text"),
			LeafNode("i", "italic text"),
			LeafNode(None, "Normal text"),
    	],
	),
]

