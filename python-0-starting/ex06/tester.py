from ft_filter import ft_filter


def fun(variable):
    '''
    Check if variable is a vowel
    '''
    letters = ['a', 'e', 'i', 'o', 'u']
    if (variable in letters):
        return True
    else:
        return False


#  sequence
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']

#  using filter function
filtered = filter(fun, sequence)
ft_filtered = ft_filter(fun, sequence)

print('The filtered letters are:')
for s in filtered:
    print(s)

print('The ft_filtered letters are:')
for s in ft_filtered:
    print(s)

original = filter.__doc__
copy = ft_filter.__doc__
print(copy)  # output: docstring
print(original == copy)  # output: True
