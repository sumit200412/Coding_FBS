s = input("Enter a string : ")

words = s.split()
word_count = len(words)
char_count = len(s.replace(" ", ""))

print("Number of words:", word_count)
print("Number of characters:", char_count)