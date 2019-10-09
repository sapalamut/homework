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
print(nested_tuple[0][0])
