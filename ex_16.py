
the_song = {
    1: "Oh yeah, I'll tell you something",
    2: "I think you'll understand",
    3: "When I'll say that something",
    4: "I want to hold your hand",
    5: "I want to hold your hand",
    6: "I want to hold your hand",
    7: "Oh please, say to me",
    8: "You'll let me be your man",
    9: "And please, say to me",
    10: "You'll let me hold your hand",
    11: "I'll let me hold your hand",
    12: "I want to hold your hand"
}

input_num = int(input('Enter a number from 1 to 12: '))
if input_num > 12:
    print('Enter a valid number!')
else:
    print(the_song[input_num])