from textnode import *
import os, shutil

from markdown_blocks import *
from copystatic import *
from gen_content import *

static_path = "./static"
public_path = "./public"
path_content = "./content"
template_path = "./template.html"

def main():
	# print("deleting public directory...")
	if os.path.exists(public_path):
		shutil.rmtree(public_path)

	# print("copying static files to public directory...")
	static_to_public(static_path, public_path)

	# print("Generating page...")
	generate_pages_recursive(path_content, template_path, public_path)


main()