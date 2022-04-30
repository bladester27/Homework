import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('127.0.0.1', 8888))

while True:
    try:
        result = sock.recv(40960)
    except KeyboardInterrupt:
        sock.close()
    else:
        print('New Device, MAC: ', result.decode('utf-8'))
