def sum_series(n):
    sum = 0
    for i in range(1, n + 1):
        sum = sum + i
    return sum
n = int(input("Enter number : "))
ans = sum_series(n)
print("Sum =", ans)