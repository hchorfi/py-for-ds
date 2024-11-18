import sys

def get_input() -> str:
    try:
        arg = input("What is the text to count?\n")
        arg += "\n"
        return arg
    except EOFError:
        pass

def count_input(input):
    count_upper = 0
    count_lower = 0
    count_digit = 0
    count_punct = 0
    count_space = 0
    print(f'The text contains {len(input)} characters:')
    for char in input:
        if char.isspace(): count_space += 1
        elif char.isupper() : count_upper += 1
        elif char.islower() : count_lower += 1
        elif char.isdigit() : count_digit += 1
        elif char.isprintable() : count_punct += 1
    print(f'{count_upper} upper letters')
    print(f'{count_lower} lower letters')
    print(f'{count_punct} punctuation marks')
    print(f'{count_space} spaces')
    print(f'{count_digit} digits')

def main():
    try:
        numbers_of_args = len(sys.argv)
        assert numbers_of_args <= 2, "AssertionError: more than one argument is provided"
        if numbers_of_args == 1:
            input = get_input()
        elif numbers_of_args == 2:
            input = sys.argv[1]
        count_input(input)
    except Exception as error:
        print(Exception.__name__ + ":", error)

if __name__ == "__main__":
    main()