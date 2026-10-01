n = int(input("enter number: "))
count = 0
num = 2

while(count < n):
    i = 2
    k = 0

    while(i < num):
        if num % i == 0:
            k = 1
            break
        i = i + 1

    if(k == 0):
        print(num, end=" ")
        count = count +1

    num = num + 1