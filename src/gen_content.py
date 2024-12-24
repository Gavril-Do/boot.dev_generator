import os
from markdown_blocks import markdown_to_html_node

def generate_page(from_path, template_path, dest_path):
	# print a message "Generating page from "from_path" to "dest_path" using "template_path"
	# print(f"Generating page from {from_path} to {dest_path} using {template_path}")
	# read markdown file at "from path" and store the contents in a variable
	with open(from_path, "r") as f:
		markd_file = f.read()
	# read template file at "template_path" and store contents in a variable
	with open(template_path, "r") as f:
		templ_file = f.read()
	# use markdown to htmlnode and .to html method to convert the markdown file to an html string
	html_node = markdown_to_html_node(markd_file)
	html_string = html_node.to_html()
	# use extract title function to grab the title of the page
	title = extract_title(markd_file)
	# replace the {{ title }} and {{ content }} placeholders in the template with the HTML and title you generated
	templ_file = templ_file.replace("{{ Title }}", title)
	templ_file = templ_file.replace("{{ Content }}", html_string)
	# write the new *full html page* to a file at dest_path be sure to create any necessary directories if they don't exist
	dest_dir_path = os.path.dirname(dest_path)
	# print(dest_dir_path)
	if dest_dir_path != "":
		os.makedirs(dest_dir_path, exist_ok=True)
	# with open(dest_path, "x+") as f:
	# 	f.write(templ_file)

def extract_title(markdown):
	lines = markdown.split("\n")
	for line in lines:
		if line.startswith("# "):
			return line[2:]
	raise ValueError("No title found")