import socket

UDP_IP_ADDRESS = '192.168.122.235'
UDP_PORT = 5050

serverSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serverSock.bind(((UDP_IP_ADDRESS,UDP_PORT)))
filename='server1.jpg'
fp = open(filename,'wb+')
ditulis=0
counter=0
while True:
    data, addr = serverSock.recvfrom(1024)
    counter=counter+len(data)
    print(addr," blok ", counter,"panjang : ",len(data), data)
    fp.write(data)

# while True:
#     data,addr = serverSock.recvfrom(1024)
#     print("Message: ", data.decode())
