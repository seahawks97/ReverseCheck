# ReverseCheck v3.0
This program checks to see if a number you type is a palindrome (can be read the same forwards and backwards). It takes the higher of the two numbers, and tells if it is evenly divisble by the other. If it's not, it tells the number of times it is divisible with the remainder.
### Use It
Download *new_checker.py*, run it, and type a number. Type -1 to quit.
### How It Works
Prompt user for input. Verifies that it is an integer. Constructs a list with the digits, and a reversed list from that. Checks to see if it is a palindrome by comparing the values at each index to the other list. If it matches correctly, it is indeed a palindrome. Then, it prints a statement that says, "*YOUR NUMBER* is/is not a palindrome." It checks if the higher number divided by the lower is 1, and if it is, it makes the number of "times" statement singular. It is plural if not. It prints the statement, "*HIGHER* is divisible by *LOWER* *BLANK* times with remainder *REMAINDER*." This is in a While loop, so it continues to prompt for a number via input until you type "-1" to quit the program.
