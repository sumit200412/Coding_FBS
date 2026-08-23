def fact(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n * fact(n - 1)

def sos(n):
    if(n == 0):
        return 0 
    else:
        return fact(n) + sos(n - 1)
    
num = int(input("Enter the number : "))
res = sos(num)
print(f"Sum of series : {res}")