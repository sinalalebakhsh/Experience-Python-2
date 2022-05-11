

user_ = input('Write something: ')

try:
    print(int(user_))
    print(2/0)
except ZeroDivisionError as sinanis:
    print('EXCEPTION' , sinanis)
except ModuleNotFoundError:
    print('Module not found')
except Exception:
    print('EXCEPTION')
else:
    print('else is this ...')
finally:
    print('FINALL is this')
