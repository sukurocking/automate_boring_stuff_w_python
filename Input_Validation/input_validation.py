while True:
    print("Enter your age")
    age = input()
    try:
        age = int(age)
    except:
        print("Please input numeric digits")
        continue
    if age < 1:
        print("Please input positive number.")
        continue
    break

print(f"Your age is {age}")