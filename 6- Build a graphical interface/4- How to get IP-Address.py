import socket, os
os.system('cls')
host = socket.gethostname()
ip = socket.gethostbyname(host)
print()
print(f'PC name={host}')
print()
print(f'IP-Address={ip}')
print()
