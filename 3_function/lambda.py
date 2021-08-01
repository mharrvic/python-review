# lambda
# one time anonymous function
# automatically return

from functools import reduce

my_list = [1, 2, 3, 4]

print(list(map(lambda item: item * 2, my_list)))

print(reduce(lambda acc, item: acc + item, my_list))