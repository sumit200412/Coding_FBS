no = int(input("Enter the number = "))
count = len(str(no))
temp = no
print(count)
arno = 0
while no > 0:          # add :
    dig = no % 10
    arno = arno + (dig ** count)
    no //= 10
if temp == arno:
    print(f"{temp} is Armstrong")
else:
    print("No is Not Armstrong")