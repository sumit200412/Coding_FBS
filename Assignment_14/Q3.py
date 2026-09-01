words = ["cat", "dog", "cat", "bird", "dog", "cat"]
unique = set(words)

for w in unique:
    print(w, ":", words.count(w))