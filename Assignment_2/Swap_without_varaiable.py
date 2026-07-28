#9 Swap Two Numbers Without Using Third Variable
num1 = int(input('Enter the number 1 = '))
num2 = int(input('Enter the number 2 = '))
num1 = num1 + num2 
num2 = num1 - num2
num1 = num1 - num2 
print('Num1 after swapping = ',num1)
print('Num2 after swapping = ',num2)
