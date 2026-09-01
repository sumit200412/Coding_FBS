num = [2, 4, 6, 8, 10]
target = 12

for i in range(len(num)):
    for j in range(i + 1, len(num)):
        if(num[i] + num[j] == target):
            print(num[i], num[j])