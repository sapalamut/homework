from heapq import nlargest

# Ex:1
some_dict = {
    "one" : "aaa",
    "two" : "bbb",
    "three" : "ccc",
    "four" : "ccc",
    "five" : "eee",
    "six" : "bbb"
} 

uniq_dict = list()
dup_dict = list()

for i in some_dict.values():
    if i not in uniq_dict:
        uniq_dict.append(i)
    else:
        dup_dict.append(i)
print('The duplicates are:', dup_dict)
print('\n')

# Ex:2
some_dict = {
    "elem_1" : 1,
    "elem_2" : 15,
    "elem_3" : 47,
    "elem_4" : 18,
    "elem_5" : 74,
    "elem_6" : 3,
    "elem_7" : 50
}

highest = nlargest(3, some_dict, key = some_dict.get)
print(highest)
print('\n')

# Ex:3
some_string = 'alabalanica'

empty_dict = {}

for i in some_string:
    if i not in empty_dict:
        empty_dict[i] = 1
    else:
        empty_dict[i] += 1

print(empty_dict)
print('\n')

# Ex:4
some_list = {"bread": 5,
             "butter": 10,
             "milk": 7,
             "sugar": 11,
             "water": 15,
             "chocoloate": 13,
             "juice": 17,
             "cheese": 21
            }

def some_items(user_input_value):
    result = []
    for key in some_list.keys():
        if some_list[key] <= user_input_value:
            result.append(key)
    return result
    
entr_val = int(input('Enter numbers between 5 - 21 range: '))

print(some_items(entr_val))