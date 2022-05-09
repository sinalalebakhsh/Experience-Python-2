list_ = []

with open('sina lalebakhsh.txt', 'r') as file_name:
    for line in file_name.read().split('\n'):
        list_.append(line)

print(list_)
    