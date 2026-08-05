side1 = int(input("Enter the side1 :"))
side2 = int(input("Enter the side2 : "))
side3 = int(input("Enter the side3 : "))
if((side1 + side2 > side3)and(side2 + side3 > side1)and(side3 + side1 > side2)):
    print("Valid Triangle")
else:
    print("Invalid Triangle")