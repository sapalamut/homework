# Conditionals

# Sample:1
a = 3
b = 4
if a > b:
	print(True)
if a < b:
	print(False)

# Sample:2
c = True
b = False
if c == True:
	print(not False)
else:
	print(True)	

# Sample:3
num_one = (15 + 15)
num_two = (20 - 10)
if num_one > num_two:
	print(True)
else:
	print(False)

# Sample:4
age = 37
name = 'Arman'
if name == 'Arman'and age == 37:
	print(f'Your name is {name} and your age is {age}')
else:
	print('Who are you???')

# Sample:5
weather = 'sunny'
condition = not False
random = 'lencheck'
len_of = len(random)
print(len_of)
if weather == 'sunny':
	print(f'Yeah it\'s{weather} outside!')
	if condition == True:
		print(f'So {condition}')

# Sample:6
soccer_team = 11
weather = 'good'
if soccer_team == 12 and weather == 'good':
	print('Yes we are playing')
else:
	print('We are not')

# Sample:7
a = 1
b = 2
c = 3

if a > b:
	print(False)
elif b > c:
	print(False)
else:
	print("None of the answers is true")

# Sample:8
num_enter = int(input('please enter a number: '))
if num_enter <= 0:
	print('Negatine')
else:
	print('Positive')	

# Sample:9
ent_tempo =int(input('Enter the temperature outside: '))
weather_1 = 45
weather_2 = 35
weather_3 = 20
weather_4 = 0
if ent_tempo >= weather_1:
	print('It\'s very hot take off all your clothes')
elif ent_tempo <= weather_2:
	print('It\'s OK you can stay in t shirt')
elif ent_tempo <= weather_3:
	print('It"s getting cold put some clothes on')
else:
	ent_tempo <= weather_4
	print('You are going to die, it\'s very cold')			  