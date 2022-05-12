def equal_operator():
    with open('memory.txt' , 'r') as memory:
        get_memory = memory.read()
        memory_list = get_memory.split('\n')
    finall_number = 0
    while memory_list != []:
        if memory_list[1] == '+':
            finall_number = float(memory_list[0]) + float(memory_list[2])
            memory_list = memory_list[3:]
        elif memory_list[0] == '+':
            finall_number += float(memory_list[1])
            memory_list = memory_list[2:]
    return finall_number


print(equal_operator())

# def equal_operator():
#     with open('memory.txt' , 'r') as memory:
#         get_memory = memory.read()
#         memory_list = get_memory.split('\n') # ['77', '+', '3', '+', '1', '+', '1']

#         finall_list = [] #  80 
#         finall_number = 0.0  # 80

#         for calc in memory_list: # '+'  ['77' , '+', '3', '+', '1', '+', '1']
#             try:
#                 if float(calc):
#                     finall_list.append(float(calc))
#                     memory_list = memory_list[1:] #   '+', '1'
#             except ValueError:
#                 try:
#                     if calc == '+':
#                         finall_number = finall_list[0]  float(memory_list[1]) # 81
#                         finall_list[0] = finall_number # 81
#                         memory_list = memory_list[2:] #  '+', '1'
#                 except Exception:
#                     print(finall_number)

# print(equal_operator())

