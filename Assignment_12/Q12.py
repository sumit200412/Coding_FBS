s = input("Enter a string: ")
count = 0

for n in s:
    if(n >= 'a' and n <= 'z'):
        count = count + 1

print("Lowercase characters:", count)