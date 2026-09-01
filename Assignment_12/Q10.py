s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

count1 = 0
count2 = 0

for n in s1:
    count1 = count1 + 1

for n in s2:
    count2 = count2 + 1

if count1 > count2:
    print("Larger string:", s1)
else:
    print("Larger string:", s2)