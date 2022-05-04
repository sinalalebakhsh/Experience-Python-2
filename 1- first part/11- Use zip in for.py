import os
os.system('cls')

list_names = ['sina', 'mina', 'lina', 'dina']
list_names = list(map(lambda x: x.upper(), list_names))

list_marks = ['10', '20', '30', '40']
list_ages = ['30' , '20', '10', '5']

for name, mark, age in zip(list_names, list_marks, list_ages):
    print(f'name={name}|mark={mark}|age={age}')
