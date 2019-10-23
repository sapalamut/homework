# Algorithms

def factorial(n):
	if n > 1:
		return n * factorial(n-1)
	else:
		return 1

print(factorial(5))	

# Ex1
class Book:
	def __init__(self, name, year, author, price):
		self.name = name
		self.year = year
		self.author = author
		self.price = price

def get_the_name(self):
	return self.author

def get_the_price(self):
	self.price = price

the_book1 = Book('Jack Russel', 1975, 'some items', '100$')
the_book2 = Book('Raild Kembis', 1223, 'some items', '140$')

print(the_book1.get_the_name())
print(the_book1.price)
the_book1.get_the_price("234$")
print(the_book1)




