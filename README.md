# PufiX

![Version](https://img.shields.io/badge/version-1.1.0-blue)
![Python](https://img.shields.io/badge/python-3.x-green)
![License](https://img.shields.io/badge/license-MIT-orange)

A text-based terminal application inspired by **Termux**, packed with utilities, games, and tools.

## Features

- 📝 **Notebook** — save and manage notes
- 🧮 **Calculator** — basic math operations
- 🎮 **Games** — rock-paper-scissors, dice, coin-flip, guess-the-number
- ⏱️ **Timer** — countdown timer
- 📚 **Text Tools** — text formatting, colorization
- 📦 **Package System** — install/remove packages dynamically
- 🎨 **Customization** — custom colors, text styles, lines
- 💾 **Profile** — save user profile with name and Telegram

## Commands

### Core Commands
| Command | Alias | Description |
|---------|-------|-------------|
| `me` | — | Show your name |
| `tg` | — | Show your Telegram username |
| `set.tg` | — | Set your Telegram username |
| `edit.name` | `e.n` | Edit your name |
| `my.profile` | `profile` | View full profile |
| `.` or `help` | — | Show all commands |

### Games 🎮
| Command | Alias | Description |
|---------|-------|-------------|
| `guess-the-number` | `gtn` | Guess the number (1-10) |
| `rock-paper-scissors` | `rps` | Play RPS against computer |
| `dice` | — | Roll a dice (1-6) |
| `coin-flip` | `cf` | Flip a coin |

### Tools ⏱️
| Command | Alias | Description |
|---------|-------|-------------|
| `timer` | `t` | Countdown timer |
| `calc.base` | — | Basic calculator (+, -, *, /) |
| `py.base` | — | Python print/input helper |

### Notebook 📝
| Command | Alias | Description |
|---------|-------|-------------|
| `notebook` | `nb` | Open notebook for writing |
| `e.notebook` | `e.nb` | Save and exit notebook |
| `find.notebook` | — | View saved notes |

### Text & Lines 🎨
| Command | Alias | Description |
|---------|-------|-------------|
| `m <text>` | — | Print colored text |
| `line` | — | Print line with `-` |
| `bigline` | — | Print line with `=` |
| `sbigline` | — | Print line with `≡` |
| `xline` | — | Print line with `\|\|\|` |
| `aline` | — | Print line with `≈` |
| `fline` | — | Print line with `.` |
| `gline` | — | Print line with `•·` |
| `pline` | — | Print line with `` ` `` |
| `undertext` | `ut` | Enable underline text |
| `basetext` | `bt` | Reset text formatting |

### System
| Command | Alias | Description |
|---------|-------|-------------|
| `clear` | — | Clear terminal |
| `incognito` | — | Incognito mode |
| `red.sys` | `r.s` | Red system prompt |
| `set.title` | — | Set custom title |
| `!program` | `!p` | Show program info |
| `inspired` | — | Show inspiration |

### History
| Command | Description |
|---------|-------------|
| `history` | Show last 10 commands |
| `history.clear` | Clear command history |

### Package System 📦
| Command | Description |
|---------|-------------|
| `pkg list` | List installed packages |
| `pkg install <name>` | Install a package |
| `pkg remove <name>` | Remove a package |
| `pkg commands` | Show all package commands |
| `pkg commands <name>` | Show commands for specific package |

## Installed Packages

- **face** — emoji faces
- **window_editor** — text editor
- **sys** — system info (date, time, etc.)
- **text** — text processing
- **crpassword** — password generator
- **binarytext** — binary/text conversion
- **rgbhsvhex** — color conversion
- **morse** — morse code
- **qlist** — quick list management
- **qlist_tablesizes** — table tools
- **esound** — sound effects
- **emerald** — emerald theme

## Installation

git clone https://github.com/TOYTTQE/PufiX.git
cd PufiX
python3 PufiX

## Usage

Run the program:

python3 PufiX

Enter your name and Telegram username on first run.

## What's New in v1.1.0 🎉

✨ **New Games:**
- 🎮 Rock-Paper-Scissors (`rps`) — play against computer
- 🎲 Dice (`dice`) — roll a dice
- 🪙 Coin Flip (`cf`) — flip a coin

⏱️ **New Tools:**
- `timer` — countdown timer with live display

## License

MIT License — feel free to use and modify!

## Author

Created with ❤️ by TOYTTQE

## Inspired by

TERMUX ⟩_ (Linux environment)
