def highest_even(li):
    list = []
    for item in li:
        if item % 2 == 0:
            list.append(item)
    return max(list)


print(highest_even([10, 1, 2, 3, 4, 5, 6, 7, 8, 11]))
