# Ex:1
def max_num(num1, num2, num3):
    max_value = int(num1)
    if num2 > max_value:
        max_value = num2
        if num3 > max_value:
            max_value = num3
    elif num3 > max_value:
        max_value = num3
        
    return max_value

ent_first = int(input('Enter the first number please: '))
ent_second = int(input('Enter the second number please: '))
ent_thhird = int(input('Enter the third number please: '))

print('The Max number is:',max_num(ent_first, ent_second, ent_thhird))

# Ex:2
def fizz_buzz(ntrd_num):
    if ntrd_num % 3 == 0:
        print('Fizz', end='')
    if ntrd_num % 5 == 0:
        print('Buzz', end='')
    print('')
    return ntrd_num
type_a_number = int(input('Enter a number please: '))

fizz_buzz(type_a_number)

# Ex:3
def show_numbers(limit):
    for i in range(0, limit):
        if i % 2 == 0:
            print(str(i) + ' EVEN')
        else:
            print(str(i) + ' ODD')
    return limit    
entr_val = int(input('Type a limit number please: '))
print(show_numbers(entr_val))
    
    