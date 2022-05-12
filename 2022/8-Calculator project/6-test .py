def equal_operator():
    with open('memory.txt' , 'r') as memory:
        get_memory = memory.read()
        memory_list = get_memory.split('\n') # ['77', '+', '3', '+', '1', '+', '1']
        return memory_list
        # finall_list = [] # 
        # finall_number = 0.0  # 

        # for calc in memory_list: # 
        #     try:
        #         if float(calc):
        #             finall_list.append(float(calc))
        #             memory_list = memory_list[1:] # 
        #     except ValueError:
        #         try:
        #             if calc == '+':
        #                 finall_number = finall_list[0] + float(memory_list[1]) # 
        #                 finall_list[0] = finall_number # 
        #                 memory_list = memory_list[2:] # 
        #         except Exception:
        #             print(finall_number)

print(equal_operator())

