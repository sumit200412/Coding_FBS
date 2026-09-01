numbers = [10, 12, 15, 20, 24, 30, 36, 40, 45, 60]

m = int(input("Enter m: "))
n = int(input("Enter n: "))

print("Numbers divisible by", m, "and", n, ":")

for num in numbers:
    if num % m == 0 and num % n == 0:
        print(num)