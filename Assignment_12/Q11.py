s = input("Enter a string: ")

for n in s:
    if(n == " "):
        s = s.replace(" ", "-")
print(s)