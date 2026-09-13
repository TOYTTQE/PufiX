COMMANDS = ["sound", "soundex", "syllables", "leet", "vowels", "consonants", "spell"]
DESCRIPTION = "Sound — phonetics, transcription, leet"

UNTRANSLIT = [
	("my", "май"), ("bough", "бау"), ("tough", "таф"), ("thor", "сёр"), ("colonel", "кёрнел"), ("through", "сру"), ("aone", "аон"), ("bone", "бон"), ("cone", "кон"), ("done", "дон"), ("eone", "ион"), ("fone", "фон"), ("gone", "гон"), ("hone", "хане"), ("ione", "айон"), ("jone", "джон"), ("kone", "кон"), ("lone", "лон"), ("mone", "мане"), ("none", "нон"), ("oone", "оон"), ("pone", "пон"), ("qone", "кьён"), ("rone", "рон"), ("sone", "сон"), ("tone", "тон"), ("uone", "уон"), ("vone", "вон"), ("wone", "вон"), ("xone", "ксон"), ("yone", "йон"), ("zone", "зон"), ("queue", "кью"), ("together", "тугезер"), ("ite", "айт"), ("eople", "ипл"), ("iend", "энд"), ("every", "эври"), ("lear", "лёр"), ("are", "ар"), ("thing", "финг"), ("some", "сам"), ("machine", "машин"), ("future", "фьючер"), ("eau", "ью"), ("with", "виз"), ("get", "гет"), ("eye", "ай"), ("of", "оф"), ("cen", "цен"), ("ace", "ейс"), ("ice", "айс"), ("lover", "лавер"), ("love", "лав"), ("gir", "гёр"), ("ce", "се"), ("gi", "джи"), ("ge", "дж"), ("gy", "джи"), ("ci", "си"), ("cy", "сай"), ("one", "уан"), ("two", "ту"), ("three", "фри"), ("four", "фо"), ("five", "файв"), ("six", "сикс"), ("seven", "севен"), ("eight", "эйт"), ("nine", "найн"), ("uni", "юни"), ("but", "бат"), ("cup", "кап"), ("luck", "лак"), ("sun", "сан"), ("igh", "ай"), ("hel", "хэл"), ("our", "аур"), ("un", "ан"), ("your", "ёур"), ("you", "ю"), ("tech", "тех"), ("he", "хи"), ("she", "ши"), ("tion", "шн"), ("sion", "жн"), ("ough", "оу"), ("augh", "ау"), ("eigh", "эй"),
	("shch", "щ"), ("sch", "щ"),
	("yo", "ё"), ("zh", "ж"), ("kh", "к"), ("ts", "ц"), ("ch", "ч"),
	("sh", "ш"), ("yu", "ю"), ("ya", "я"),
	("ph", "ф"), ("ck", "к"), ("th", "в"), ("gh", "ф"),
	("wh", "у"), ("qu", "кв"), ("ng", "нг"), ("kn", "н"), ("wr", "р"),
	("ea", "и"), ("ee", "и"), ("oo", "у"),
	("ai", "эй"), ("ay", "эй"), ("ei", "эй"), ("ey", "ей"), ("oy", "ой"),
	("ou", "ау"), ("ow", "ау"), ("oa", "оу"),
	("ie", "и"), ("ue", "у"), ("ui", "у"), ("au", "ав"),
	("h", "х"), ("c", "к"), ("j", "й"), ("k", "к"),
	("b", "б"), ("v", "в"), ("g", "г"), ("d", "д"),
	("e", "е"), ("z", "з"), ("i", "и"),
	("l", "л"), ("m", "м"), ("n", "н"), ("o", "оу"), ("p", "п"),
	("r", "р"), ("s", "с"), ("t", "т"), ("u", "у"), ("f", "ф"),
	("x", "кс"), ("y", "и"), ("w", "в"), ("a", "э"),
	("''", "ъ"), ("'", "ь"),
]

READ_LETTERS = {
	"a": "эй", "b": "би", "c": "си", "d": "ди", "e": "и",
	"f": "эф", "g": "джи", "h": "эйч", "i": "ай", "j": "джей",
	"k": "кей", "l": "эл", "m": "эм", "n": "эн", "o": "оу",
	"p": "пи", "q": "кью", "r": "эр", "s": "эс", "t": "ти",
	"u": "ю", "v": "ви", "w": "дабл-ю", "x": "икс", "y": "уай",
	"z": "зи",
}

LEET = {
	"a": "4", "b": "β", "c": "¢", "d": "δ", "e": "3", "f": 		"φ", "g": "γ", "h": "η", "i": "1", "j": "/", "k": "κ", "l": "|",	"m": "μ", "n": "ν", "o": "0", "p": "π", "q": "θ", "r": "ρ",	"s": "5", "t": "7", "u": "υ", "v": "↓", "w": "→", "x": "χ",
	"y": "¥", "z": "2",
}

VOWELS_EN = set("aeiouy")
VOWELS_RU = set("аеёиоуыэюя")
CONSONANTS_EN = set("bcdfghjklmnpqrstvwxz")
CONSONANTS_RU = set("бвгджзйклмнпрстфхцчшщ")

def soundex(word):
	word = word.upper()
	if not word:
		return ""
	first = word[0]
	mapping = {
		# Английские
	"B": "1", "F": "1", "P": "1", "V": "1",
	"C": "2", "G": "2", "J": "2", "K": "2", "Q": "2", "S": "2", "X": "2", "Z": "2",
	"D": "3", "T": "3",
	"L": "4",
	"M": "5", "N": "5", "R": "6",
	# Русские (по фонетическому принципу)
	"Б": "1", "П": "1", "Ф": "1", "В": "1",
	"Ц": "2", "Г": "2", "Ж": "2", "К": "2", "С": "2", "Х": "2", "З": "2", "Ш": "2", "Щ": "2",
	"Д": "3", "Т": "3",
	"Л": "4",
	"М": "5", "Н": "5",
	"Р": "6",
	}
	result = first
	prev = mapping.get(first, "")
	for c in word[1:]:
		code = mapping.get(c, "")
		if code and code != prev:
			result += code
		prev = code
	result = (result + "000")[:4]
	return result

def handle(command):
	parts = command.split(maxsplit=1)
	cmd = parts[0]
	arg = parts[1] if len(parts) > 1 else ""

	if not arg:
		print("\033[31m\033[1mError: EmptyText\033[0m")
		return

	if cmd == "sound":
		result = ""
		i = 0
		while i < len(arg):
			matched = False
			for trans, rus in UNTRANSLIT:
				if arg[i:i+len(trans)].lower() == trans:
					result += rus if arg[i].islower() else rus.upper()
					i += len(trans)
					matched = True
					break
			if not matched:
				result += arg[i]
				i += 1
		print("\033[33m" + result + "\033[0m")

	elif cmd == "soundex":
		for word in arg.split():
			print("\033[33m" + word + "\033[0m → \033[36m" + soundex(word) + "\033[0m")

	elif cmd == "syllables":
		text = arg.lower()
		count = 0
		prev_vowel = False
		for c in text:
			is_vowel = c in VOWELS_EN or c in VOWELS_RU
			if is_vowel and not prev_vowel:
				count += 1
			prev_vowel = is_vowel
		if count == 0:
			count = 1
		print("\033[33m" + str(count) + "\033[0m")

	elif cmd == "leet":
		result = ""
		for c in arg:
			if c.lower() in LEET:
				result += LEET[c.lower()]
			else:
				result += c
		print("\033[33m" + result + " \033[0m")

	elif cmd == "vowels":
		result = []
		for c in arg:
			if c.lower() in VOWELS_EN or c.lower() in VOWELS_RU:
				result.append(c)
		print("\033[33m" + ", ".join(result) + "\033[0m")

	elif cmd == "consonants":
		result = []
		for c in arg:
			if c.lower() in CONSONANTS_EN or c.lower() in CONSONANTS_RU:
				result.append(c)
		print("\033[33m" + ", ".join(result) + "\033[0m")

	elif cmd == "spell":
		result = []
		for c in arg.lower():
			if c in READ_LETTERS:
				result.append(READ_LETTERS[c])
			else:
				result.append(c)
		print("\033[33m" + " ".join(result) + "\033[0m")
