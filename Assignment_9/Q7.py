def sod(n):
    if( n == 0):
        return 0
    else:
        return n % 10 + sod(n // 10)

num =int(input("Enter the number : "))
res = sod(num)
print(f'sum of digits {res}')