import os
os.system('cls')

print('Welcome to your journey')

playing = input('Do you want to play? ')

if playing.lower() != 'yes':
    print('Good Bye! ')
    quit()
else:
    print('OK, Let\'s go! ')

score = 0

answer = input('What does CPU stand for? ')
if answer.lower() == 'central processing unit':
    print('good job!')
    score += 1
else:
    print('You said wrong!')

answer = input('What does GPU stand for? ')
if answer.lower() == 'graphics processing unit':
    print('good job!')
    score += 1
else:
    print('You said wrong!')

answer = input('What does RAM stand for? ')
if answer.lower() == 'random access memory':
    print('good job!')
    score += 1
else:
    print('You said wrong!')

answer = input('What does PSU stand for? ')
if answer.lower() == 'power supply unit':
    print('good job!')
    score += 1
else:
    print('You said wrong!')

print('You got ' + str(score) + ' questions correct!')
print('You got ' + str((score / 4 ) * 100) + '%.')
