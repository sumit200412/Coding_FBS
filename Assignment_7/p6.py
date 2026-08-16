k = 5
for i in range(1,k+1):
    for j in range(k-i):
        print(" ",end=" ")

    for j in range(i):
        print(i+j ,end=" ")

    for j in range(i-1,0,-1):
        print(i+j-1, end=" ")
    print()
