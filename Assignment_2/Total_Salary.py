#6 Calculate Total Salary
basic = int(input('Enter the basic salary = '))
da = basic * 10 / 100
ta = basic * 12 / 100
hra = basic * 15 / 100
total_salary = (basic + da + ta + hra)
print('da = ',da)
print('ta = ',ta)
print('hra = ',hra)
print('Total salary = ',total_salary)