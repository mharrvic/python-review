# Error Handling

while True:
    try:
        age = int(input("what is your age? "))
        10 / age
        # raise Exception("hey cut it out")
    except ValueError as err:
        print(f"please enter a number: {err}")
        continue
    except ZeroDivisionError:
        print("please enter age higher than 0")
        break
    else:
        print("thank you!")
        break
    finally:
        print("ok, i am finally done")
    print("can you hear me?")
