D = [2000, 500, 200, 100, 50, 20, 10, 5]
amount = int(input("enter amount: "))
count = 0

for note in D:
    n = amount // note
    if(n > 0):
        print(note, ":", n)
        count = count + n
        amount = amount % note

print(f"Minimum number of notes = {count}")