sub1 = int(input("Enter the sub1 marks : "))
sub2 = int(input("Enter the sub2 marks : "))
sub3 = int(input("Enter the sub3 marks : "))
sub4 = int(input("Enter the sub4 marks : "))
sub5 = int(input("Enter the sub5 marks : "))
total_marks = sub1+sub2+sub3+sub4+sub5
perc = total_marks/5
print(perc)
if(perc >= 90):
    print("First class ")
elif(perc >= 80):
    print("Second class")
elif(perc < 35):
    print("Fail")
else:
    print("Third class")