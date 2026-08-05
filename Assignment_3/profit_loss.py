cost_price = int(input('Enter the cost price : '))
selling_price = int(input('Enter the selling price : '))

if(selling_price > cost_price):
    print('profit')
elif(selling_price == cost_price):
    print("No profit No loss")
else:
    print("loss") 