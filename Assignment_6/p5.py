for i in range(5):
    k=1
    for j in range(i+1):
        print(k,end=" ")
        k=k*(i-j)//(j+1)

    print()