from socket import *
serverPort=12000
serverSocket=socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('User is ready')
while True:
    connectionSocket,addr=serverSocket.accept()
    sentence=connectionSocket.recv(1024).decode()
    print('Receive sentence: ',sentence)
    message=sentence.upper()
    connectionSocket.send(message.encode())
    connectionSocket.close()