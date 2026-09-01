numbers = [2, 5, 3, 8, 4]
max = 0

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        product = numbers[i] * numbers[j]

        if(product > max):
            max = product
            a = numbers[i]
            b = numbers[j]

print("Numbers:", a, b)
print("Maximum product:", max)