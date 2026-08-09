num = int(input("Enter the number  : "))
temp = 1
sum = 0
for i in range(1,num+1):
    sum = sum + temp 
    temp = temp * 2
print(f'sum = {sum}')