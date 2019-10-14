# Lists and Tuples

# Ex:1
a = (1, 2)

print(a[0], a[1])

# Ex:2
def tuple():
	user_name = input("Enter you name: ")
	user_surname = input("Enter your surname: ")

	return user_name, user_surname

user_info = tuple()

print("Your name is " + user_info[0])
print("Your surname is " + user_info[1])
print('\n')

# Ex:3
nested_tuple = ((1,2), (3,4), (5,6))

print(nested_tuple[0])
print(nested_tuple[0][0], nested_tuple[1][0])
print('\n')

# Ex:4
a = [1,2,3]
print(a[0])
print('\n')

# Ex:5
my_list = [1, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]

my_list.remove(23)
print(my_list, ": After removing 23")

my_list.sort()
print(my_list, ": After sorting")

my_list.reverse()
print(my_list, ": After reversing")

my_list.pop()
print(my_list, ": Popping")

del my_list[-5:]
print(my_list, ": After deleting the last five elements")
print('\n')

# Ex:6
my_list = [1, 2, 3, 4]

my_list.append(5)
print(my_list, ": After appending five")

new_list = [6, 7, 8]
my_list.extend(new_list)
print(my_list, ": After extending")

my_list.insert(0,0)
print(my_list, ": After inserting zero")
print('\n')

# Ex:7
def average(in_list):
	sum = 0
	for number in in_list:
		sum += number
	return sum / len(in_list)

my_list1 = [1, 2, 3, 4, 5, 6, 7]
my_list2 = [91, 92, 93, 94, 95, 96, 97]

print("The average of my_list1 is:", average(my_list1))
print("The average of my_list2 is:", average(my_list2))
print('\n')

# Ex:8 Same with Indexing
def average(in_list):
	sum = 0
	for i in range(0, len(in_list)):
		sum += in_list[i]
	return sum / len(in_list)

my_list1 = [1, 2, 3, 4, 5, 6, 7]
my_list2 = [91, 92, 93, 94, 95, 96, 97]

print("The average of my_list1 is:", average(my_list1))
print("The average of my_list2 is:", average(my_list2))
print('\n')

# Ex:9
def two_average(in_2d_list):
	result = []

	for num_list in in_2d_list:
		sum = 0
		for number in num_list:
			sum += number

		result.append(sum / len(num_list))

	return result

my_2d_list = [[61, 32, 12, 123], [123, 131, 131, 123], [4, 1, 2]]

print("averages:", two_average(my_2d_list))

# Ex:10
def lists(my_list):
	big = 0
	for i in my_list:
		if i > big:
			big	= i
list_one = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(f'The biggest number is {big}')

# Ex:11
new_list = [1, 2, 3, 4, 5, 6, 7, 7, 3, 3, 2, 2, 8, 9, 0]
empty = []
for i in new_list:
	if i not empty:
		empty.append(i)
print(new_list)		
























