def odd():
    n = int(input("Enter the Number : "))
    sum = 0
    for i in range(1 , n+1 , 2):
        sum = sum + i
    print('sum of odd number ',sum)
odd()