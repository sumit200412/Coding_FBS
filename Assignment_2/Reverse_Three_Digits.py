#10 Reverse a Three-Digit Number
num = int(input('Enter the 3 digit number = '))
digit1 = num // 100 #4
digit2 = (num // 10) % 10 
digit3 = num % 10
reverse = (digit3 * 100) + (digit2 * 10) + digit1
print("Reverse Number = ", reverse)