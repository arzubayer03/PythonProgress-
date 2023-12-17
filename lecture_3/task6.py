# write a program using python to create a simple calculator.

num1=int(input('Enter Number One:'))
num2=int(input('Enter Number Two:'))
operator=input('Enter operator(+,-,*,/):')
add=num1+num2
sub=num1-num2
mul=num1*num2
div=num1/num2

if operator=='+':
    print("Addition is:",add)
elif operator== '-':
    print("Sub is:",sub)
elif operator== '*':
    print("Multi is:",mul)
elif operator== '/':
    print("Division is:",div)
else:
    print('Enter Valid Operator')
    