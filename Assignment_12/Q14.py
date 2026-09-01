s = input("Enter a string: ")

words = s.split()

for w in words:
    count = words.count(w)
    print(w, ":", count)