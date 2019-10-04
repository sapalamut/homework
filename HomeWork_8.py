# Ex:1 KM to Miles
def km_to_miles(km):
    conv_miles = 1.6
    return km / conv_miles
entr_num = float(input('Enter your number in kilometers: '))
print('Your distance in miles is:',km_to_miles(entr_num))
print('')

# Ex:2 Celsius to Fahrenheit
def cel_to_far(celsius):
    conv_fahrenheit = celsius * 9 / 5 + 32
    return conv_fahrenheit
entr_num = int(input('Enter your number in celsius: '))
print('Your degree in fahrenheit is:',cel_to_far(entr_num))
print('')

# Ex:3 Magic Ball