unit = int(input("Enter the units : "))
if(unit <= 50):
    total = unit*0.5  
    print(total+(total*2/10))
elif(unit <= 150):
    total = (50*0.5)+(unit-50)*0.75 
    print(total+(total*2/10))
elif(unit <= 250):
    total = (50*0.5)+(100*0.75)+(unit-150)*1.20
    print(total+(total*2/10))
else:
    total = (50*0.5)+(100*0.75)+(100*1.20)+(unit-250)*1.50
    print(total+(total*2/10))


