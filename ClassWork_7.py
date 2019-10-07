#Mutable and Imutable
my_int = 14
print(id(my_int))

a = 'eqweqweq'
print(id(a))
print('\r')

x = 1
b = 1
print(id(x)), print(id(b))
print('\r')

a = [1,2,3]
b = [3,1,2]
c = [2,3,1]

print(id(a))
print(id(b))
print(id(c))
print('\r')

#Strings

# Ex:1

entr_smth = input('Enter a sign: ')

sign_is = ord("!")
count = 0

for i in entr_smth:
	if ord(i) == sign_is:
		count += 1	
		print(f'You have {count} of !' )		
	else:
		print('No matches!')	

# Ex:2
a = 'ABCDEFGH'
print(a[0])
print(a[0:5])
print('\n')

d = 'xyz'
print(d[-2])

my_str = 'space'
print(my_str[-3:-1])

#Ex:3 
a = 'abcd'
print(a.find('b'))

#Ex:4
a = 'Hello I am going to leave this place soon'
print(a.split(' '))

# String methods

my_string = 'These are some OF the python methods'
print(my_string.upper())
print(my_string.capitalize())
print(my_string.lower())
print(my_string.title())
print(my_string.replace("some", "any"))








		
