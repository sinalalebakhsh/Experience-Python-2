


with open('sina_second.txt' , 'a') as file:
    while True:
        user_input = input('Write name: ')
        if user_input == 'finish':
            break
        user_name = file.write(f'\n{user_input}')
        user_input = input('Enter score: ')
        if user_input == 'finish':
            break
        user_score = file.write(f' {user_input}')


with open('sina_second.txt' , 'r') as file:
    a = file.read().split('\n')
    numbers = []
    for sinanis in a:
        numbers.append(int(sinanis.split(' ')[1]))
print(numbers)
print(f'Sum numbers: {sum(numbers)} / {len(numbers)} = {sum(numbers)/len(numbers)}')
