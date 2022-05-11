

def error_handeling_for_user_input():
    while True:
        get_input = input('Enter number: ')
        try:
            get_input = int(get_input)
            print(get_input , 'is integer')
            break
        except ValueError:
            try:
                get_input = float(get_input)
                print(get_input , 'is float')
                break
            except ValueError:
                print('ValueError, can\'t write Non-numerical. just write numerical')
    return get_input


print(error_handeling_for_user_input())
