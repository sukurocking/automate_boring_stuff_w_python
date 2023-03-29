# # Matching multiple groups with pipe
import re
# # hero_regex = re.compile(r"Batman|Tina Fey")
# # mo1 = hero_regex.search("Batman and Tina Fey")
# # print(mo1.group())
# # # mo1 = hero_regex.findall("Batman and Tina Fey")
# # # print(mo1)

# # bat_regex = re.compile(r"Bat(man|mobile|copter|bat)")
# # mo = bat_regex.search("Batmobile lost a wheel")
# # print(mo.group())
# # print(mo.group(1))

# # Optional matching with the question mark
# # bat_regex = re.compile(r"Bat(wo)?man") # wo is an optional group
# # # ? says: Match zero or one of the group preceding this question mark
# # mo1 = bat_regex.search("The Adventures of Batman")
# # mo1.group()
# # mo2 = bat_regex.search("The Adventures of Batwoman")
# # mo2.group()

# # Matching zero or more with the star
# # bat_regex = re.compile(r"Bat(wo)*man")
# # mo1 = bat_regex.search("The Adventures of Batman")
# # mo1.group()
# # mo2 = bat_regex.search("The Adventures of Batwoman")
# # mo2.group()
# # mo3 = bat_regex.search("The Adventures of Batwowoowman") 
# # mo3.group() # This results in attribute error since the above search was not successful (It consists of a spelling mistake of "wo" pattern)

# # Matching One or More with the Plus
# # bat_regex = re.compile(r"Bat(wo)+man")
# # mo1 = bat_regex.search("The Adventures of Batman")
# # mo1.group() # Now this results in AttributeError, since the above search was not successful.
# # # It does not consist of one or more patterns of (wo) group
# # mo2 = bat_regex.search("The Adventures of Batwoman")
# # mo2.group()
# # mo3 = bat_regex.search("The Adventures of Batwowoman")
# # mo3.group()


# # Matching Specific Repetitions with Braces
# # ha_regex = re.compile(r"(Ha){3}")
# # mo1 = ha_regex.search("HaHaHa")
# # mo1.group()


# # ha_regex1 = re.compile(r"(Ha){3,5}") # This will match 3 repetitions, 4 repetitions & 5 repetitions of Ha
# # mo2 = ha_regex1.search("HaHaHa")
# # mo2.group()
# # mo3 = ha_regex1.search("HaHaHaHa")
# # mo3.group()
# # mo4 = ha_regex1.search("Ha")
# # mo4 == None


# # Greedy and Non-greedy Matching
# # Python regular expressions are greedy by default
# # greedy_ha_regex = re.compile(r"(Ha){3,5}")
# # mo1 = greedy_ha_regex.search("HaHaHaHaHa")
# # mo1.group()

# # nongreedy_ha_regex = re.compile(r"(Ha){3,5}?")
# # mo2 = nongreedy_ha_regex.search("HaHaHaHaHa")
# # mo2.group()


# # The findall() method
# # phone_num_regex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d") # has no groups
# # mo = phone_num_regex.search('Cell: 415-555-9999 Work: 212-555-0000')
# # mo.group()

# # phone_num_regex.findall('Cell: 415-555-9999 Work: 212-555-0000')

# # phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups
# # phone_num_regex.findall('Cell: 415-555-9999 Work: 212-555-0000')


# #### Character Classes ####
# xMasRegex = re.compile(r"\d+\s\w+")
# xMasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, \
#                    7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')


# #### Making Your Own Character Classes ####
# # Matching vowels
# vowel_regex = re.compile(r"[aeiouAEIOU]")
# vowel_regex.findall('RoboCop eats baby food. BABY FOOD.')


# # Matching ranges of characters
# # [a-zA-Z0-9] will match all lowercase letters, uppercase letters, and numbers.

# consonant_regex = re.compile(r"[^aeiouAEIOU]")
# consonant_regex.findall('RoboCop eats baby food. BABY FOOD.')


# ## The Caret and Dollar Sign Characters
# # ^ indicates "starting with"
# # $ indicates "ending with"
# begins_with_hello = re.compile(r"^Hello")
# mo = begins_with_hello.search("Hello, world!")
# mo.group()

# ends_with_number = re.compile(r"\d$")
# mo = ends_with_number.search("Your number is 42")
# mo.group()

# # Checking if whole string is num
# whole_string_num = re.compile(r"^\d+$")
# whole_string_num.search("12345678")
# whole_string_num.search('12345xyz67890') == None
# print(whole_string_num.search('12345xyz67890'))


# ## The Wildcard Character
# # .(or dot) character will match any character except for a newline
# at_regex = re.compile(r".at")
# at_regex.findall('The cat in the hat sat on the flat mat.')


# #### Matching Everything with Dot-Star ####
# # the dot character means “any single character except the newline,” and 
# # the star character means “zero or more of the preceding character.”
# name_regex = re.compile(r"First Name: (.*) Last Name: (.*)")
# mo = name_regex.search("First Name: Sukumar Last Name: Subudhi")
# # mo.group()
# mo.group(1)
# mo.group(2)


# # Using dot star in a non-greedy fashion
# nongreedyRegex = re.compile(r'<.*?>')
# mo = nongreedyRegex.search('<To serve man> for dinner>')
# mo.group()

# greedyRegex = re.compile(r"<.*>")
# mo = greedyRegex.search('<To serve man> for dinner>')
# mo.group()


# # Matching Newlines with the Dot Character
# # Using the 2nd parameter
# no_new_line_regex = re.compile(".*")
# no_new_line_regex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()

# new_line_regex = re.compile(".*", re.DOTALL)
# new_line_regex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()


# # Case-Insensitive Matching
# robocop = re.compile(r"robocop", re.IGNORECASE)
# robocop.search("RoboCop is part man, part machine, all cop.").group()
# robocop.search("ROBOCOP protects the innocent.").group()


# Substituting Strings with the sub() Method
# namesRegex = re.compile(r'Agent \w+')
# namesRegex.sub("CENSORED", "Agent Alice gave the secret documents to Agent Bob")

# agent_names_regex = re.compile(r"Agent (\w)\w*")
# agent_names_regex.sub(r"\1****", "Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent")


# Managing Complex Regexes
# Using verbose mode
# phone_num_regex = re.compile(r"""(
#     (\d{3}|\(\d{3}\))?                     # area code
#     (\s|-|\.)?                             # separator
#     \d{3}                                  # first 3 digits
#     (\s|-|\.)                              # separator
#     \d{4}                                  # last 4 digits
#     (\s*(ext|x|ext.)\s*\d{2,5})?           # extension
#     )""", re.VERBOSE)


# num_regex = re.compile(r"\d+")
# num_regex.sub("X", "12 drummers, 11 pipers, five rings, 3 hens") == "X drummers, X pipers, five rings, X hens"


# Write a regex that matches a number with commas for every three digits? It must match the following:

# '42'
# '1,234'
# '6,368,745'
# but not the following:

# '12,34,567' (which has only two digits between the commas)
# '1234' (which lacks commas)


# valid_numbers = ['42', '1,234', '6368,745']
# invalid_numbers = ['12,34,567', '1234']

# num_regex = re.compile(r"^\d{1,3}(,\d{3})*$")

# for number in valid_numbers + invalid_numbers:
#     match = num_regex.match(number)
#     if match:
#         print(f"{number} is valid")
#     else:
#         print(f"{number} is invalid")


# How would you write a regex that matches a sentence where the first word is either 
# Alice, Bob, or Carol; the second word is either eats, pets, or throws; 
# the third word is apples, cats, or baseballs; 
# and the sentence ends with a period? This regex should be case-insensitive. 

# It must match the following:

# 'Alice eats apples.'
# 'Bob pets cats.'
# 'Carol throws baseballs.'
# 'Alice throws Apples.'
# 'BOB EATS CATS.'

# but not the following:

# 'RoboCop eats apples.'
# 'ALICE THROWS FOOTBALLS.'
# 'Carol eats 7 cats.'

valid_strings = ['Alice eats apples.', 'Bob pets cats.', 'Carol throws baseballs.',\
                 'Alice throws Apples.', 'BOB EATS CATS.']
invalid_strings = ['RoboCop eats apples.', 'ALICE THROWS FOOTBALLS.', 'Carol eats 7 cats.']

pattern = re.compile(r"""(
                     ^(Alice|Bob|Carol)             # First word
                     \s                             # Space between words
                     (eats|pets|throws)             # Second word
                     \s                             # Space between words
                     (apples|cats|baseballs)        # Third word
                     \.$                            # End of sentence
                    ) """, re.IGNORECASE | re.VERBOSE)

for sentence in valid_strings + invalid_strings:
    match = pattern.match(sentence)
    if match:
        print(f"The sentence is valid:\t{sentence}")
    else:
        print(f"The sentence is invalid:\t{sentence}")