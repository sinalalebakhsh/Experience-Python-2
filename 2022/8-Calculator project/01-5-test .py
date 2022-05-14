def duplicate_checker():
    with open('memory_in_one_line.txt' , 'r') as memory_in_one_line:
        get_memory_line_in_one_line = list(memory_in_one_line.read())
        if get_memory_line_in_one_line[-1] == '+':
            get_memory_line_in_one_line = get_memory_line_in_one_line[:-1]
            finall_list = ''.join(get_memory_line_in_one_line)
            with open('memory_in_one_line.txt' , 'w') as memory_in_one_line:
                memory_in_one_line.write(finall_list)
        if get_memory_line_in_one_line[-1] == '-':
            get_memory_line_in_one_line = get_memory_line_in_one_line[:-1]
            finall_list = ''.join(get_memory_line_in_one_line)
            with open('memory_in_one_line.txt' , 'w') as memory_in_one_line:
                memory_in_one_line.write(finall_list)
        if get_memory_line_in_one_line[-1] == '*':
            get_memory_line_in_one_line = get_memory_line_in_one_line[:-1]
            finall_list = ''.join(get_memory_line_in_one_line)
            with open('memory_in_one_line.txt' , 'w') as memory_in_one_line:
                memory_in_one_line.write(finall_list)
        if get_memory_line_in_one_line[-1] == '/':
            get_memory_line_in_one_line = get_memory_line_in_one_line[:-1]
            finall_list = ''.join(get_memory_line_in_one_line)
            with open('memory_in_one_line.txt' , 'w') as memory_in_one_line:
                memory_in_one_line.write(finall_list)
    return finall_list    



