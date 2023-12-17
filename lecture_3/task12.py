# A student will not be allowed to sit in exam if his/her attendance is less than 70%. Take following input from user & print percentage of class attended. Is student is allowed to sit in exam or not?
    # Number of classes held
    # Number of classes attended.


held=int(input('classes Held:'))
attended=int(input('classes attended:'))

percentOfAttended=attended/held*100

if percentOfAttended>70:
    print('go to exam hall')
else:
    print('You cannot go to exam hall')


