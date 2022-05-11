
with open('sina_second.txt' , 'r') as file_ , open('testfile.txt' , 'w') as testfile:
    testfile.write(file_.read())
