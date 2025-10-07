import time
from socket import *

# create a UDP Socket
host = input('enter destination IP:')
port = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

#(1) send the ping message using UDP
tsent = time.time()
message = f'the time is {tsent}'.encode('utf-8')
clientSocket.sendto(message,(host,port))
print(f'sent time {tsent}')

while True:
    trecv = time.time()

    # listen for message
    data, addr = clientSocket.recvfrom(1024)

    #(2) print the response message from server, if any
    if 'THE TIME IS' in data.decode():
        print(f'   recieved: {data}')

        #(3) calculate and print the round trip time (RTT), in seconds, of each packet, if server responses
        rtt = trecv-tsent
        print(f'   RTT: {rtt}')

    #(4) otherwise, print “Request timed out”
    if trecv - tsent > 15:
        print('   Request Timed Out')
        break