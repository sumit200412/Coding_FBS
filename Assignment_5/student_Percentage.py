student = int(input("Enter the Number of student : "))
total_percentage = 0
for i in range(1,student+1):
    total = 0
    print("Enter the marks of student for 5 subjects",i + 1)
    for j in range(5):
        marks = int(input('marks = '))
        total = total + marks
    per = total / 5
    print(f"percentage = {per}")
    total_percentage = total_percentage + per
average = total_percentage / student
print(f'Average Percentage = {average}')