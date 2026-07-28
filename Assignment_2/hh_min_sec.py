#1 Convert Time (hh, min, sec) into Seconds
hours = int(input('Enter the hours = '))
minutes = int(input('Enter the minutes = '))
seconds = int(input('Enter the seconds = '))
total_seconds = (hours * 3600) + (minutes * 60) + seconds
print('Total seconds = ',total_seconds)