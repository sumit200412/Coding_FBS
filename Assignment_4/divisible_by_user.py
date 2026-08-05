n = int(input("Enter the range : "))
div = int(input("Enter the diviser : "))
i = 1
while(n >= i):
    if(i % div == 0):
        print(i)
    i = i + 1