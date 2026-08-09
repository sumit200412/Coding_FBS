#S = a + a²/2 + a³/3 + ... + a¹⁰/10

num = int(input('Enter the number : '))
sum = 0 
for i in range(1,11):
    sum = sum + (num ** i) / i
print(f'sum = {sum}')