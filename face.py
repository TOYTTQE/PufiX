COMMANDS = ["face.list", "face.random", "face.*"]
DESCRIPTION = "ASCII faces collection"

faces = {
	"face.happy": ":)",
	"face.sad": ":(",
	"face.sad.tearful": ";(",
	"face.happy.tearful": ";)",
	"face.dead": "×_×",
	"face.fdead": "x_x",
	"face.sleep": "UoU ᶻzᶻ",
	"face.superhappy.ceyes": "U∇U",
	"face.surprised": "OΔO",
	"face.surprised.happy": "O∇O",
	"face.embarrassed": "O_O",
	"face.unhappiness": "UΔU",
	"face.worried": "O~O",
	"face.worried.ceyes": "U~U",
	"face.worried.dual": "O≈O",
	"face.worried.dual.ceyes": "U≈U",
	"face.cute": "UwU",
	"face.cat": "^owo^",
	"face.goat": "ΘυΘ",
	"face.imp": "`•η•‘",
	"face.fwh": "`•u•‘",
	"face.tongue": "OuO",
	"face.cry": "T_T",
	"face.smile.cry": "TuT",
	"face.unhappiness.cry": "TηT",
	"face.laughing": "`U∇U,",
}

def handle(command):
	import random
	if command == "face.list":
		for fname, fval in faces.items():
			print(fname + " " * (35 - len(fname)) + fval)
	elif command == "face.random":
		print("\033[33m" + random.choice(list(faces.values())) + "\033[0m")
	elif command.startswith("face."):
		if command in faces:
			print("\033[33m" + faces[command] + "\033[0m")
		else:
			print("\033[31m\033[1mError: UnknownFace\033[0m")
