# Steven Tucker
# 25 November 2018
# New, fully functional palindrome checker

def main():
    while True:
        # gets string and integer numbers
        num = get_number()
        int_num = int(num)

        # Gets the number into a list of its integers, and a reversed, usable list
        my_list = [int(d) for d in str(num)]
        reversed_list = my_list[::-1]

        is_palindrome = test_is_palindrome(my_list, reversed_list)               # True/False
        palindrome_num = get_num_palindrome(reversed_list)                       # int

        high = max(int_num, palindrome_num)
        low = min(int_num, palindrome_num)

        if is_palindrome is True:
            print(f'{num} is a palindrome.')
        else:
            print(f'{num} is not a palindrome.')

        # Plurality
        if high // low == 1:
            s = ''
        else:
            s = 's'

        if high % low == 0:
            print(f'{high} is divisible by {low} {int(high/low)} time{s} with no remainder.\n')
        else:
            print(f'{high} is divisible by {low} {high//low} time{s} with remainder {high % low}.\n')


def get_number():
    """Prompt for user to input number. Takes no args. If -1, program quits.
    Returns a positive number, retries otherwise"""
    while True:
        num = input('Please type a number to check if it is a palindrome, or -1 to quit: ')
        # Validate to make sure it's a number
        try:
            num2 = int(num)
            if num2 > 0:
                return num
            elif num2 == -1:
                input('Press Enter to quit')
                exit(0)
            else:
                print('Please type a positive number.\n')

        except ValueError:
            print('Please type a number.\n')


def test_is_palindrome(l1, l2):
    """Takes original list and reversed list as args. Returns False if any value does not match counterpart,
    True otherwise."""
    # print(f'reversed list: {rev_list}')
    for i in range(int(len(l1) // 2) + 1):
        if l1[i] != l2[i]:     # checks to see if a number matches to the negative index of it
            return False

    return True


def get_num_palindrome(rev_list):
    """Takes reversed list as arg. Returns the palindrome number."""
    total = 0
    # Convert to integer
    for i in range(len(rev_list)):
        total += rev_list[i] * (10 ** (len(rev_list) - i))

    return int(total / 10)


main()