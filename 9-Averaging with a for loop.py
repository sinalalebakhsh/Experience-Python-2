import os
os.system('cls')

# Averaging with a for loop
# میانگین گرفتن با حلقه for

number = [10, 20, 30, 40, 50, 60, 70, 80, 90]

result = 0

for numb in number:
    result += numb

print(result)
print(len(number))
print(result / len(number))

