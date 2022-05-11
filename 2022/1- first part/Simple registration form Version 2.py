import os
os.system('cls')


user_name = ''
password = ''
user_finish = input('write "finish" for finish : ')

while user_finish != 'finish':       
    user_name = input('Enter Your User name: "write finish 4 finish" ')
    if user_name == 'finish':
        break
    password = input('Enter Your Password: ') 
    if user_name == password:
        print("Username and password cannot be the same.")
    if len(password) < 8:
        print("Password length should be at least 8 chars ")
    if len(password) > 20:
        print("password length should be at most 20 chars ")
    if len(user_name) < 4:
        print("User name length should be at least 4 chars ")
    
    #If you want all the conditions to be fulfilled together and
    #you do not take the user's time anymore, it is better to write like this.

    if not ((user_name == password) or (len(password) < 8) or (len(password) > 20) or (len("User name") < 4)):
        print(f"your user name is good {user_name} and your password is strong {password}")
