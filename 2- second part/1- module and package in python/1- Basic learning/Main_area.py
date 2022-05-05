import os

def cleaner():
    return os.system('cls')

def printer():
    print('This is printer function.')

def closerpage():
    print('The page closed.')

    
    
# when you write this : 
print('this is main area')
# So inside that one file runs
# but if write this :    
if __name__ == '__main__':
    print('this is main area  for more ... **** ')
#this not runs in another files
