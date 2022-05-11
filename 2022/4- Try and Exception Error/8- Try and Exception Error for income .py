from traceback import print_tb


def calc_income(income):
    if income < 0:
        raise Exception('Income should not be a negative number.')
    
    return income * 2

user_income = int(input('Enter your income: '))

try:
    print(calc_income(user_income))
except:
    print('EXCEPTION')

print('this text is test ...')



