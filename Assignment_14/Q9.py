n = [1, 2, 3, 4, 5, 6]
target = 10

for i in range(len(n)):
    for j in range(i + 1, len(n)):
        for k in range(j + 1, len(n)):
            if(n[i] + n[j] + n[k] == target):
                print(n[i], n[j], n[k])