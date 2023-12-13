#Write a program that takes hours and minutes as input, and calculates the total number of minutes.

hour=int(input('Enter hour:'))
minute=int(input('Enter minute:'))

hourMinute=hour*60
totalMinute=minute+hourMinute
print('Total Minute is:',totalMinute)