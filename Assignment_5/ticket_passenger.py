num = int(input('enter the number : '))
cost = int(input('enter the cost : '))
total = 0

for i in range(num):
    age = int(input('Enter the age : '))

    if(age < 12):
        ticket = cost -(cost * 30/100)
    elif(age > 59):
        ticket = cost -(cost * 50/100)
    else:
        ticket = cost
    print(f'Ticket amount : {ticket}')
    total = total + ticket 
    print(f'Total ticket cost : {total} ') 
