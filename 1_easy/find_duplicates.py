some_lists = ['a', 'b', 'c', 'd', 'd', 'e', 'f', 'g', 'g', 'h']

duplicates = []
for item in some_lists:
    if some_lists.count(item) > 1:
        if item not in duplicates:
            duplicates.append(item)
print(duplicates)