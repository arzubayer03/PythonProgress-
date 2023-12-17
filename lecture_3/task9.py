# A school has following rules for grading system:
#i) Below 50 – F; ii) 50 to 60 – D; iii) 60 to 70 – C; iv) 70 to 80 – B; v) Above 80 – A
# Ask user to enter marks and print the corresponding grade.

marks=int(input('Enter  Marks:'))
if marks<50:
    print('Fail')
elif marks>=50 and marks<60:
    print('D')
elif marks>=60 and marks<70:
    print('C')
elif marks>=70 and marks<80:
    print('B')
elif marks>=80 and marks<=100:
    print('A')
else:
    print('Enter Valid number')