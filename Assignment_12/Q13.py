s = input("Enter a string: ")

letters = 0
digits = 0

for n in s:
    if((n >= 'a') and (n <= 'z') or (n >= 'A') and (n <= 'Z')):
        letters = letters + 1
    elif((n >= '0') and (n <= '9')):
        digits = digits + 1

print("Letters:", letters)
print("Digits:", digits)