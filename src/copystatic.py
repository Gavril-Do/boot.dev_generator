import os, shutil

# Copy  contents of static to public
def static_to_public(source, destination):
	if not os.path.exists(source):
		raise Exception("Source directory does not exist")
	if not os.path.exists(destination):
		os.mkdir(destination)

	for filename in os.listdir(source):
		from_path = os.path.join(source, filename)
		dest_path = os.path.join(destination, filename)
		if os.path.isfile(from_path):
			shutil.copy(from_path, dest_path)
		else:
			static_to_public(from_path, dest_path)

# 	else:
# 		for filename in os.listdir("./public"):
# 			file_path = os.path.join("./public", filename)
# 			try:
# 				if os.path.isfile(file_path):
# 					os.unlink(file_path)
# 				elif os.path.isdir(file_path):
# 					shutil.rmtree(file_path)
# 			except Exception as e:
# 				return "failed to delete %s. Reason: %s" % (file_path, e)
# 	to_print.append(copy_files(path))
# 	return to_print

# def copy_files(path):
# 	copied = []
# 	items = os.listdir(path)
# 	for item in items:
# 		if item == "":
# 			copied.append("continue")
# 			continue
# 		if os.path.isfile(os.path.join(path, item)):
# 			# copied.append(os.path.join(path.replace("static", "public"), item))
# 			copied.append(shutil.copy2(os.path.join(path, item), os.path.join(path.replace("static", "public"), item)))
# 		else:
# 			if not os.path.exists(os.path.join(path.replace("static", "public"), item)):
# 				copied.append(os.mkdir(os.path.join(path.replace("static", "public"), item)))
# 				# copied.append(os.path.join(path.replace("static", "public"), item))
# 			copied.append(copy_files(os.path.join(path, item)))
# 	return copied

# path.removeprefix("/home/gavril/workspace/github.com/gavril-do/boot.dev_generator/static")
	# dir_list = os.listdir(path)
	# to_print = []
	# for each in dir_list:
	# 	if os.path.isfile(os.path.join(path, each)):
	# 		to_print.append(f"{os.pardir}/boot.dev_generator/public", os.listdir())
	# 		# to_print.append(shutil.copy(os.path.join(path, each), "/home/gavril/workspace/github.com/gavril-do/boot.dev_generator/public"))
	# 		continue
	# 	to_print.append(static_to_public(os.path.join(path, each)))
	# return to_print
	# shutil.copy2()
	# if not os.path.exists("/home/gavril/workspace/github.com/gavril-do/boot.dev_generator/static/"):
	# 	raise Exception("'Static' folder does not exist")
	# # if not os.path.exists("/home/gavril/workspace/github.com/gavril-do/boot.dev_generator/public"):
	# # 	os.mkdir("/home/gavril/workspace/github.com/gavril-do/boot.dev_generator/public")
	# return os.path.realpath("/home/gavril/workspace/github.com/gavril-do/boot.dev_generator/static/")
