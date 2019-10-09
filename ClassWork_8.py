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

# Ex:3
nested_tuple = ((1,2), (3,4), (5,6))

print(nested_tuple[0])
print(nested_tuple[0][0], nested_tuple[1][0])

# Ex:4
a = [1,2,3]
print(a[0])

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

