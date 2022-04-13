# نمایش چدول ضرب در خروجی

import os
os.system('cls')


list_numbers = [1,2,3,4,5,6,7,8,9,10]

list_numbers_2 = [1,2,3,4,5,6,7,8,9,10]

for s in list_numbers:
    for i in list_numbers_2:
        print(f'multiply number{s} by {i} = {s * i}')


