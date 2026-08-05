num = int(input("Enter the number : "))
i = 1
sum = 0
while(i < num):
    if num % i == 0:
        sum = sum + i
    i = i + 1
if(sum == num):
    print("Perfect Number")
else:
    print("Not a Perfect Number")
