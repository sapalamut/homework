import math
#Romans to Ints

class py_solution:
    def roman_to_int(self, s):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(s)):
            if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
                int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
            else:
                int_val += rom_val[s[i]]
        return int_val

print(py_solution().roman_to_int('MMMCMLXXXVI'))
print(py_solution().roman_to_int('MMMM'))

# Ex2 Rectangle
class Rectangle:
	def __init__(self, l, w):
		self.length = 1
		self.width = w

	def rectangle_area(self):
		return self.length * self.width					

	def rectangle_perimeter(self):
		return (self.length + self.width) * 2

rectangle_l = int(input('Input rectangle length: '))
rectangle_w = int(input('Input rectangle width: '))

my_rectangle = Rectangle(rectangle_l, rectangle_w)

print(my_rectangle.rectangle_area())
print(my_rectangle.rectangle_perimeter())	

# Ex3 Circle
class Circle:
	def __init__(self, r):
		self.radius = r

	def area(self):
		return self.radius ** 2 * math.pi
	def perimeter(self):
		return 2 * self.radius * math.pi		

new_circle = Circle(8)

print(new_circle.area())
print(new_circle.perimeter())

