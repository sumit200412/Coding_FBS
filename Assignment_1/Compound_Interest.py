# 5 Compound Interest
principle=int(input('Enter the principle Amount :'))
Rate=int(input('Enter the Rate :'))
Time=int(input('Enter the time Period :'))
Amount=principle(1+Rate/100)**Time
compound_interest= Amount - principle
print('compound Interest will be =',compound_interest)