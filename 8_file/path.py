try:
    with open("app/sads.txt", mode="r") as my_file:
        print(my_file.read())
except FileNotFoundError as err:
    print("file not found")
    raise err