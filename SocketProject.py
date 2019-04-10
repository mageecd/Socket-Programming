#   https://www.techbeamers.com/python-tutorial-essentials-of-python-socket-programming/

# Managing errors in python socket programming

import socket  # for sockets
import sys  # for exit

try:
    # create an AF_INET, STREAM socket (TCP)
    sock_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as err_msg:
    print ('Unable to instantiate socket. Error code: ' + str(err_msg[0]) + ' , Error message : ' + err_msg[1])
    sys.exit();

print ('Socket Initialized')