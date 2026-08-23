def prime(n, i):
    if(n < 2):
        return False

    elif( i * i > n):
        return True

    elif(n % i == 0):
        return False

    else:
        return prime(n, i + 1)
    
num = int(input("Enter the number : "))

if prime(num, 2):
    print(f"{num} is prime number")
else:
    print(f"{num} is not a prime number")