side1 = int(input("Enter the side1 :"))
side2 = int(input("Enter the side2 : "))
side3 = int(input("Enter the side3 : "))
if(side1 == side2 and side2 == side3):
    print("It is Equilateral Triangle")
elif(side1 == side2 or side2 == side3 or side1 == side3):
    print("It is Isosceles Triangle")
else:
    print("It is scalene Triangle")