import os
os.system('cls')
import random

LINE_LENGTH = 15

number_cups = int(input('How many cups? '))
number_chances = int(input('How many chances? '))
print('-'*LINE_LENGTH)

list_choice_for_ai = []
counter_list = 0

for s in range(0,number_cups):
    counter_list += 1
    list_choice_for_ai.append(counter_list)

ai_choice_goal = random.choice(list_choice_for_ai)

input_Guess = 0

flag_number_chances = 0


word_for_last_chance = 's'

while input_Guess != ai_choice_goal:
    for counting in range(number_chances):
        if number_chances - counting == 1:
            word_for_last_chance = ''
        print(f'{number_chances - counting} chance{word_for_last_chance} left.')
        input_Guess = int(input(f'Guess[1-{number_cups}]: '))
        if input_Guess == ai_choice_goal:
            print('You guessed right.')
            print('-'*LINE_LENGTH)
            print('You won! ')
            break
            
        else:
            print('Wrong guess.')
            print('-'*LINE_LENGTH)
            flag_number_chances += 1
    if flag_number_chances == number_chances:
        print(f'The right answer is {ai_choice_goal}')
        print('You lost. Sorry!')
        input_Guess == ai_choice_goal
        break


