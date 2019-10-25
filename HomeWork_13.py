# Ex1

def entry(num_list):
    conv = list(num_list.split(",")) #List
    return conv
entr_num = input('Enter numbers separated by commas! ')

print("The numbers are:", entry(entr_num))

#-----------------------------------------#
def entry(num_list):
    conv = tuple(num_list.split(",")) #Tuple
    return conv
entr_num = input('Enter numbers separated by commas! ')

print("The numbers are:", entry(entr_num))

# Ex2

def remove_duplicates(your_data):
    no_duplicates_list = []

    splt_list = your_data.split(" ")

    for word in splt_list:
        if word not in no_duplicates_list:
            no_duplicates_list.append(word)
    return no_duplicates_list

def sort_list(my_list):
	return my_list.sort()

entered = input("Enter some words: ")

without_duplicates = remove_duplicates(entered)
sort_list(without_duplicates)

print(" ".join(without_duplicates))