COMMANDS = ["date", "time"]
DESCRIPTION = "System information"

import datetime

def handle(command):
	if command == "date":
		now = datetime.datetime.now()
		print("\033[33m" + now.strftime("%Y-%m-%d") + "\033[0m")

	elif command == "time":
		now = datetime.datetime.now()
		print("\033[33m" + now.strftime("%H:%M:%S") + "\033[0m")
