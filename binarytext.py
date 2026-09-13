COMMANDS = ["to-binary", "from-binary"]
DESCRIPTION = "Text to binary converter (and back)"

def handle(command):
	parts = command.split(maxsplit=1)
	cmd = parts[0]
	arg = parts[1] if len(parts) > 1 else ""

	if not arg:
		print("\033[31m\033[1mError: EmptyText\033[0m")
		return

	# текст → бинарный (UTF-8)
	if cmd == "to-binary":
		result = []
		for byte in arg.encode("utf-8"):
			result.append(format(byte, "08b"))
		print("\033[33m" + " ".join(result) + "\033[0m")

	# бинарный → текст (UTF-8)
	elif cmd == "from-binary":
		clean = arg.replace(" ", "")
		if len(clean) % 8 != 0:
			print("\033[31m\033[1mError: InvalidBinary (length % 8 != 0)\033[0m")
			return
		try:
			byte_list = []
			for i in range(0, len(clean), 8):
				byte = clean[i:i+8]
				if not all(c in "01" for c in byte):
					print("\033[31m\033[1mError: InvalidBinary (only 0 and 1)\033[0m")
					return
				byte_list.append(int(byte, 2))
			result = bytes(byte_list).decode("utf-8")
			print("\033[33m" + result + "\033[0m")
		except Exception as e:
			print("\033[31m\033[1mError: " + str(e) + "\033[0m")
