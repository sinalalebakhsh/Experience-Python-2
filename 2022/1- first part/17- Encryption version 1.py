import os
os.system('cls')

my_str = input('Write down what you want to encrypt: ')

nums = []

for char in my_str:
    nums.append(str((ord(char)+43)))

print(','.join(nums))

secret_str = ','.join(nums)

list_from_secret = []

for s in secret_str.split(','):
    list_from_secret.append((chr(int(s)-43)))

print(''.join(list_from_secret))

