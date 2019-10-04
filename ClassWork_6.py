# Exception handling
try:
	1 / 0
except:
	print('error occured')

# Ex1.
try:
	a = 1
	b = 2
	
	c > b
	print('OK')	
except:	
	print('ERROR')

# Ex2.
my_string = 'This is not a number!'

try:
	print('Converting my string to int...')
	1 / 0
	print('String #' + 1 + ": " + my_string)
	my_int = int(my_string)
	print(my_int)

except ValueError:	
	print("Can't convert; my_string to a number")

except TypeError:	
	print("Can't concatanate a number with string")

except:	
	print('Uknown Error')

print("Done!")

# Ex3.
try:
	input_file = open("NumberFile.txt", mode = "r")

	try:
		for line in input_file:
			print(int(line))

	except ValueError:
		print("A value error occured")

	else:
		print("No errors occured")
	finally:
		input_file.close()
except IOError:
	print("An error occured reading the file!")		