from math import pi
from datetime import datetime

# Ex:1

number = int(input('Enter EVEN or ODD number please: '))
entered_number = (number % 2 == 1)
print(f'If the number is ODD it\'s False, if the number is EVEN it\'s True: {entered_number}')

# Ex:2

circle_radius = float(input('Enter the radius number: '))
print(f'The area of the circle with radius is: {(pi * circle_radius ** 2)}')

# Ex:3

time_now = datetime.now()
print(f'Current time is: {time_now}')