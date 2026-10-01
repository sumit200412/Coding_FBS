n = int(input("Enter number of employees: "))
total_salary = 0

for i in range(1,n + 1):

    basic = int(input("Enter basic salary: "))

    if(basic < 20000):
        da = basic * 10 / 100
        ta = basic * 12 / 100
        hra = basic * 15 / 100
    else:
        da = basic * 15 / 100
        ta = basic * 18 / 100
        hra = basic * 20 / 100

    salary = basic + da + ta + hra

    print("Employee", i)
    print("Basic Salary =", basic)
    print("DA =", da)
    print("TA =", ta)
    print("HRA =", hra)
    print("Total Salary =", salary)
    print()

    total_salary = total_salary + salary

print(f"Total Salary of all employees = {total_salary}")