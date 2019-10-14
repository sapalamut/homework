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
info_data = {
	"worker": ['David', 'Mcloud'],
	"age": [21,]
}

print('Workers info is', info_data['worker'])
info_data['age'].append(50)

print('Workers age is', info_data['age'])

# Ex:5
sample_text = 'Far far away behind the word mountains far from the countries Vokalia and Consonantia there live the blind texts Separated they live in Bookmarksgrove right at the coast of the Semantics a large language ocean A small river named Duden flows by their place and supplies it with the necessary regelialia It is a paradisematic country in which roasted parts of sentences fly into your mouth Even the all powerful Pointing has no control about the blind texts it is an almost unorthographic life One day however a small line of blind text by the name of Lorem Ipsum decided to leave for the far World of Grammar The Big Oxmox advised her not to do so because there were thousands of bad Commas'

word_dict = {}

sample_text = sample_text.lower()
sample_text = sample_text.split(' ')

for word in sample_text:
	if word in word_dict.keys():
		word_dict[word] += 1
	else:
		word_dict[word] = 1


for (word, amount) in word_dict.items():
	if amount > 2:
		print(word, ":", amount)			














