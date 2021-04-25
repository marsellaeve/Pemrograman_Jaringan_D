import socket

UDP_IP_ADDRESS = '192.168.122.25'
UDP_PORT = 5050

serverSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

serverSock.bind(((UDP_IP_ADDRESS,UDP_PORT)))

while True:
    data,addr = serverSock.recvfrom(1024)
    print("Message: ", data.decode())
