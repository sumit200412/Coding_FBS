num = [1, 2, 3, 4, 5, 6, 7, 8]

even = []
odd = []

for x in num:
    if x % 2 == 0:
        even.append(x)
    else:
        odd.append(x)

print("Even list:", even)
print("Odd list:", odd)