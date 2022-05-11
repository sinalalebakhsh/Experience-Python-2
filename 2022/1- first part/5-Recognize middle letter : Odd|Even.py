import os
os.system('cls')

user_input = input('Enter your word :') #sinas

user_input = user_input.replace(" ", "")
print(user_input)

len_user_input = len(user_input)

if len(user_input) == 0:
    print("your word can't be zero")
else:
    if len_user_input % 2 == 1:
        middle_index = int(len_user_input / 2)
        print(user_input[middle_index])
    else:
        middle_index = int(len_user_input / 2) 
        print(user_input[middle_index-1:middle_index+1])



