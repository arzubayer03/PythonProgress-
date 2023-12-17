# A company decided to give bonus to employees based on the following conditions:
    # i. 10% of salary if year of service is more than 5 years
    # ii. 5% of salary if year of service is more than 3 years.
    # Ask user for their salary and year of service and print the total amount.


currentSalary=int(input('Enter Current Salary: '))
year=int(input('Enter Working Year: '))

bonus10=currentSalary*10/100
bonus5=currentSalary*5/100

if year>5:
    print('Total amount is:',currentSalary+bonus10)
elif year>3:
    print('Total amount is:',currentSalary+bonus5)
else:
    print('Total amount is:',currentSalary)