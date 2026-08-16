def leap_year(year):
    if year % 4 == 0:
        return "Leap Year"
    else:
        return "Not a Leap Year"
year = int(input("Enter year: "))
print(leap_year(year))