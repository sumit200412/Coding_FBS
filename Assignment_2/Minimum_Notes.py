#11 Minimum Number of Notes
amount = int(input('Enter the Amount = '))
notes2000 = amount // 2000
amount = amount % 2000
notes500 = amount // 500
amount = amount % 500
notes200 = amount // 200
amount = amount % 200
notes100 = amount // 100
amount = amount % 100
notes50 = amount // 50
amount = amount % 50
notes20 = amount // 20
amount = amount % 20
notes10 = amount // 10
amount = amount % 10
notes5 = amount // 5
amount = amount % 5
notes2 = amount // 2
amount = amount % 2
notes1 = amount // 1
amount = amount % 1

print('Notes 2000 = ',notes2000)
print('Notes 500 = ',notes500)
print('Notes 200 = ',notes200)
print('Notes 100 = ',notes100)
print('Notes 50 = ',notes50)
print('Notes 20 = ',notes20)
print('Notes 10 = ',notes10)
print('Notes 5 = ',notes5)
print('Notes 2 = ',notes2)
print('Notes 1 = ',notes1)
total_notes = notes2000+notes500+notes200+notes100+notes50+notes20+notes10+notes5+notes2+notes1
print('minimum number of notes = ',total_notes)