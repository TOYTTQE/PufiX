COMMANDS = ["date", "time", "version"]
DESCRIPTION = "System information"

import datetime

VERSION = "1.0.0"

def handle(command):
	if command == "date":
		now = datetime.datetime.now()
		print("\033[33m" + now.strftime("%Y-%m-%d") + "\033[0m")

	elif command == "time":
		now = datetime.datetime.now()
		print("\033[33m" + now.strftime("%H:%M:%S") + "\033[0m")

	elif command == "version":
		print("\033[1mPufiX \033[36;1mv" + VERSION + "\033[0m")
		print("\033[90mInspired by TERMUX ⟩_\033[0m")
