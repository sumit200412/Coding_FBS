#3 Convert Feet and Inches into Meters and Centimeters
feet = int(input('Enter the feet = '))
inches = int(input('Enter the inches = '))
total_inches = (feet * 12) + inches
centimeters = total_inches * 2.54
meters = centimeters / 100
print('Meters = ',meters)
print('Centimeters = ',centimeters)