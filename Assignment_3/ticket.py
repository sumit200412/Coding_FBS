total = 0
for i in range(5):
    age = int(input("Enter Age: "))
    ticket = float(input("Enter Ticket Amount: "))
    if age < 12:
        ticket = ticket - (ticket * 30 / 100)
    elif age > 59:
        ticket = ticket - (ticket * 50 / 100)
    total = total + ticket
print("Total Ticket Amount =", total)