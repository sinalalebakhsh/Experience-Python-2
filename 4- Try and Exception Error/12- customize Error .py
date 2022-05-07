class NegetiveNumberError(Exception):
    pass

def age_checker(age):
    if age <= 0 :
        raise NegetiveNumberError('Cant use zero & negetive number for age. ')
    return f'{age} * 2 = {age * 2}'

user_age = int(input('Enter the age: '))

print(age_checker(user_age))


