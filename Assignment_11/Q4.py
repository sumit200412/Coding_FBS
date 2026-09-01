numbers = [10, 40, 20, 50, 30]

for i in range(len(numbers)):
    for j in range(0, len(numbers)-i-1):
        if(numbers[j] > numbers[j+1]):
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

print("Sorted list:", numbers)
print("Second largest:", numbers[-2])