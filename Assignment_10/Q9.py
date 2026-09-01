numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_list = []
odd_list = []

for num in numbers:
    if(num % 2 == 0):
        even_list.append(num)
    else:
        odd_list.append(num)

print("Even elements:", even_list)
print("Odd elements:", odd_list)