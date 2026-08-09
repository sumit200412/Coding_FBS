num = int(input("Enter is number : "))
fact = 1
sum = 0
for i in range(1,num+1):
    fact = fact * i
    sum = sum + fact
print(f'sum = {sum}')