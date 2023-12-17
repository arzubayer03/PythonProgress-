#  Take input of age of 3 people by user and determine oldest and youngest among them.

Person1=int(input('Enter age of Person 1: '))
Person2=int(input('Enter age of Person 2: '))
Person3=int(input('Enter age of Person 3: '))

oldest=0
if oldest<Person1:
    oldest=Person1
if oldest<Person2:
    oldest=Person2
if oldest<Person3:
    oldest=Person3
    
print('Oldest person is',oldest)


youngest=Person1
if youngest>Person2:
    youngest=Person2
if youngest>Person3:
    youngest=Person3
    
print('Youngest person is',youngest)