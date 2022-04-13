import os
os.system('cls')

input_number = int(input('Enter your Number: '))

is_prime = True

for s in range(2, input_number):
    if input_number % s == 0:
        is_prime = False
        print(f'{input_number} % {s} = 0')
        break

if is_prime ==True:
    print(f'Your number {input_number}\'s Prime.')
else:
    print(f'Your number {input_number}\'s not Prime.')

