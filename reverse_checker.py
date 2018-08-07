# Author: Steven Tucker
# Start Date: 6 August 2018
# Purpose: See if a n-digit number evenly divides into the reverse of itself

from math import log10

def main():
    num = get_number()
    digits = get_digits(num)
    list_of_units = breakdown(num, digits)
    reverse_num = construct(list_of_units, digits)
    is_div(num, reverse_num)

def get_number():
    """This gets a whole, positive number from the user. -1 quits the program."""
    while True:
        num_in = input("Type a number (-1 to quit): ")
        try:
            num_in = int(num_in)
            if num_in == -1:
                quit(1)
            elif num_in > 0:
                return num_in
            else:
                print("Please type a positive number.")
        except ValueError:
            print("Please type a number.")


def get_digits(n):
    """This spits out the number of digits of the typed number in base 10."""
    num_dig = int(log10(n)) + 1
    print("Number of digits: " + str(num_dig))
    return num_dig


def breakdown(num, digits):
    """This breaks the number down into its base 10 components, i.e. 3 + 20 + 100 for the number 123."""
    remainders = []

    for i in range(1, digits + 1):
        rem = num % 10**i
        remainders.append(rem)
        num -= rem
    print("Powers: " + str(remainders))

    for i in range(len(remainders)):
        remainders[i] = int(remainders[i] / 10**i)
    #print(remainders)

    return remainders


def construct(ber, digits):
    """Param ber is a list, param digits is an int. This constructs the new number to be used as the divisor."""
    new_nums = []
    for i in range(len(ber)):
        new = ber[i] * 10**(digits - (i+1))
        new_nums.append(new)

    ver = 0
    for i in new_nums:
        ver += i
    print("New number: " + str(ver))
    return ver


def is_div(old, new):
    """This calculates if the higher number is divisible by the smaller number."""
    if new > old:
        higher = new
        lower = old
    else:
        higher = old
        lower = new

    print("The time has come. Is " + str(higher) + " evenly divisible by " + str(lower) + "?")

    if higher % lower == 0:
        print(str(higher) + " is evenly divisible by " + str(lower) + ".\n")
    else:
        print(str(higher) + " is NOT evenly divisible by " + str(lower) + ".\n")


while True:
    main()