from textnode import *
import os, shutil

from copystatic import *

static_path = "./static"
public_path = "./public"


def main():
	print("deleting public directory...")
	if os.path.exists(public_path):
		shutil.rmtree(public_path)

	print("copying static files to public directory...")
	static_to_public(static_path, public_path)


main()