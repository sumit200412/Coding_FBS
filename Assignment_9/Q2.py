def Digit(n):
    if(n==0):
        return 0
    else:
        return 1 + Digit(n // 10)

def arm(n ,digits):
    if(n == 0):
        return 0
    else:
        digit = n % 10
        return digit ** digits + arm(n // 10 , digit)

num = int(input("Enter the number : "))
digits = Digit(num)

if(arm(num,digits)== num):
    print(f'{num} is amrstrong number')
else:
    print(f'{num} is not amstrong number')