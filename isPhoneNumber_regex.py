import re
# phone_num_regex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
phone_num_regex = re.compile(r"(\d{3})-(\d{3}-\d{4})")
mo = phone_num_regex.search('Call me 415-555-1011 tomorrow, or call my office number: 415-555-9999')
print('Phone number found: ' + mo.group()) #group() method returns the match

# Printing multiple groups of the match
areacode, mainnumber = mo.groups()
print(areacode)
print(mainnumber)