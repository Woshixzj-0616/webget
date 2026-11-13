from socket import *
serverPort=5201
serverSocket=socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(('',serverPort))
print('The server is ready to receive')
while True:
    message,clientAddress=serverSocket.recvfrom(2048)
    print('Receive message: ',message.decode())
    modifiedMessage=message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(),clientAddress)