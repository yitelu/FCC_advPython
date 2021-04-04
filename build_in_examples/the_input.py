# input()	Allowing user input

"""
input(prompt=None, /)
    Read a string from standard input.  The trailing newline is stripped.

    The prompt string, if given, is printed to standard output without a
    trailing newline before reading input.

    If the user hits EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), raise EOFError.
    On *nix systems, readline is used if available.
"""

# raw_input() is not longer available in the Python3

# the input from user would always be String type


def sum_two():

    num = 0

    for i in range(2):
        num += int(input("enter your number: "))

    return num


print(sum_two())
