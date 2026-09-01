numbers = [10, 20, 30, 20, 40, 20, 50]
num = int(input("Enter a number: "))

if(num in numbers):
    print(num, "is present in the list")
    print("It occurs", numbers.count(num), "times")
else:
    print(num, "is not present in the list")