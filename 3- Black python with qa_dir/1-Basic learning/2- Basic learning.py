import platform

class InformationSystem:
    def __init__(self):
        pass

    def __str__(self):
        print('\n' * 3)
        print('******Start Engine******', '\n')
        print(f'Platform:{platform.machine()}', '\n') 
        print(f'Version:{platform.version()}', '\n') 
        print(f'OS name:{platform.platform()}', '\n') 
        print(f'uname:{platform.uname()}', '\n') 
        print(f'System:{platform.system()}', '\n') 
        print(f'Processor:{platform.processor()}', '\n') 
        return 'End'

sina = InformationSystem()

print(sina)
print('\n' * 3)

        
