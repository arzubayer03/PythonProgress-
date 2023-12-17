# A student will not be allowed to sit in exam if his/her attendance is less than n%. Take following input from user & print percentage of class attended. Is student is allowed to sit in exam or not?
    # Number of classes held
    # Number of classes attended
    # Value of n%


held=int(input('classes Held:'))
attended=int(input('classes attended:'))

percent=int(input('Enter percent: '))
percentOfAttended=attended/held*100

if percentOfAttended>percent:
    print('go to exam hall')
else:
    print('You cannot go to exam hall')



print(percentOfAttended)