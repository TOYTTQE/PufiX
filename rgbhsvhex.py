COMMANDS = ["rgb", "hsv", "hex", "list colors"]
DESCRIPTION = "Colored text via RGB/HSV/HEX (256 colors)"

def rgb_to_256(r, g, b):
	if abs(r - g) < 10 and abs(g - b) < 10 and abs(r - b) < 10:
		if r < 8:
			return 16
		if r > 248:
			return 231
		return 232 + int((r - 8) / 247 * 23)
	ri = int(r / 255 * 5)
	gi = int(g / 255 * 5)
	bi = int(b / 255 * 5)
	return 16 + (36 * ri) + (6 * gi) + bi

def rgb_to_ansi(r, g, b):
	n = rgb_to_256(r, g, b)
	return "\033[38;5;" + str(n) + "m"

def hsv_to_rgb(h, s, v):
	s = s / 100
	v = v / 100
	c = v * s
	x = c * (1 - abs((h / 60) % 2 - 1))
	m = v - c
	if h < 60:
		r, g, b = c, x, 0
	elif h < 120:
		r, g, b = x, c, 0
	elif h < 180:
		r, g, b = 0, c, x
	elif h < 240:
		r, g, b = 0, x, c
	elif h < 300:
		r, g, b = x, 0, c
	else:
		r, g, b = c, 0, x
	return int((r + m) * 255), int((g + m) * 255), int((b + m) * 255)

def handle(command):
	if command == "list colors":
		print("\033[1m256 colors:\033[0m")
		for i in range(0, 256, 16):
			row = ""
			for j in range(i, i + 16):
				row += "\033[48;5;" + str(j) + "m  \033[0m"
			print("\033[90m" + str(i).rjust(3) + ":\033[0m " + row)
		return

	parts = command.split(maxsplit=2)
	cmd = parts[0]
	arg = parts[1] if len(parts) > 1 else ""
	text = parts[2] if len(parts) > 2 else ""

	if not arg or not text:
		print("\033[31m\033[1mUsage:\033[0m")
		print("  rgb <r,g,b> <text>")
		print("  hsv <h,s,v> <text>")
		print("  hex <#RRGGBB> <text>")
		return

	if cmd == "rgb":
		try:
			vals = arg.replace(" ", "").split(",")
			r, g, b = int(vals[0]), int(vals[1]), int(vals[2])
			if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
				print("\033[31m\033[1mError: RGB out of range (0-255)\033[0m")
				return
			print(rgb_to_ansi(r, g, b) + text + "\033[0m")
		except (ValueError, IndexError):
			print("\033[31m\033[1mError: InvalidRGB (use: rgb 255,0,0 text)\033[0m")

	elif cmd == "hsv":
		try:
			vals = arg.replace(" ", "").split(",")
			h, s, v = int(vals[0]), int(vals[1]), int(vals[2])
			if not (0 <= h <= 360 and 0 <= s <= 100 and 0 <= v <= 100):
				print("\033[31m\033[1mError: HSV out of range\033[0m")
				return
			r, g, b = hsv_to_rgb(h, s, v)
			print(rgb_to_ansi(r, g, b) + text + "\033[0m")
		except (ValueError, IndexError):
			print("\033[31m\033[1mError: InvalidHSV (use: hsv 360,100,100 text)\033[0m")

	elif cmd == "hex":
		try:
			hex_val = arg.replace("#", "")
			if len(hex_val) != 6:
				print("\033[31m\033[1mError: InvalidHEX (use: #RRGGBB)\033[0m")
				return
			r = int(hex_val[0:2], 16)
			g = int(hex_val[2:4], 16)
			b = int(hex_val[4:6], 16)
			print(rgb_to_ansi(r, g, b) + text + "\033[0m")
		except ValueError:
			print("\033[31m\033[1mError: InvalidHEX (use: #RRGGBB)\033[0m")
