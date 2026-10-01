list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
union = []

for num in list1:
    if(num not in union):
        union.append(num)

for num in list2:
    if(num not in union):
        union.append(num)

print("Union:", union)