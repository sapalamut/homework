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
def permission(name_str, surname_str, age_str):
     
    if name_str == "":
        print('Error: Name is empty')
        return False
    if surname_str == "":
        print('Error: Surname is empty')
        return False
     
    age_int = 0
    try:
        age_int = int(age_str)
    except:
        print('age field is empty')
        return False
     
    if age_int < 18:
        print('Error: Age must be at least 18')
        return False
     
    return True
 
name = input('What is your name? ')
surname = input('What is your surname? ')
age = input('What is your age? ')
 
is_valid = permission(name, surname, age)
 
def validation_action(key):
    if key == True:
        print('Next step')
    else:
        print('Something went wrong!')
validation_action(is_valid)
print('\n')

# Ex:4 Words in Sentence
def count_w(entrd_words):
    space_count = 0
    for c in entrd_words:
        if c == ' ':
            space_count = space_count + 1
             
    return space_count + 1
 
 
ent_val = input('Write something: ')
print('The number of words in sentence is:',count_w(ent_val))
print('\n')

# Ex:5 Any other Charater
def check_in(entrd_w):
    
    is_eng_only = True
    word_en = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxz'
    for c in entrd_w:
        if not c in word_en:
            is_eng_only = False
            break
    
    if is_eng_only:    
        print('Good, you entered ENG letters!')
    else:
        print('You entered wrong letter!')
        
    return is_eng_only

entr_smth = input('Type something please: ')
check_in(entr_smth)