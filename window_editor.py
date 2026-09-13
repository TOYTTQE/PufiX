COMMANDS = ["create file", "delete file", "list files", "edit", "read"]
DESCRIPTION = "Window editor — text editor + file operations"

import os

def handle(command):

	# create file "name"
	if command.startswith("create file "):
		file_name = command[12:].strip().strip('"')
		if not file_name:
			print("\033[31m\033[1m[EDITOR] Error: NoFileName\033[0m")
			return
		try:
			with open(file_name, "x") as f:
				pass
			print("\033[33;1m[EDITOR] Created: " + file_name + "\033[0m")
		except FileExistsError:
			print("\033[31m\033[1m[EDITOR] Error: FileExists\033[0m")

	# delete file "name"
	elif command.startswith("delete file "):
		file_name = command[12:].strip().strip('"')
		if not file_name:
			print("\033[31m\033[1m[EDITOR] Error: NoFileName\033[0m")
			return
		try:
			os.remove(file_name)
			print("\033[33;1m[EDITOR] Deleted: " + file_name + "\033[0m")
		except FileNotFoundError:
			print("\033[31m\033[1m[EDITOR] Error: FileNotFound\033[0m")

	# list files
	elif command == "list files":
		files = [f for f in os.listdir(".") if os.path.isfile(f)]
		if not files:
			print("\033[33m[EDITOR] No files\033[0m")
		else:
			print("\033[33;1m[EDITOR] Files:\033[0m")
			for f in files:
				print("  \033[33m" + f + "\033[0m")

	# read <file>
	elif command.startswith("read "):
		file_name = command[5:].strip().strip('"')
		if not file_name:
			print("\033[31m\033[1m[EDITOR] Error: NoFileName\033[0m")
			return
		try:
			with open(file_name, "r") as f:
				content = f.read()
			if content:
				print(content)
			else:
				print("\033[33m[EDITOR] File is empty\033[0m")
		except FileNotFoundError:
			print("\033[31m\033[1m[EDITOR] Error: FileNotFound\033[0m")

	# edit <file>
	elif command.startswith("edit "):
		file_name = command[5:].strip().strip('"')
		if not file_name:
			print("\033[31m\033[1m[EDITOR] Error: NoFileName\033[0m")
			return

		lines = []
		try:
			with open(file_name, "r") as f:
				content = f.read()
			if content:
				lines = content.split("\n")
				print("\033[33m[EDITOR] Loaded: " + file_name + " (" + str(len(lines)) + " lines)\033[0m")
			else:
				print("\033[33m[EDITOR] Empty file: " + file_name + "\033[0m")
		except FileNotFoundError:
			print("\033[33m[EDITOR] New file: " + file_name + "\033[0m")

		print("\033[1m[EDITOR] Commands:\033[0m")
		print("  \033[36m:w \033[0m — save")
		print("  \033[36m:q \033[0m — quit (no save)")
		print("  \033[36m:wq\033[0m — save & quit")
		print("  \033[36m:x \033[0m — delete last line")
		print("\033[90m" + "─" * 55 + "\033[0m")

		while True:
			try:
				line = input("\033[90m> \033[0m")
			except KeyboardInterrupt:
				print("\n\033[33m[EDITOR] Cancelled (no save)\033[0m")
				return

			if line == ":q":
				print("\033[33m[EDITOR] Closed (no save)\033[0m")
				return
			elif line == ":w":
				with open(file_name, "w") as f:
					f.write("\n".join(lines))
				print("\033[32m[EDITOR] Saved: " + file_name + " (" + str(len(lines)) + " lines)\033[0m")
			elif line == ":wq":
				with open(file_name, "w") as f:
					f.write("\n".join(lines))
				print("\033[32m[EDITOR] Saved & closed: " + file_name + " (" + str(len(lines)) + " lines)\033[0m")
				return
			elif line == ":x":
				if lines:
					lines.pop()
					print("\033[33m[EDITOR] Removed last line\033[0m")
				else:
					print("\033[31m\033[1m[EDITOR] No lines to remove\033[0m")
			else:
				lines.append(line)
