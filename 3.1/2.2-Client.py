import socket

x = input('Введите первое число - ')
y = input('Введите второе число - ')
ds = x, y
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.7', 8888))
sock.send(bytes(str(ds), encoding="UTF-8"))
result = sock.recv(1024)
ans = result.decode('utf-8')
print(ans)
sock.close()
