#! python3
# mapIt.py - Launches a map in the browser using an address from the 
# command line or clipboard


# This is what the program does
# 1. Gets a street address from the command line arguments or clipboard
# 2. Opens the webbrowser to the Google Maps page for the address

# This means your code will need to do the following:
# 1. Read the command line arguments from sys.argv
# 2. Read the clipboard contents
# 3. Call the webbrowser.open() function to open the web browser


# The script will use the command line arguments instead of the clipboard. 
# If there are no command line arguments, then the program will know to use the contents of the clipboard.

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    # Get address from command line
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard
    address = pyperclip.paste()
    
webbrowser.open("https://www.google.com/maps/place/" + address)

