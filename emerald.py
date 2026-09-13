COMMANDS = ["emerald"]
DESCRIPTION = "Emerald — Markdown notes for PufiX"

import os
import re
import datetime

VAULT = "vault"

def ensure_vault():
	if not os.path.exists(VAULT):
		os.makedirs(VAULT)

def parse_states(content):
	m = re.search(r'<!--\s*states:\s*([\d,\s]*)\s*-->', content)
	if not m:
		return []
	raw = m.group(1).strip()
	if not raw:
		return []
	return [int(x) for x in raw.split(",") if x.strip().isdigit()]

def render_md(text, states=None):
	if states is None:
		states = parse_states(text)

	# Убираем служебную строку
	text = re.sub(r'<!--\s*states:[\d,\s]*-->', '', text)
	text = text.rstrip()

	lines = text.split("\n")
	result = []
	in_code = False
	checkbox_num = 0

	for line in lines:
		if line.strip().startswith("```"):
			in_code = not in_code
			result.append("\033[7m\033[38;5;248m" + "─" * 40 + "\033[0m")
			continue
		if in_code:
			result.append("\033[7m\033[38;5;248m" + line.ljust(40) + "\033[0m")
			continue

		# Чекбокс
		cb_match = re.match(r'^- \[ \]\s*-?\s*(.*)$', line)
		if cb_match:
			checkbox_num += 1
			text_part = cb_match.group(1)
			if checkbox_num in states:
				mark = "\033[32m\033[1m[ ✓ ]\033[0m"
			else:
				mark = "\033[31m\033[1m[ x ]\033[0m"
			result.append("\033[1m • \033[0m" + mark + " \033[1m[" + str(checkbox_num) + "]\033[0m \033[36m-\033[0m " + text_part)
			continue

		# Заголовки
		if line.startswith("###### "):
			result.append("\033[38;5;255m# " + line[7:] + " #\033[0m")
		elif line.startswith("##### "):
			result.append("\033[38;5;253m## " + line[6:] + " ##\033[0m")
		elif line.startswith("#### "):
			result.append("\033[38;5;251m### " + line[5:] + " ###\033[0m")
		elif line.startswith("### "):
			result.append("\033[38;5;249m#### " + line[4:] + " ####\033[0m")
		elif line.startswith("## "):
			result.append("\033[38;5;247m##### " + line[3:] + " #####\033[0m")
		elif line.startswith("# "):
			result.append("\033[38;5;245m###### " + line[2:] + " ######\033[0m")
		elif line.startswith("> "):
			result.append("\033[38;5;171m\033[7m " + line[2:] + "\033[0m")
		elif line.startswith("- "):
			result.append("\033[1m • " + line[2:] + "\033[0m")
		else:
			l = line
			l = re.sub(r'\*\*(.+?)\*\*', r'\033[1m\1\033[0m', l)
			l = re.sub(r'\*([^*]+?)\*', r'/\1/', l)
			l = re.sub(r'==(.+?)==', r'\033[38;5;228m\033[7m\1\033[0m', l)
			l = re.sub(r'`(.+?)`', r'\033[7m\033[38;5;248m\1\033[0m', l)
			l = re.sub(r'\[\[(.+?)\]\]', r'\033[38;5;171m\033[4m\1\033[0m', l)
			l = re.sub(r'#(\w+)', r'\033[38;5;171m\033[7m#\1\033[0m', l)
			result.append(l)
	return "\n".join(result)

def find_note(name):
	path = os.path.join(VAULT, name + ".md")
	return path if os.path.exists(path) else None

def update_states(path, states):
	with open(path, "r") as f:
		content = f.read()
	# Убираем старую строку states
	content = re.sub(r'\n?<!--\s*states:[\d,\s]*-->\s*$', '', content)
	# Добавляем новую
	states_str = ",".join(str(s) for s in sorted(states))
	content = content.rstrip() + "\n<!-- states: " + states_str + " -->\n"
	with open(path, "w") as f:
		f.write(content)

def handle(command):
	parts = command.split(maxsplit=3)
	cmd = parts[0]
	sub = parts[1] if len(parts) > 1 else ""
	arg = parts[2] if len(parts) > 2 else ""
	arg = arg.strip().strip('"').strip("'")
	num = parts[3] if len(parts) > 3 else ""

	if cmd != "emerald":
		return

	ensure_vault()

	if not sub:
		print("\033[1memerald — Markdown Notes:\033[0m")
		print("  \033[36memerald new\033[0m <title>          — create")
		print("  \033[36memerald list\033[0m                 — list notes")
		print("  \033[36memerald show\033[0m <title>         — read")
		print("  \033[36memerald edit\033[0m <title>         — edit")
		print("  \033[36memerald delete\033[0m <title>       — delete")
		print("  \033[36memerald search\033[0m <word>        — search")
		print("  \033[36memerald links\033[0m <title>        — backlinks")
		print("  \033[36memerald tags\033[0m                 — all tags")
		print("  \033[36memerald stats\033[0m                — stats")
		print("  \033[36memerald daily\033[0m                — daily note")
		print("  \033[36memerald <note> set.y <n>\033[0m     — check checkbox")
		print("  \033[36memerald <note> set.n <n>\033[0m     — uncheck checkbox")
		return

	# set.y / set.n
	if sub in ("set.y", "set.n"):
		print("\033[31m\033[1mError: Use 'emerald <note> " + sub + " <n>'\033[0m")
		return

	if arg in ("set.y", "set.n"):
		note_name = sub
		action = arg
		if not num:
			print("\033[31m\033[1mError: NoNumber\033[0m")
			return
		if not num.isdigit():
			print("\033[31m\033[1mError: NoNumber\033[0m")
			return
		path = find_note(note_name)
		if not path:
			print("\033[31m\033[1mError: NoteNotFound\033[0m")
			return
		with open(path, "r") as f:
			content = f.read()
		states = parse_states(content)
		n = int(num)
		# Проверяем, что n не больше кол-ва чекбоксов
		cb_count = len(re.findall(r'^- \[ \]', content, re.MULTILINE))
		if n < 1 or n > cb_count:
			print("\033[31m\033[1mError: CheckboxNotFound\033[0m")
			return
		if action == "set.y":
			if n not in states:
				states.append(n)
		elif action == "set.n":
			if n in states:
				states.remove(n)
		update_states(path, states)
		print("\033[33;1m[emerald] Updated: " + note_name + "\033[0m")
		return

	if sub == "new":
		if not arg:
			print("\033[31m\033[1mError: NoTitle\033[0m")
			return
		path = os.path.join(VAULT, arg + ".md")
		if os.path.exists(path):
			print("\033[31m\033[1mError: NoteExists\033[0m")
			return
		try:
			with open(path, "w") as f:
				f.write("# " + arg + "\n")
			print("\033[33;1m[emerald] Created: " + arg + "\033[0m")
		except (PermissionError, OSError) as e:
			print("\033[31m\033[1mError: CannotWrite <" + str(e) + ">\033[0m")

	elif sub == "list":
		notes = [f[:-3] for f in os.listdir(VAULT) if f.endswith(".md")]
		if not notes:
			print("\033[33m[emerald] No notes\033[0m")
			return
		print("\033[33;1m[emerald] Notes (" + str(len(notes)) + "):\033[0m")
		for note in sorted(notes):
			print("  \033[36m" + note + "\033[0m")

	elif sub == "show":
		if not arg:
			print("\033[31m\033[1mError: NoTitle\033[0m")
			return
		path = find_note(arg)
		if not path:
			print("\033[31m\033[1mError: NoteNotFound\033[0m")
			return
		with open(path, "r") as f:
			content = f.read()
		print(render_md(content))

	elif sub == "edit":
		if not arg:
			print("\033[31m\033[1mError: NoTitle\033[0m")
			return
		path = find_note(arg)
		lines = []
		if path:
			with open(path, "r") as f:
				content = f.read()
			if content:
				lines = content.split("\n")
				print("\033[33m[emerald] Loaded: " + arg + "\033[0m")
		else:
			path = os.path.join(VAULT, arg + ".md")
			print("\033[33m[emerald] New note: " + arg + "\033[0m")

		print("  \033[36m:w\033[0m save | \033[36m:q\033[0m quit | \033[36m:wq\033[0m save&quit")
		while True:
			try:
				line = input("\033[90m> \033[0m")
			except KeyboardInterrupt:
				return
			if line == ":q":
				return
			elif line == ":w":
				try:
					with open(path, "w") as f:
						f.write("\n".join(lines))
					print("\033[32m[emerald] Saved\033[0m")
				except (PermissionError, OSError) as e:
					print("\033[31m\033[1mError: CannotWrite <" + str(e) + ">\033[0m")
			elif line == ":wq":
				try:
					with open(path, "w") as f:
						f.write("\n".join(lines))
					print("\033[32m[emerald] Saved & closed\033[0m")
					return
				except (PermissionError, OSError) as e:
					print("\033[31m\033[1mError: CannotWrite <" + str(e) + ">\033[0m")
					return
			else:
				lines.append(line)

	elif sub == "delete":
		if not arg:
			print("\033[31m\033[1mError: NoTitle\033[0m")
			return
		path = find_note(arg)
		if not path:
			print("\033[31m\033[1mError: NoteNotFound\033[0m")
			return
		try:
			os.remove(path)
			print("\033[33;1m[emerald] Deleted: " + arg + "\033[0m")
		except (PermissionError, OSError) as e:
			print("\033[31m\033[1mError: CannotDelete <" + str(e) + ">\033[0m")

	elif sub == "search":
		if not arg:
			print("\033[31m\033[1mError: NoWord\033[0m")
			return
		found = []
		for fname in os.listdir(VAULT):
			if not fname.endswith(".md"):
				continue
			with open(os.path.join(VAULT, fname), "r") as f:
				content = f.read()
			if arg.lower() in content.lower():
				found.append(fname[:-3])
		if not found:
			print("\033[33m[emerald] Not found\033[0m")
			return
		print("\033[33;1m[emerald] Found in:\033[0m")
		for note in found:
			print("  \033[36m" + note + "\033[0m")

	elif sub == "links":
		if not arg:
			print("\033[31m\033[1mError: NoTitle\033[0m")
			return
		found = []
		for fname in os.listdir(VAULT):
			if not fname.endswith(".md"):
				continue
			with open(os.path.join(VAULT, fname), "r") as f:
				content = f.read()
			if "[[" + arg + "]]" in content:
				found.append(fname[:-3])
		if not found:
			print("\033[33m[emerald] No backlinks\033[0m")
			return
		print("\033[33;1m[emerald] Backlinks to \"" + arg + "\":\033[0m")
		for note in found:
			print("  \033[36m" + note + "\033[0m")

	elif sub == "tags":
		tags = {}
		for fname in os.listdir(VAULT):
			if not fname.endswith(".md"):
				continue
			with open(os.path.join(VAULT, fname), "r") as f:
				content = f.read()
			for line in content.split("\n"):
				if re.match(r'^#{1,6} ', line):
					continue
				for word in line.split():
					if word.startswith("#") and len(word) > 1:
						tag = word.strip("#.,!?")
						tags[tag] = tags.get(tag, 0) + 1
		if not tags:
			print("\033[33m[emerald] No tags\033[0m")
			return
		print("\033[33;1m[emerald] Tags:\033[0m")
		for tag, count in sorted(tags.items()):
			print("  \033[36m#" + tag + "\033[0m (" + str(count) + ")")

	elif sub == "stats":
		notes = [f for f in os.listdir(VAULT) if f.endswith(".md")]
		total_words = 0
		for fname in notes:
			with open(os.path.join(VAULT, fname), "r") as f:
				total_words += len(f.read().split())
		print("\033[33;1m[emerald] Stats:\033[0m")
		print("  Notes: \033[36m" + str(len(notes)) + "\033[0m")
		print("  Words: \033[36m" + str(total_words) + "\033[0m")

	elif sub == "daily":
		today = datetime.datetime.now().strftime("%Y-%m-%d")
		path = os.path.join(VAULT, today + ".md")
		if not os.path.exists(path):
			try:
				with open(path, "w") as f:
					f.write("# " + today + "\n")
				print("\033[33;1m[emerald] Created daily: " + today + "\033[0m")
			except (PermissionError, OSError) as e:
				print("\033[31m\033[1mError: CannotWrite <" + str(e) + ">\033[0m")
				return
		else:
			print("\033[33;1m[emerald] Daily " + today + " already exists\033[0m")
		with open(path, "r") as f:
			print(render_md(f.read()))
