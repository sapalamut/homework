dict_1 = {'key1': 1, 'key2': 2, 'key3': 3}
dict_2 = {'key1': 1, 'key2': 2, 'key4': 4}

for (key, value) in set(dict_1.items()) & set(dict_2.items()):
    print('%s: %s is the same' % (key, value))