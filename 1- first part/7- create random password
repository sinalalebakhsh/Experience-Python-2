import os
os.system('cls')

import string as s
from random import *

ch = s.ascii_letters + s.digits + s.punctuation

input_user = ''

print('write "finish" for finish\n')

while input_user != 'finish':
    password = "".join(choice (ch) for x in range(randint(11,20)))
    input_user = input('Press Enter to simplify the password')
    if input_user == 'finish':
        break
    if input_user != '':
        print('just press Enter')
    else:    
        print(password)
