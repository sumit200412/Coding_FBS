#5 Selling Price of Book
cost_price = int(input('Enter the cost price = '))
discount = int(input('Enter the discount(%) = '))
discount_amount = (cost_price * discount) / 100
selling_price = cost_price - discount_amount
print('selling price is = ',selling_price)