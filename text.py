COMMANDS = ["upper", "lower", "reverse", "count", "replace"]
DESCRIPTION = "Text manipulation"

def handle(command):
	parts = command.split(maxsplit=1)
	cmd = parts[0]
	arg = parts[1] if len(parts) > 1 else ""

	if not arg:
		print("\033[31m\033[1mError: EmptyText\033[0m")
		return

	if cmd == "upper":
		print("\033[33m" + arg.upper() + "\033[0m")

	elif cmd == "lower":
		print("\033[33m" + arg.lower() + "\033[0m")

	elif cmd == "reverse":
		print("\033[33m" + arg[::-1] + "\033[0m")

	elif cmd == "count":
		print("\033[33m" + str(len(arg)) + " chars\033[0m")

	elif cmd == "replace":
		sub = command.split(maxsplit=3)
		if len(sub) < 4:
			print("\033[31m\033[1mUsage: replace <old> <new> <text>\033[0m")
			return
		old = sub[1]
		new = sub[2]
		text = sub[3]
		print("\033[33m" + text.replace(old, new) + "\033[0m")
