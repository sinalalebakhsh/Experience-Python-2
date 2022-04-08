# برنامه ای بنویسید که از کاربر کلمه ای را بگیرد. سپس به کاربر بگوید که آیا طول این کلمه زوج است یا فرد

import os
os.system('cls')


input_user = input("Let's see how many characters are in your sentence? Is the number even or odd? : ")


len_input_user = len(input_user)


while input_user != 'sina':
    if int(len_input_user) % 2 == 0:
        print(f'\nYour sentence is {len_input_user} characters.')

        print('\nand this number is Even.')

        print('\nIf you want to stop, write (sina)')

        input_user = input("\nLet's see how many characters are in your sentence? Is the number even or odd? : ")

        len_input_user = len(input_user)
    else:
        print(f'\nYour sentence is {len_input_user} characters.')

        print('\nand this number is Odd.')

        print('\nIf you want to stop, write (sina)')

        input_user = input("\nLet's see how many characters are in your sentence? Is the number even or odd? : ")

        len_input_user = len(input_user)


print('\nmy mission is done :) ')

