# Ex:1

name = input('Please enter your name: ')
birthdate = int(input('Please enter the year you were born: '))
age = 2019 - birthdate
years_100 = 100 - age
result = print(f'You will become 100 years old in {str(years_100)} years')

# Ex:2

triangle_short_side_1 = input('Enter the first side value: ')
triangle_short_side_2 = input('Enter the second side value: ')
triangle_long_side = input('Enter the third side value: ')
create_triangle = print(f'You can create a triangle {int(triangle_short_side_1) + int(triangle_short_side_2) > int(triangle_long_side) and int(triangle_short_side_1) + int(triangle_long_side) > int(triangle_short_side_2) and int(triangle_long_side) + int(triangle_short_side_2) > int(triangle_short_side_1)}')