f = open('sina_second.txt', 'w')

names = ['sina' , 'sasan' , 'lale']

for names_ in names:
    f.writelines(names_)
    f.writelines('\n')

f.writelines(map(lambda name: name+'\n', names))




