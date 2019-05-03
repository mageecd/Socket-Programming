"""This is the Client Side for my networking socket programming project.
Socket project guide: https://www.techbeamers.com/python-tutorial-essentials-of-python-socket-programming/"""
import socket

def Main():
    host = '127.0.0.1' #localhost
    #host = '165.22.150.177' #server should be at this IP
    port = 4001 #server should be listening on this port

    mySocket = socket.socket()
    mySocket.connect((host, port))

    data = mySocket.recv(4096).decode()
    print(data)

    while True:
        message = input("Input: ")
        if str(message).upper() == 'QUIT':
            break
        mySocket.send(message.encode())
        if str(message).upper() == 'WHAT DOES AJA MEAN?':
            data = mySocket.recv(16384).decode() #make sure it can receive the entire "recursion" joke
        else:
            data = mySocket.recv(4096).decode()
        print(data)
        if not data:
            break
    print("Connection to " + host + " on port " + str(port) + " closed.")
    mySocket.close()

if __name__ == '__main__':
    Main()

