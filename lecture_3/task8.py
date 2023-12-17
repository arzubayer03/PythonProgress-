# A shop will give discount of 10% if the cost of purchased quantity is more than 1000.

quantity=int(input('Enter Quantity:'))
price=int(input('Enter Price:'))

cost=price*quantity
discount=cost*10/100

if cost>=1000:
    print('With 10% discount your price is',cost-discount)
else:
    print('price is',cost)