# list, set, dictionary


# list
my_list = [char for char in "hello"]
my_list2 = [num for num in range(0, 100)]
my_list3 = [num ** 2 for num in range(0, 100)]
my_list4 = [num ** 2 for num in range(0, 100) if num % 2 == 0]

# print(my_list4)


# set
my_lists = {char for char in "hello"}
my_lists2 = {num for num in range(0, 100)}
my_lists3 = {num ** 2 for num in range(0, 100)}
my_lists4 = {num ** 2 for num in range(0, 100) if num % 2 == 0}

simple_dict = {"a": 1, "b": 2}
my_dict = {key: value ** 2 for key, value in simple_dict.items() if value % 2 == 0}
my_dik = {num: num * 2 for num in [1, 2, 3]}
# print(my_dict)
print(my_dik)