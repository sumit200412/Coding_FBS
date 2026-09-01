words = ["flower", "flow", "flight"]
prefix = words[0]

for w in words:
    while(not w.startswith(prefix)):
        prefix = prefix[:-1]

print("Longest common prefix:", prefix)