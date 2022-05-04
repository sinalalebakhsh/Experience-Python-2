# گرفتن ورودی از کاربر و محاسبۀ میانگین توسط کامپیوتر 
# ورژن بالاتر برای محاسبه میانگی


import os
os.system('cls')

print('Enter the numbers you want to calculate the mean. Finish at the end')


list_number = []

while True:
    input_number = input('Enter number: ')
    if input_number == 'finish':
        break
    if input_number.isalpha():
        print('you can just Enter "Numbers"')
    else:
      list_number.append(int(input_number))

print(f'sum number: {sum(list_number)}')
print(f'Average number: {sum(list_number) / len(list_number)}')
print(f'The max number: {max(list_number)}')
print(f'The min number: {min(list_number)}')

