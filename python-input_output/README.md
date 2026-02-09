Python Input/Output (I/O): 

Reading & Writing Files

This guide explains how Python handles input/output (I/O), including:

* user input from the terminal (input)
* output to the terminal (print)
* reading from files
* writing to files
* common pitfalls (types, encoding, paths, exceptions)

What “I/O” means

I/O = Input/Output: the ways a program communicates with the outside world.

Common I/O sources

* Keyboard → input (user typing)
* Screen/Terminal → output (messages you print)
* Files → read/write data stored on disk
* (Also: networks, databases, sensors, etc.)

In Python, I/O is usually done through streams.

Standard streams: stdin, stdout, stderr
When you run a program in a terminal, it has 3 default 
streams:

* stdin (standard input): where input comes from (usually keyboard)
* stdout (standard output): where normal output goes (usually terminal)
* stderr (standard error): where errors/debug info go (usually terminal)

Example

name = input("Name? ")   # reads from stdin
print("Hi", name)        # writes to stdout

Why this matters: You can redirect these streams in a 
terminal:

python3 app.py > output.txt      # stdout to file
python3 app.py 2> errors.txt     # stderr to file
python3 app.py > all.txt 2>&1    # stdout + stderr to file

Terminal input with input()

input() always returns a 
string

Even if the user types a number, it comes in as text:

age = input("Age? ")
print(type(age))  # <class 'str'>

Convert types when needed

age = int(input("Age? "))          # whole numbers only
height = float(input("Height? "))  # decimals allowed

Handling comma decimals (5,6)

Some locales use , as decimal separator:

height = float(input("Height? ").replace(",", "."))

Validate input (avoid crashes)

If the user types something non-numeric, int() / float() will raise an error.
Use try/except:

while True:
    raw = input("Enter a number: ")
    try:
        number = int(raw)
        break
    except ValueError:
        print("Please enter a valid integer.")

Terminal output with print()

Basic print

print("Hello")
print("A", "B", "C")  # spaces between items by default

Formatting output

f-strings (recommended):
name = "Kedia"
print(f"Hello, {name}!")

Newlines

* print() adds a newline by default
* \n inside strings means 
“newline”

print("Line 1\nLine 2")

Controlling end and separator

print("A", "B", "C", sep="-")  # A-B-C
print("Loading...", end="")    # no newline at end

File I/O: reading and writing files

Key idea: file paths and the current directory

When you open "data.txt", Python looks in your current working directory (where you ran the program).

Check from Terminal:

pwd   # where am I?
ls    # what files are here?

Opening files: open() and modes

Python uses open(path, mode, encoding=...).

Common modes

* "r" → read (file must exist)
* "w" → write (creates file, overwrites if exists)
* "a" → append (creates file, writes at end)
* "x" → create (fails if file exists)
* Add "b" for binary (images, PDFs, etc.), e.g. "rb", "wb"

Examples:

open("file.txt", "r", encoding="utf-8")  # read text
open("file.txt", "w", encoding="utf-8")  # overwrite/write
open("file.txt", "a", encoding="utf-8")  # append

Always close files: use with

The safest pattern is a context manager:

with open("notes.txt", "r", encoding="utf-8") as f:
    content = f.read()

with automatically closes the file even if an error happens.

Reading files

1) Read the entire file
with open("notes.txt", "r", encoding="utf-8") as f:
    content = f.read()
print(content)

2) Read line-by-line (best for large files)
with open("notes.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.rstrip())  # remove trailing newline

3) Read all lines into a list
with open("notes.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
print(lines)

Writing files

1) Write (overwrite)
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Hello!\n")
    f.write("Second line.\n")

2) Append (add to end)
with open("log.txt", "a", encoding="utf-8") as f:
    f.write("New entry\n")

3) Write multiple lines at once
lines = ["one\n", "two\n", "three\n"]
with open("list.txt", "w", encoding="utf-8") as f:
    f.writelines(lines)

pathlib: modern path handling (recommended)

pathlib.Path makes file paths cleaner and cross-platform.

from pathlib import Path

path = Path("notes.txt")

# Read all text
text = path.read_text(encoding="utf-8")

# Write text (overwrite)
path.write_text("Hello\n", encoding="utf-8")

Useful checks:

if path.exists():
    print("File exists!")

Encoding: why utf-8 matters

Text files must be decoded/encoded. Using encoding="utf-8" avoids weird issues with accented characters.

✅ Recommended:

open("file.txt", "r", encoding="utf-8")

Common errors (and what they mean)

FileNotFoundError

You tried to read a file that doesn’t exist in the current folder.
* Fix: check pwd, ls, or use the correct path.

PermissionError

You don’t have permission to read/write at that location.

* Fix: choose a folder you own (like your home folder).

ValueError: invalid literal for int()

You tried int("5,6") or int("abc").

*Fix: validate input, or use float() and handle commas.

TypeError: '>=' not supported between instances of 'str' and 'int'

You compared text from input() directly to a number.

* Fix: convert input first (int(...) or float(...)).

Flushing and buffering (advanced but useful)

Output may be buffered (delayed) in some environments.

Force immediate printing:

print("Working...", flush=True)

Mini example: ask user, write to file, read it back

from pathlib import Path

path = Path("names.txt")

name = input("What's your name? ").strip()

# Append name to file
with path.open("a", encoding="utf-8") as f:
    f.write(name + "\n")

# Read and display all names
print("\nAll saved names:")
print(path.read_text(encoding="utf-8"))
Run from terminal:
python3 app.py
Summary checklist
input() returns string
Convert types (int, float) before math/comparisons
Use with open(...) as f: to avoid forgetting close()
Choose correct file mode: r, w, a
Use encoding="utf-8" for text files
Use pathlib.Path for cleaner paths
If file isn’t found: check pwd + ls
