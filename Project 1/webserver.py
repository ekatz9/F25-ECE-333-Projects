#import socket module
from socket import *
import sys # in order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a server socket
host = '127.0.0.1'
port = 80
serverSocket.bind((host,port))

while True: 
    #establish connection
    print('ready to serve...')
    serverSocket.listen()
    connectionSocket, addr = serverSocket.accept()

    try:
        #message is GET request from Client
        message = connectionSocket.recv(1028)

        #f is requested file path
        filename = message.split()[1]
        print(f'f:{filename}')
        f = open(filename[1:])
        #DEBUG:
        print(f'{f} requested')

        outputdata = f.read()

        #Send one HTTP header line into socket
        #200 OK response here
        connectionSocket.send('200 ok'.encode())
        #DEBUG
        print(f'   200 OK response sent')

        #Send the content of the requested file to the client
        for i in range(0,len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
            print(f'   \'{outputdata[i]}\'')
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    except IOError:
        #Send Response Message for file not found
        #404 reponse here
        connectionSocket.send('404 file found not'.encode())
