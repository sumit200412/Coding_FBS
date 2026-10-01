for i in range(11):
    if i == 0:
        print("*" * 23)
    elif i == 10:
        print("*" * 23, "*")

    else:
        print(" " * (22 - i) + "*")