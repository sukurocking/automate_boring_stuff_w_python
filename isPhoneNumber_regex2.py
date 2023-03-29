import re

phone_number_regex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phone_number_regex.search("My number is (415) 555-4242.")
print(type(mo))
print(mo.group())