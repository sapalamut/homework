import random 

# For Loops

# Ex:1
for i in range(0,10):
	print(i)

for i in range(2,17):
	print(i)

for i in range(10,11):
	print(i)

# Ex:2
for i in range(10):
	print(i)

for i in range(0,10):
	print(i)

for i in range(0,10,2):
	print(i)

for i in range(10,1,-1):
	print(i)

# Ex:3
sum  = 0

for i in range(1, 4):
	next_number = int(input('Enter number # ' + str(i) + ': ')) 
	sum += next_number
print(sum / 3)

# Ex:4
a = 'hello world'

for i in a:
	print(i)	

# Ex:5

i = 0
while i < 10:
	print(i)
	i += 1

# Ex:6

#number_of_games = int(input('Number of games'))
#for i in range(0, number_of_games):
#	hidden_number = random.randint(1,100)

#user_guess	=  0
#while not user_guess == hidden_number:

#	user_guess = int(input('Guess the number: '))

#	if user_guess > hidden_number:
#		print('Too High!')

#	elif user_guess < hidden_number:
#		print('Too Low!')

#	else:
#		print('That\'s Right!')

# Ex:7
for i in range(1, 11):
	for j in range(1, 11):
		print(i, 'times', j, 'equals', i*j)

# Ex:8
for i in range(0, 12):
	if i % 2 == 0:
		continue
	print(i)	

# Ex:9
for i in range(0, 12):
	if i % 2 == 0:
		pass
	else:	
		print(i)		

# Ex:10
string = "eqweqeretwrqweqweeqweqweqw"

for i in string:
	if i == 't':
	 	break
	print(i)			

#string = "fdfkjfkdsfnksnkndskandksanda"
#amount_of_ns = 0
#	for i in string:
#		amount_of_ns =+ 1
#	print(i)

# Ex:11

amount = int(input('Select a number: '))

count = 0
for i in range(1, amount):
	
	for j in range(2, amount):
		
		if i % j == 0 and i != j:
			break
		if j == amount -1:
			print(i)
			count += 1
print(count)				
