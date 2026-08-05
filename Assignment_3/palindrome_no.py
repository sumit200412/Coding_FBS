num = int(input("Enter the 3 digit number : "))
first = num // 100
last = num % 10
if(first == last):
    print("Number is palindrome")
else:
    print("Number is not Palindrome")


