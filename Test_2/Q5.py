 
total = 0

for i in range(5):
    price = int(input('Enter the price of product : '))
    total = total + price

gst = total * 18 / 100
bill = total + gst 

print(f'total before gst = {total}')
print(f'gst = {gst}')
print(f'Total bill = {bill}')