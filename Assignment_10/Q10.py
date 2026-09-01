numbers = [10, 20, 30, 20, 40, 20, 50]

num = int(input("Enter element to remove: "))

while (num in numbers):
    numbers.remove(num)

print("List after removing:", numbers)