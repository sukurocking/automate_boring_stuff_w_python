# This program counts the number of instances of each character in a given string
import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message: 
    count.setdefault(character, 0) # This sets a default for a key, if it does not exist in the dictionary
    count[character] = count[character] + 1
pprint.pprint(count)
