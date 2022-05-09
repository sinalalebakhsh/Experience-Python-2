file = open('sina lalebakhsh.txt', 'r')

try:
    text_ = file.read()

    text_ = text_.split('\n')

    while True:
        user_input = input('Enter name: ')
        if user_input == 'finish':
            break
        text_.append(user_input)

    print(text_)
finally:
    file.close()