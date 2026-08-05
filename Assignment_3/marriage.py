gender = input("Enter the gender(M/F): ")
age = int(input("Enter the age : "))
if(gender == 'F'):
    if(age >= 18):
        print("Girl is eligible for marriage")
    else:
        print("pehle padhai kar le")
else:
    if(age >= 21):
        print("Boy is eligible for marriage")
    else:
        print("pehle kama lo")