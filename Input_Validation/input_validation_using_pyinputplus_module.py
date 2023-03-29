import pyinputplus as pyip
response = pyip.inputNum()

response = input("Enter a number: ")
response 

response = pyip.inputInt(prompt="Enter a number: ")

response = pyip.inputNum("Enter num: ", min = 4)
# Number must be at minimum 4.

response = pyip.inputNum(limit=2)

response = pyip.inputNum(limit=2,default="N/A")

# Validation for Roman numerals
response = pyip.inputNum(allowRegexes=[r"(I|V|X|L|C|D|M)+", r"zero"])
response = pyip.inputNum(allowRegexes=[r"(i|v|x|l|c|d|m)+", r"zero"])

# Below code doesnt accept even numbers
response = pyip.inputNum(blockRegexes=[r"[02468]$"])

# Specifying both allowRegexes and blockRegexes paramaters
response = pyip.inputStr(allowRegexes=[r"caterpillar", r"category"], blockRegexes=[r"cat"])


# InputCustom 
def adds_up_to_ten(numbers):
    numbers_list = list(numbers)
    for i, digit in enumerate(numbers_list):
        numbers_list[i] = int(digit)
    if sum(numbers_list) != 10:
        raise Exception("The digits must add up to 10, not %s", (sum(numbers_list)))
    return int(numbers) #Return an int form of numbers

response = pyip.inputCustom(adds_up_to_ten)
    