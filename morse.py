COMMANDS = ["to-morse", "from-morse"]
DESCRIPTION = "Text to Morse code"

MORSE = {
	"А": ".-", "Б": "-...", "В": ".--", "Г": "--.", "Д": "-..",
	"Е": ".", "Ж": "...-", "З": "--..", "И": "..", "Й": ".---",
	"К": "-.-", "Л": ".-..", "М": "--", "Н": "-.", "О": "---",
	"П": ".--.", "Р": ".-.", "С": "...", "Т": "-", "У": "..-",
	"Ф": "..-.", "Х": "....", "Ц": "-.-.", "Ч": "---.", "Ш": "----",
	"Щ": "--.-", "Ъ": "--.--", "Ы": "-.--", "Ь": "-..-", "Э": "..-..",
	"Ю": "..--", "Я": ".-.-",
	"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
	"F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
	"K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
	"P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
	"U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
	"Z": "--..",
	"0": "-----", "1": ".----", "2": "..---", "3": "...--",
	"4": "....-", "5": ".....", "6": "-....", "7": "--...",
	"8": "---..", "9": "----.",
	".": ".-.-.-", ",": "--..--", "?": "..--..", "!": "-.-.--",
	"/": "-..-.", "-": "-....-", "(": "-.--.", ")": "-.--.-",
	":": "---...", ";": "-.-.-.", "=": "-...-", "+": ".-.-.",
	"@": ".--.-.",
}

MORSE_REV_RU = {}
MORSE_REV_EN = {}
for k, v in MORSE.items():
	if "А" <= k <= "Я":
		MORSE_REV_RU[v] = k
	elif "A" <= k <= "Z":
		MORSE_REV_EN[v] = k
	else:
		MORSE_REV_RU[v] = k
		MORSE_REV_EN[v] = k

def handle(command):
	parts = command.split(maxsplit=1)
	cmd = parts[0]
	arg = parts[1] if len(parts) > 1 else ""

	if not arg:
		print("\033[31m\033[1mError: EmptyText\033[0m")
		return

	if cmd == "to-morse":
		result = []
		for char in arg.upper():
			if char == " ":
				result.append("/")
			elif char in MORSE:
				result.append(MORSE[char])
			else:
				result.append("?")
		print("\033[33m" + " ".join(result) + "\033[0m")

	elif cmd == "from-morse":
		ru_mode = False
		if arg.startswith("RU "):
			ru_mode = True
			arg = arg[3:]
		elif arg.startswith("EN "):
			arg = arg[3:]

		result = ""
		for code in arg.split(" "):
			if code == "/":
				result += " "
			elif ru_mode and code in MORSE_REV_RU:
				result += MORSE_REV_RU[code]
			elif not ru_mode and code in MORSE_REV_EN:
				result += MORSE_REV_EN[code]
			else:
				result += "?"
		print("\033[33m" + result + "\033[0m")
