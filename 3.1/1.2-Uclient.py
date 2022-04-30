import socket
from uuid import getnode as get_mac

mac = get_mac()
mac_dict = []
for i in str(mac):
    mac_dict += i
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(bytes(str(mac_dict), encoding="UTF-8"), ('localhost', 8888))

