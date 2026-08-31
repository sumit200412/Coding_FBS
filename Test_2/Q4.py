length = int(input("Enter the length :"))
breadth = int(input("Enter the breadth :"))
height = int(input('Enter the Height : '))
rate = int(input('Enter the rate for per sq.m : '))

area = 2 *(length + breadth)*height

cost = area * rate

print(f"area of four wall = {area}")
print(f"total painting cost = {cost}")