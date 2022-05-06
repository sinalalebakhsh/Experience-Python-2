import getpass


def print_info():
    user_info =  getpass.getuser()
    return user_info

print()
print(print_info())
print()
