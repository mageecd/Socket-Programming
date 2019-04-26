import socket
import time


def Main():
    host = '127.0.0.1' #localhost
    #host = "165.22.150.177" #server's host IP
    port = 4001 #server listens on this port

    mySocket = socket.socket()
    mySocket.bind((host, port))


    mySocket.listen(2)
    print("Running the socket project")
    conn, addr = mySocket.accept()
    print("Connection from: " + str(addr))

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("from connected  user: " + str(data))

        data = str(data).upper()
        #print("Received from User: " + str(data))

        data_out = data
        conn.send(data_out.encode())

        if data == "EXIT":
            break

    conn.close()


if __name__ == '__main__':
    Main()