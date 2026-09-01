words = ["eat", "tea", "tan", "ate", "nat", "bat"]
groups = {}

for w in words:
    key = ''.join(sorted(w))

    if(key not in groups):
        groups[key] = []

    groups[key].append(w)

for group in groups.values():
    print(group)