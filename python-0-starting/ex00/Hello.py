ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# list (Ordered, Changeable, Allow Duplicates)
ft_list[1] = "World!"

# tuple (Ordered, Unchangeable, Allow Duplicates)
ft_tuple_to_list = list(ft_tuple)
ft_tuple_to_list[1] = "Morocco!"
ft_tuple = tuple(ft_tuple_to_list)

# set (Unordered, Unchangeable, Duplicates Not Allowed)
ft_set.remove("tutu!")
ft_set.add("BG!")

# dict (Ordered > 3.7, Changeable, Duplicates Not Allowed)
ft_dict["Hello"] = "1337!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
