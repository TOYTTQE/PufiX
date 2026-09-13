COMMANDS = ["genpass", "genpin", "genpass-strong"]
DESCRIPTION = "Password generator"

import random
import string

def handle(command):
	parts = command.split()
	cmd = parts[0]
	length = None

	if len(parts) > 1:
		try:
			length = int(parts[1])
		except ValueError:
			print("\033[31m\033[1mError: NoNumber\033[0m")
			return

	if cmd == "genpass":
		if length is None:
			length = 12
		if length < 1:
			print("\033[31m\033[1mError: Length must be > 0\033[0m")
			return
		chars = string.ascii_letters + string.digits
		password = "".join(random.choice(chars) for _ in range(length))
		print("\033[33;1m" + password + "\033[0m")

	elif cmd == "genpin":
		if length is None:
			length = 4
		if length < 1:
			print("\033[31m\033[1mError: Length must be > 0\033[0m")
			return
		pin = "".join(random.choice(string.digits) for _ in range(length))
		print("\033[33;1m" + pin + "\033[0m")

	elif cmd == "genpass-strong":
		if length is None:
			length = 16
		if length < 1:
			print("\033[31m\033[1mError: Length must be > 0\033[0m")
			return
		chars = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"
		password = "".join(random.choice(chars) for _ in range(length))
		print("\033[33;1m" + password + "\033[0m")
