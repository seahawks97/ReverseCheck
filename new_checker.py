# Steven Tucker
# 25 November 2018
# Update: Started a new file to make it cleaner & hopefully simpler

def main():
    while True:
        num = get_number()

        # Gets the number into a list of its integers
        # I know this is contradictory but it's a lot easier
        my_list = [int(d) for d in str(num)]
        # print(f'my list: {my_list}')
        is_palindrome = test(my_list)
        if is_palindrome is True:
            print(f'{num} is a palindrome\n')
        else:
            print(f'{num} is not a palindrome.\n')


def get_number():
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


def test(the_list):
    length = len(the_list)
    reverse = the_list[::-1]                    # Reversed
    # print(f'reversed list: {reverse}')

    for i in range(int(length // 2) + 1):
        if the_list[i] != reverse[i]:     # checks to see if a number matches to the negative index of it
            return False

    return True



main()
