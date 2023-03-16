# collatz
# Write a function named collatz() that has one parameter named number. 
# If number is even, then collatz() should print number // 2 and return this value. 
# If number is odd, then collatz() should print and return 3 * number + 1.

def main():
    while True:
        try:
            num = int(input("Number: \n"))
            collatz(num)
            break
        except ValueError:
            print("Please enter a number.")
            continue

def collatz(number):
    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = 3 * number + 1
        print(number)

if __name__ == "__main__":
    main()
