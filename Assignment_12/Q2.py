s = input("Enter a string: ")
n = int(input("Enter index: "))

s = s[:n] + s[n+1:]
print("New string:", s)