# Dictionaries
human = {'name': 'Jirayr', 'surname': 'Melikyan', 'age': 19, 'is_married': False}
print(human['name'], human['surname'], human['is_married'])

#adding
human['age'] = 30

#changing
human['have_pet'] = False

#deleting
del human['age']

print(human)

for value in human.values():
	print(value)

print(human.keys())
print(human.values())

# Ex:1
fruits = {'apple': 5, 'orange': 14, 'pinapple': 1, 'banannas': 4, 'pomegranade': 16}

for key in fruits.keys():
	if fruits[key] > 5:
		print(key)

# Ex:2
python_students = {
	'Gor Smbatyan': 26, 'David Grigoryan': 26, 'Vardges Hovhannisyan': 26, 
	'Rafayel Kostanyan': 28, 'Khachatur Khachatryan': 23, 'Marat Yarumyan': 24, 
	'Artur Altunyan': 23, 'Sedrak Harutyunyan': 24, 'Marianna Beglaryan': 25, 
	'Vardges Davtyan': 28, 'Tigran Danielyan': 28, 'Gevorgyan Arno': 23, 
	'Arthur Ananyan': 29, 'Arman Babayan': 28

}

python_students['Arman Babayan'] = 15
python_students['Vardges Davtyan'] = 30

print(python_students.keys())
print(python_students.values())

# Ex:3
classes = {
	'Math': ['David', 'Lucy', 'Dana'],
	'Physics': ['Addison', 'Benjamin'],
	'Chemistry': ['Sara', 'Pele']
}

print('Students in math class', classes['Math'])

classes['Math'].append('Jirayr')


print('Students in math class', classes['Math'])

# Ex:4


