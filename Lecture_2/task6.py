#Write a program in that takes minutes as input, and display the total number of hours and minutes.

minute=int(input('Enter minute:'))

hour=minute//60
remainMinute=minute%60

print(hour,'Hours and',remainMinute,'Minutes.')