k = 5
for i in range(1, k + 1):
    for j in range(k - i):
        print(" ", end="")

    if i == 1:
        print(1)
    elif i == k:
        for j in range(1, k + 1):
            print(j, end=" ")
        print()
    else:
        print(1, end="")

        for j in range(2 * i - 3):
            print(" ", end="")

        print(i)