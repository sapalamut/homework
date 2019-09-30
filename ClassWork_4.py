# FUNCTIONS

# Ex:1
def add_two_numbers(num1, num2):
	return	num1 + num2
result = add_two_numbers(1, 2)
print(result)
print(add_two_numbers(1, 2))
first = 1
second = 2
third = 3
print(add_two_numbers(first, second), add_two_numbers(second, third))
print('\n')

# Ex:2
def print_hello_world():
	print("Hello Wolrd")
print_hello_world()

# Ex:3
def box(six, five):
	return six * five
box_ad = box(6, 5)
print(box(6, 5))
print('\n')

# Ex:4
def math_class(first_num, second_num, third_num):
	return (first_num + second_num) // third_num

ent_frst = int(input('Enter the first number please: '))
ent_second = int(input('Enter the second number please: '))
ent_thhird = int(input('Enter the third number please: '))

print('The total sum is: ',math_class(ent_frst, ent_second, ent_thhird))
print('\n')

# Ex:5
def even_or_odd(number):
	if number % 2 == 0:
		return "Even"
	return "Odd"
		
print_num = int(input("Enter a number: "))

print(even_or_odd(int(float(print_num))))
print('\n')

# Ex:6
def two_numbers(num1, num2):
	return num1 + num2
print(two_numbers(1, 2))

# Ex:7
summing = 0

def add_numbers(num1, num2):
	summing =  num1 + num2

	add_numbers(5,6)

print(summing)


# Ex:8
def two_numbers(num1, num2 = 9):
	return num1 + num2
print(two_numbers(1,))

# Ex:9

def currency_amount(amount, currency="USD"):
    amount = str(amount)
    if currency == "JPY":
        return "¥" + amount
    elif currency == "USD":
        return "$" + amount    
    elif currency == "EUR":
        return "€" + amount
    else:
        return amount
print(currency_amount(5, "JPY"))

Ex:10

def check_balance(balance, entr_amount):
	entr_amount = int(input('Taxes are: '))
	if entr_amount <= balance:
		return True
	else:
		return False	


print(check_balance(400, 1000))