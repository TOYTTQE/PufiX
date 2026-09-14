import random
import os
import importlib.util

installed_packages = {}

def install_package(pkg_name):
	pkg_file = pkg_name.replace("-", "_") + ".py"
	if not os.path.exists(pkg_file):
		return False
	spec = importlib.util.spec_from_file_location(pkg_name, pkg_file)
	module = importlib.util.module_from_spec(spec)
	spec.loader.exec_module(module)
	installed_packages[pkg_name] = module
	return True

for pkg in ["face", "window_editor", "sys", "text", "crpassword", "binarytext", "rgbhsvhex", "morse", "qlist", "qlist_tablesizes", "esound", "emerald"]:
	install_package(pkg)

print("  " * 15 + "\033[36m\033[1mPufiX\033[0m")

try:
	with open("profile.txt", "r") as f:
		lines = f.read().split("\n")
		name = lines[0]
		tg = lines[1]
	print("Welcome back, \033[33m" + name + "\033[0m!")
except (FileNotFoundError, IndexError):
	name = input(">>> Your name: ")
	tg = input(">>> You in \033[36;1mTELEGRAM\033[0m: @")
	with open("profile.txt", "w") as f:
		f.write(name + "\n" + tg)

notebook_open = False
notebook_lines = []
history = []
while True:
	command = input("> ")
	history.append(command)
	
	if command == "py.base":
		type = input("type: print / input\n> ")
		if type == "print" or type == "input":
			typetext = input("Write the text for " + type + "\n> ")
			if type == "print":
				print(typetext)
			elif type == "input":
				input(typetext)
	elif command == "calc.base":
		try:
			a = int(input("a = "))
			operator = input("operator: + - / *\n> ")
			b = int(input("b = "))
		except ValueError:
			print("\033[31m\033[1mError: NoNumber\033[0m")
			continue
		if operator == "+":
			print(">>>", a + b)
		elif operator == "-":
			print(">>>", a - b)
		elif operator == "/":
			if b == 0:	
				print("\033[31m\033[1mError: Division by Zero\033[0m")
				continue
			print(">>>", a / b)
		elif operator == "*":
			print(">>>", a * b)
		else:
			print("\033[31m\033[1mUnknown Operator: <Your: \"" + operator + "\">\033[0m")
			continue
	elif command == "me":
		if name == "":
			print("\033[31m\033[1mError: Empty / or / \033[7mHidden Name\033[0m")
		else:
			print("You: \033[33m" + name + "\033[0m")
	elif command == "." or command == "help":
		print("[ me | tg | set.tg | edit.name | py.base | calc.base | notebook | e.notebook | find.notebook | undertext | basetext | red.sys | incognito | m text | set.title | line | bigline | sbigline | xline | aline | gline | fline | pline | guess-the-number | rock-paper-scissors | dice | coin-flip | timer | history | history.clear | my.profile | inspired ]")
	elif command == "undertext" or command == "ut":
		print("\033[7m")
		continue
	elif command == "basetext" or command == "bt":
		print("\033[0m")
		continue	
	elif command == "red.sys" or command == "r.s":
		input("\033[31m> ")
		continue
	elif command == "edit.name" or command == "e.n":
		name = input(">>> Your name: ")
		with open("profile.txt", "w") as f:
			f.write(name + "\n" + tg)
	elif command == "clear":
		print("\n" * 100000 + "\033[H\033[J")
		print("  " * 15 + "\033[36m\033[1mPufiX\033[0m")
		continue
	elif command == "set.title":
		title = input("Title: ")
		print(" " * 30 + "\033[1m" + title + "\033[0m")
	elif command == "line":
		try:	
			size = int(input("Size: "))
		except ValueError:
			print("\033[31m\033[1mError: NoNumber\033[0m")
			continue
		if size < 1:
			print(f"\033[31m\033[1mError: <Size: {size}>\033[0m")
			continue
		print("-" * size)
	elif command == "bigline":
		try:	
			size = int(input("Size: "))
		except ValueError:
			print("\033[31m\033[1mError: NoNumber\033[0m")
			continue
		if size < 1:
			print(f"\033[31m\033[1mError: <Size: {size}>\033[0m")
			continue
		print("=" * size)
	elif command == "guess-the-number" or command == "gtn":
		try:
			size = int(input("Size: "))
		except ValueError:
			print("\033[31m\033[1mError: NoNumber\033[0m")
			continue
		label = "[ 1 - 10 ]"
		left = (size - len(label)) // 2
		right = size - len(label) - left
		print("=" * left + label + "=" * right)
		number = random.randint(1, 10)
		tries = 1
		while True:
			try:
				person_number = int(input("[guess] > "))
			except ValueError:
				print("\033[31m\033[1mError: NoNumber\033[0m")
				continue
			if person_number == number:
				print(f"\033[32m\033[1m[ ✓ | tries: {tries}]\033[0m")
				print("=" * size)
				break
			elif person_number == 0:
				print("=" * size)
				break
			else:
				if number < person_number:
					print("\033[31m\033[1mx \033[33m[↓]\033[0m")
					tries += 1								
				elif number > person_number:
					print("\033[31m\033[1mx \033[34m[↑]\033[0m")					
					tries += 1
	elif command == "set.tg":
		tg = input("You in \033[36;1mTELEGRAM\033[0m: @")
		with open("profile.txt", "w") as f:
			f.write(name + "\n" + tg)
	elif command == "tg":
		if tg:
			print("Your \033[36;1mTELEGRAM\033[0m: @" + tg)
		else:
			print("\033[31;1mError: Empty\033[0m")
	elif command == "incognito":
		print("\033[H\033[J")
		print("  " * 7 + "\033[90m\033[1mPufiX | Turn off incognito mode: clear\033[0m")
		print("\033[90m ")
	elif command == "m" or command.startswith("m "):
		parts = command.split(maxsplit=1)
		if len(parts) > 1:
			print("\033[33;1m" + parts[1] + "\033[0m")
		else:
			print("\033[31m\033[1mError: EmptyText\033[0m")
	elif command == "sbigline":
		size = int(input("Size: "))
		print("≡" * size)
	elif command == "xline":
		size = int(input("Size: "))
		print("|||" * size)		
	elif command == "aline":
		size = int(input("Size: "))
		print("≈" * size)		
	elif command == "fline":
		size = int(input("Size: "))
		print("." * size)
	elif command == "gline":
		size = int(input("Size: "))
		print(("•·" * (size // 2 + 1))[:size])
	elif command == "pline":
		size = int(input("Size: "))
		print("`" * size)				
	elif command == "find.notebook":
		try:
			with open("notebook.txt", "r") as f:
				content = f.read()
			if content:
				print(content)
			else:
				print("\033[33m[notebook.txt is empty]\033[0m")
		except FileNotFoundError:
			print("\033[31m\033[1mError: notebook.txt not found\033[0m")
	elif command == "notebook" or command == "nb":
		notebook_open = True
		notebook_lines = []
		print("-" * 55)
		print("START  ('e.nb' to save & exit)")
		print("-" * 55)
	elif command == "e.notebook" or command == "e.nb":
		if notebook_open:
			notebook_open = False
			with open("notebook.txt", "w") as f:
				f.write("\n".join(notebook_lines))
			print("END")
			print("-" * 55)
			print("Saved: " + str(len(notebook_lines)) + " lines")
	elif command == "history":
		last = history[-10:]
		for i, cmd in enumerate(last, 1):
			print(str(i) + ". " + cmd)
	elif notebook_open:
		notebook_lines.append(command)
	elif command == "history.clear":
		history = []
		print("\033[33;1mCleared \033[32;1m[✓]\033[0m")
	elif command == "my.profile" or command == "profile":
		print("\033[1mName: \033[33;1m" + name + "\033[0m\n\033[36;1mTgUserName: \033[31;1m@\033[0m\033[33;1m" + tg + "\033[0m")
	elif command == "!program" or command == "!p":
		print("\033[1mThis \033[31;1mprogram: \033[36mPufiX\033[0m")
	elif command == "inspired":
		print("Inspired: \033[34;1mTERMUX ⟩_ \033[36;1m(Linux environment)\033[0m")
	elif command == "pkg":
		print("\033[1m[PufiX Pkg] Usage:\033[0m")
		print("  \033[36;1mpkg install <name>\033[0m  — install package")
		print("  \033[36;1mpkg remove <name>\033[0m   — remove package")
		print("  \033[36;1mpkg list\033[0m            — list installed")
		print("  \033[36;1mpkg commands <name>\033[0m — show commands")
	elif command == "pkg list":
		if not installed_packages:
			print("\033[33m[PufiX Pkg] No packages installed\033[0m")
		else:
			count = len(installed_packages)
			print("\033[33;1m[PufiX Pkg] Installed packages \033[0m\033[31;1m(" + str(count) + ")\033[33;1m:\033[0m")
			for pkg_name, pkg in installed_packages.items():
				desc = getattr(pkg, "DESCRIPTION", "no description")
				print("  \033[36;1m" + pkg_name + "\033[0m — " + desc)
	elif command == "pkg commands":
		if not installed_packages:
			print("\033[33m[PufiX Pkg] No packages installed\033[0m")
		else:
			print("\033[33;1m[PufiX Pkg] Commands from packages:\033[0m")
			for pkg_name, pkg in installed_packages.items():
				print("  \033[36;1m" + pkg_name + "\033[0m:")
				for cmd in pkg.COMMANDS:
					print("    \033[33m" + cmd + "\033[0m")
	elif command.startswith("pkg commands "):
		pkg_name = command[13:].strip()
		if pkg_name in installed_packages:
			pkg = installed_packages[pkg_name]
			print("\033[33;1m[PufiX Pkg] Commands in \"" + pkg_name + "\":\033[0m")
			for cmd in pkg.COMMANDS:
				print("  \033[33m" + cmd + "\033[0m")
		else:
			print("\033[31m\033[1m[PufiX Pkg] Error: package not installed\033[0m")
	elif command.startswith("pkg install "):
		pkg_name = command[12:]
		if install_package(pkg_name):
			print("\033[33;1m[PufiX Pkg] Installed: " + pkg_name + "\033[0m")
		else: 
			print("\033[31;1m[PufiX Pkg] Error: package not found\033[0m")
	elif command.startswith("pkg remove "):
		pkg_name = command[11:]
		if pkg_name in installed_packages:
			del installed_packages[pkg_name]
			print("\033[33;1m[PufiX Pkg] Removed: " + pkg_name + "\033[0m")
		else:
			print("\033[31;1m[PufiX Pkg] Error: package not installed\033[0m")
	elif command == "rock-paper-scissors" or command == "rps":
		try:
			size = int(input("Size: "))
		except ValueError:
			print("\033[31m\033[1mError: NoNumber\033[0m")
			continue
		print("=" * size)
		print("\033[1m          [ WRITE THE \"r\", \"p\" \033[31mOR\033[37m \"s\" | \"q\" — quit ]             \033[0m")
		while True:
			itemrps = input("\033[33;1m[ YOU ]\033[0m ")
			sysrps = random.choice(["r", "p", "s"])
			if itemrps == "r":
				if sysrps == "r":
					print("\033[1mYOU: \033[33m" + itemrps + "\n\033[37mSYS: \033[33m" + sysrps + "\033[0m" + "\nYOU vs SYS: ----")
				elif sysrps == "p":
					print("\033[1mYOU: \033[33m" + itemrps + "\n\033[37mSYS: \033[33m" + sysrps + "\033[0m" + "\n YOU vs SYS: SYS")
				elif sysrps == "s":
					print("\033[1mYOU: \033[33m" + itemrps + "\n\033[37mSYS: \033[33m" + sysrps + "\033[0m" + "\n YOU vs SYS: YOU")	
			elif itemrps == "p":
				if sysrps == "r":
					print("\033[1mYOU: \033[33m" + itemrps + "\n\033[37mSYS: \033[33m" + sysrps + "\033[0m" + "\nYOU vs SYS: YOU")
				elif sysrps == "p":
					print("\033[1mYOU: \033[33m" + itemrps + "\n\033[37mSYS: \033[33m" + sysrps + "\033[0m" + "\n YOU vs SYS: ----")
				elif sysrps == "s":
					print("\033[1mYOU: \033[33m" + itemrps + "\n\033[37mSYS: \033[33m" + sysrps + "\033[0m" + "\n YOU vs SYS: SYS")	
			elif itemrps == "s":
				if sysrps == "r":
					print("\033[1mYOU: \033[33m" + itemrps + "\n\033[37mSYS: \033[33m" + sysrps + "\033[0m" + "\nYOU vs SYS: SYS")
				elif sysrps == "p":
					print("\033[1mYOU: \033[33m" + itemrps + "\n\033[37mSYS: \033[33m" + sysrps + "\033[0m" + "\n YOU vs SYS: YOU")
				elif sysrps == "s":
					print("\033[1mYOU: \033[33m" + itemrps + "\n\033[37mSYS: \033[33m" + sysrps + "\033[0m" + "\n YOU vs SYS: ----")
			elif itemrps == "q":				
				print("=" * size)
				break
	elif command == "dice":
		print("\033[33;1m               " + random.choice(["⚀ / 1", "⚁ / 2", "⚂ / 3", "⚃ / 4", "⚄ / 5", "⚅ / 6"]) + " \033[0m")
	elif command == "coin-flip" or command == "cf":
		print("\033[33;1m" + random.choice(["HEADS ❶ ", "TAILS 🪙 "]) + "\033[0m")
	elif command == "timer" or command == "t":
		try:
			seconds = int(input("Seconds: "))
		except ValueError:
			print("\033[31m\033[1mError: NoNumber\033[0m")
			continue
		import time
		for sec in range(seconds, 0, -1):
			print(f"\033[33;1m {sec}s \033[0m", end="\r")
			time.sleep(1)
		print("\033[32;1mFINISHED [ ✓ ]\033[0m")
	else:
		handled = False
		for pkg in installed_packages.values():
			for cmd in pkg.COMMANDS:
				if command == cmd or command.	startswith(cmd + " ") or (cmd.endswith(".*") and command.startswith(cmd[:-1])):
					pkg.handle(command)
					handled = True
					break
			if handled:
				break
		if not handled:
			print("\033[31m\033[1mError: Unknown Command\033[0m")
