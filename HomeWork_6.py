# Ex:1
entr_num = int(input('Enter a number please: '))

for i in range(1, 10):
    if entr_num <= 0:
        print('Enter a valid number please')
        break
    else:
        print(entr_num, 'x', i, '=', entr_num * i)

# Ex:2
dots = int(input('Enter the number of dots: '))

for i in range(0, dots):
    for j in range(0, i + 1):
        print('* ', end='')
    print('\n')
for i in range(dots, 0, -1):
    for j in range(0, i - 1):
        print('* ', end='')
    print('\n')    

# Ex:3
dgt_count = int(input('Enter a number please: '))

count = 0
while(dgt_count > 0):
    dgt_count = dgt_count // 10
    count = count + 1
print('The number of digits is: ',count)    