# Ex:1
def same_items(chars):
    list_items = 0
    for i in chars:
        if len(i) > 0 and i[0] == i[-1]:
            list_items += 1
    
    return list_items
ent_val = input('Enter something: ')
print('the matches are:', same_items(ent_val.split(',')))
print('\n')

# Ex:2
def empty_list():
    e_list = [] #Enter something here: 'abc'
    if len(e_list) == 0:
        print('This list is empty')
    else:
        print('This list is not empty')
    
    return ' '       
print(empty_list())
print('\n')

# Ex:3
def longest_word(words_list):
    max_val = words_list[0] 
    max_len = len(max_val)
    
    for i in words_list:
        if max_len < len(i):
            max_len = len(i)
            max_val = i
    
    return max_val
    
ent_val = input('Enter some words seperated by spaces: ')
print('The longest word is:', longest_word(ent_val.split(' ')))
print('\n')

# Ex:4
