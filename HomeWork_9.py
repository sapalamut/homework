# Ex:1
def replacer(some_string):
    
    dollar = '$'
    empty = ' '
    
    for i in range(len(some_string)):
        if i == 0:
            empty += some_string[i]
        else:
            empty += dollar
    
    return empty    
    
entrtd_val = input('Enter a word: ')
print('Your entered word has "$" signs in it!', replacer(entrtd_val))
print('\n')

# Ex:2
def ending(some_str):
    
    last_char = len(some_str)
    
    if last_char > 2:
        some_str += 'ly'
    elif last_char <= 2:
        print(some_str)
    else:
        some_str += 'ing'
    
    return some_str

entrtd_val = input('Enter a word please: ')
print('The word you entered is:', ending(entrtd_val))
print('\n')
# Ex:3
















    