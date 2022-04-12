
#محاسبه مجموع ارقام با حلقه for

import os
os.system('cls')

input_user = ''

while input_user != 'finish':
    input_user = input('Enter Your number: ')

    result = 0

    for i in input_user:
        result += int(i)

    print(result)
