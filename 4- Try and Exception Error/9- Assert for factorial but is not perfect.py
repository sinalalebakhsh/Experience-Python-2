def check_number(number):
    assert number>2, 'for factorial number should be more than 2'
    return number


def factorial_maker(number):
    if number == 2:
        return 2
    else:
        return number * factorial_maker(number-1) 


print(factorial_maker(check_number('s')))