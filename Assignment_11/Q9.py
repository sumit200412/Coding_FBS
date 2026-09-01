num = [1, 2, 3, 4, 5]

squares = []
cubes = []

for n in num:
    squares.append(n * n)
    cubes.append(n * n * n)

print("Numbers:", num)
print("Squares:", squares)
print("Cubes:", cubes)