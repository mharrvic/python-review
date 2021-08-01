some_lists = ["a", "b", "c", "d", "d", "e", "f", "g", "g", "h"]

duplicates = list(set([item for item in some_lists if some_lists.count(item) > 1]))

print(duplicates)