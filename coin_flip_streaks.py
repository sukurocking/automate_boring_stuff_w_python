# Write a program to find out how often a streak of six heads 
# or a streak of six tails comes up in a randomly generated list of heads and tails.

import random
random.seed(101)
N = 100

def main():
    numberOfStreaks = 0
    for experimentNumber in range(10000):
        # Code that creates a list of 100 'heads' or 'tails' values.
        coin_list = create_coin_list(N)
        # Code that checks if there is a streak of 6 heads or tails in a row.
        for i in range(N - 6):
            if is_streak(coin_list[i : i+6]):
                numberOfStreaks += 1
                break
    print(numberOfStreaks)
    print('Chance of streak: %s%%' % (numberOfStreaks / 100))


def create_coin_list(n):
    a_coin_list = []
    for i in range(n):
        if random.randint(0,1) == 1:
            a_coin_list.append('H')
        else:
            a_coin_list.append('T')
    return a_coin_list



def is_streak(a_coin_list):
    # If the list of 6 elements can be converted to a set of 1 unique element, then it is a streak
    coin_set = set(a_coin_list)
    coin_set_length = len(coin_set)
    return coin_set_length == 1

if __name__ == "__main__":
    main()
