# Join method
', '.join(["cats", "rats", "bats"])
" ".join(["My", "name", "is", "Simon"])

# Split method
"My name is Simon".split(" ")

spam = '''Dear Alice,
How have you been? I am fine. There is a container in the fridge that is labeled "Milk Experiment."
Please do not drink it.
Sincerely,
Bob'''
spam.split("\n")

# partition method
'Hello, world!'.partition('w')
"Hello, world!".partition("world")


before, sep, after = "Hello, world".partition(" ")
print(before)
print(after)

# Justifying text with rjust, ljust, center methods
"Hello".rjust(10)
"Hello".rjust(20)
"Hello".ljust(10, "*")

"Hello".center(20)

# Removing whiteplace with strip, rstrip and lstrip methods
spam = "    Hello, world    "
spam.strip()

spam.lstrip()
spam.rstrip()



spam = "SpamSpamBaconSpamEggsSpamSpam"
spam.strip("ampS")


## ASCII code or unicode of characters
ord("A")


# Copying and pasting strings with pyperclip module
import pyperclip
x = "Hello, Sushree"
pyperclip.copy(x)
pyperclip.paste()