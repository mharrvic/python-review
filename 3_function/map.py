# map, filter, zip and reduce

from functools import reduce


def multiply_by2(item):
    return item * 2


my_list = [1, 2, 3, 4]
your_list = [10, 20, 30]


def only_odd(item):
    return item % 2 != 0


def accumulator(acc, item):
    # print(acc, item)
    return acc + item


# filter
print(list(filter(only_odd, my_list)))
# map
print(list(map(multiply_by2, [1, 2, 3])))
# zip
print(list(zip(my_list, your_list)))
# reduce
print(reduce(accumulator, my_list, 10))
