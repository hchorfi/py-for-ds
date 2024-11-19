import sys as sys


def check_odd_or_even(number):
    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


numbers_of_args = len(sys.argv)
if numbers_of_args == 1:
    exit()
else:
    try:
        assert numbers_of_args == 2, \
            "AssertionError: more than one argument is provided"
        try:
            number = int(sys.argv[1])
            check_odd_or_even(number)
        except ValueError:
            print("AssertionError: argument is not an integer")
    except AssertionError as error:
        print(error)
