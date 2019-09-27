# Ex:1
entr_smth = input('Please enter a word or words: ')
if ' ' in entr_smth:
    print('This is a sentence')
else:
    print('This is a word')
    
# Ex:2
entr_num = int(input('Enter a number please: '))
total_sum = (entr_num % 5 == 0 or entr_num % 11 == 0)
if total_sum:
    print('This is divisable')
else:
    print('This is not divisable')
    
# Ex:3
ent_year = int(input('Enter a year please: '))
if (ent_year % 4) == 0:
    if (ent_year % 100) == 0:
        if (ent_year % 400) == 0:
            print(f'{ent_year} is a leap year!')
        else:
            print(f'{ent_year} is not a leap year')
    else:
        print(f'{ent_year} is a leap year!')
else:
    print(f'{ent_year} is not a leap year' )
