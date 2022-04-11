import os
os.system('cls')

user_char = ''

print('write "finish" 4 finish')

while user_char != 'finish':
    user_char = input('Just enter one character:')
    if user_char == 'finish':
        break
    if len(user_char) > 1 :
        print("your character can't be over one.")
    elif len(user_char) < 1:
        print("Your character can't be less than one.")
    else:
        if user_char.isalpha():
            if user_char.lower() in ['a','e', 'i', 'o', 'u']:
                print('Your character is one of the vowels.')
            else:
                print('Your character is one of the silent letters.')
        else:
            print('You can only write one letter of the alphabet')
