n = int(input("Enter the Number : "))
i = 1
while(n >= i):
    if(i % 7 == 0 and i % 5 == 0):
        print(i)
    i = i + 1