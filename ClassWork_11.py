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

