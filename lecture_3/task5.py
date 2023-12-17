# Write a program to find the smallest of three numbers.

num1=int(input('Enter Number One:'))
num2=int(input('Enter Number Two:'))
num3=int(input('Enter Number Three:'))
smal=0
if num1>smal:
    smal=num1
if num2<smal:
    smal=num2
if num3<smal:
    smal=num3
print(smal)