n = int(input("Enter number: "))
sum = 0
fact = 1

for i in range(1,n + 1):
    fact = fact * i
    sum = sum +(i / fact)

print(f"Sum = {sum}")