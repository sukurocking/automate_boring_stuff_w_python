# comma code
spam = ['apples', 'bananas', 'tofu', 'cats']
# spam = []
'''
Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, 
with and inserted before the last item. 
For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'. 
But your function should be able to work with any list value passed to it. Be sure to test the case where an empty list [] is passed to your function.
'''
try:
    complete_string = spam[0]
except IndexError:
    print("Empty list")
else: 
    # complete_string = spam[0]
    for list_index, list_item in enumerate(spam):
        if 1 <= list_index < len(spam)-1:
            complete_string = complete_string + ', ' + list_item
        else:
            complete_string + ' and ' + list_item
    print(complete_string)
