file = open('sina lalebakhsh.txt', 'r')

while True:
    readline_ = file.readline()
    for sinanis in readline_:
        if sinanis == '\n':
            sinanis = ' '
        print(sinanis, end='')
    if readline_ == '':
        break

