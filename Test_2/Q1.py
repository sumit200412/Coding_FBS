year = int(input('Enter the number : '))
if(year % 400 == 0):
    print(f"{year} year is Leap Year")
elif(year % 100 == 0):
    print(f'{year} year is not leap year')
elif(year % 4 == 0):
    print(f'{year} year is leap year ')
else:
    print(f'{year} is not a Leap year')