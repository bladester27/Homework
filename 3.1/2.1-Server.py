import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.7', 8888))
sock.listen(1)
print("Сервер запущен")
while True:
    try:
        client, addr = sock.accept()
    except KeyboardInterrupt:
        sock.close()
        break
    else:
        result = client.recv(1024)
        ans = result.decode('utf-8')
        x = ans[1:ans.find(',')]
        y = ans[ans.find(',') + 2:]
        x1 = x.replace("'", "")
        y1 = "".join(c for c in y if c.isdecimal())
        z = int(x1) + int(y1)
        print("Клиент отправил: ", x1, "и", y1)
        print("Отправляем ответ: ", z)
        client.send(bytes(str(z), encoding="UTF-8"))
        client.close()
