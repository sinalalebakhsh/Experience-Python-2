def equal_operator():
    with open('memory.txt' , 'r') as memory:
        get_memory = memory.read()
        memory_list = get_memory.split('\n')
    finall_number = 0
    while memory_list != []:
        try:
            if memory_list[1] == '+':
                finall_number = float(memory_list[0]) + float(memory_list[2])
                memory_list = memory_list[3:]
            elif memory_list[0] == '+':
                finall_number += float(memory_list[1])
                memory_list = memory_list[2:]
        except:
            memory_list = []

    return finall_number

print(equal_operator())
 