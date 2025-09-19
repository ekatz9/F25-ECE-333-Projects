#import socket module
from socket import *
import sys # in order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a server socket
host = '127.0.0.1'
port = 8888
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
        print(f'{filename} requested')
        f = open(filename[1:])
        #DEBUG:

        outputdata = f.read()

        #Send one HTTP header line into socket
        #assemble 200 OK response header
        header =   ('HTTP/1.1 200 OK\r\n'
                    'Accept-Ranges: bytes\r\n'
                   f'Content-Length: {len(outputdata)}\r\n'
                    'Keep-Alive: timeout = 5, max=100\r\n'
                    'Connection: Keep-Alive\r\n'
                    'Content-Type: text/html; charset=UTF-8\r\n')
        connectionSocket.send(header.encode())
        #DEBUG
        print(f'   200 OK response sent')
        print(header)

        #Send the content of the requested file to the client
        for i in range(0,len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
            #DEBUG
            #print(f'   \'{outputdata[i]}\'')
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    except IOError:
        #Send Response Message for file not found
        #404 reponse here
        connectionSocket.send('404 file found not'.encode())
