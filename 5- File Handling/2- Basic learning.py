file = open('sina lalebakhsh.txt', 'r')

read_ = file.read()

complete_txt = ''

for sinanis in read_:
    if sinanis == '\n' :
        sinanis = ' '
    print(sinanis , end='')



