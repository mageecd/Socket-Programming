import socket

def Main():
    host = '127.0.0.1' #localhost
    #host = '165.22.150.177' #server should be at this IP
    port = 4001 #server should be listening on this port

    mySocket = socket.socket()
    mySocket.connect((host, port))

    message = input(" ? ")

    while message != 'q':
        mySocket.send(message.encode())
        data = mySocket.recv(1024).decode()

        print ('Received from server: ' + data)
        message = input(" ? ")

    mySocket.close()

if __name__ == '__main__':
    Main()