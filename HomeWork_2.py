from datetime import datetime
from time import sleep

name = input('What is your name? ')
age = input('How old are you? ')
time = input('Do you know what time is it now? ')

def del_time():
    print('seems your watch is 3 seconds slow...')
sleep(3)
del_time()

now = datetime.now()
current_time = now.strftime("%H:%M:%S \n")
print("Current time is -", current_time)

game = input(f'Nice to meet you {name} - hit ENTER to play a Dice Game \n')

#----------------------------GAME-----------------------

score_decrement = 5
score_incerement = 15
score = 0
roll = int(input("Roll the dice 1: "))
time_in_millis = int(datetime.now().timestamp() * 1000)
ai_dice_value = time_in_millis % 6 + 1

if roll == ai_dice_value :
    score += score_increment
else :
    score -= score_decrement
print(f"{roll} / {ai_dice_value}")
    
roll = int(input("Roll the dice 2: "))
time_in_millis = int(datetime.now().timestamp() * 1000)
ai_dice_value = time_in_millis % 6 + 1

if roll == ai_dice_value :
    score += score_increment
else :
    score -= score_decrement
print(f"{roll} / {ai_dice_value}")

roll = int(input("Roll the dice 3: "))
time_in_millis = int(datetime.now().timestamp() * 1000)
ai_dice_value = time_in_millis % 6 + 1

if roll == ai_dice_value :
    score += score_increment
else :
    score -= score_decrement
print(f"{roll} / {ai_dice_value}")

print(f'Your score is {score} \n')
print("Better luck next time...")
