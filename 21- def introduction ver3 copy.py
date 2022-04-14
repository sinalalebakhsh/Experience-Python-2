
def import_os():
    import os
    os.system('cls')
import_os()

import random

name_input_user = input('What\'s your name? ')
gender = input('Are you a women or a man? ')

def name_str(name_input_user, gender):
    teacher_name_man = ['sina', 'omid', 'sasan', 'saman', 'karen']
    teacher_name_women = ['kimia','mahsa', 'gandom', 'baran', 'sogand']
    ai_choice_women = random.choice(teacher_name_women)
    ai_choice_man = random.choice(teacher_name_man)
    if gender == 'woman':
        print(f'your name\'s {name_input_user}. and your teacher\'s Mr.{ai_choice_man}')
    elif gender == 'man':
        print(f'your name\'s {name_input_user}. and your teacher\'s Ms.{ai_choice_women}')
        

name_str(name_input_user, gender)