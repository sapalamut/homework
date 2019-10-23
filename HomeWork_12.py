# Ex1
class GetString:
    def __init__(self):
        self.str_one = " "

    def set(self):
        self.str_one = input('Enter something: ')

    def get(self):
        print("The entered data is: ")
        return self.str_one

final_result = GetString()

final_result.set()
print(final_result.get().upper())

# Ex2
class Vehicle:
    def __init__(self, name, type, color, price):
        self.name = name
        self.type = type
        self.color = color
        self.price = price

    def describe(self):
        print('The car details are as follows:'.upper())
        print("Name is:",self.name)
        print("Type is:",self.type)
        print("Color is:",self.color)
        print("Price is:",self.price)

car1 = Vehicle("Fer", "convertible", "red", 60000)
car2 = Vehicle("Jump", "van", "blue", 10000)

car1.describe()
car2.describe()
