import socket
import time


def Main():
    host = '127.0.0.1' #localhost
    #host = "165.22.150.177" #server's host IP
    port = 4001 #server listens on this port

    mySocket = socket.socket()
    mySocket.bind((host, port))


    mySocket.listen(2)
    conn, addr = mySocket.accept()
    print("Connection from: " + str(addr))
    welcome = "Welcome to AJA!"
    state = 0
    """State key: 
        0: Fresh "game"
        1: Waiting on initial command
        2: Waiting on who's there
        3: waiting on ____ who?
        4: waiting on joke setup
        5: waiting on punchline
        6: end message
        7: waiting on user to restart"""
    while True:
        instructions = "To hear a knock-knock joke, type JOKE PLEASE. \n To tell a knock-knock joke, type 'KNOCK KNOCK.'" \
                       "\n To learn about what AJA means, type WHAT DOES AJA MEAN? \n To quit at any time, type QUIT" \
                       "\nNote: Commands are NOT case-sensitive."
        conn.send(instructions.encode())
        print(state)
        state = 1
        print(state)
        while state != 0:
            data = conn.recv(1024).decode()
            command = str(data).upper()
            print(command)
            if not data or command == "QUIT":
                return #get out of connection loop
            if state == 1:
                if command == "WHAT DOES AJA MEAN?":
                    data_out = "(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A" \
                               "(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A" \
                               "(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A" \
                               "(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A" \
                               "(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A" \
                               "(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A" \
                               "(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A" \
                               "(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A" \
                               "(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A" \
                               "(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A" \
                               "(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A" \
                               "(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A" \
                               "(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A" \
                               "(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A" \
                               "(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A" \
                               "(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(" \
                               "A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(A(Aja's Joke Algorithm)Jok" \
                               "e Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algor" \
                               "ithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm) J" \
                               "oke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Alg" \
                               "orithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)" \
                               " Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke A" \
                               "lgorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorith" \
                               "m)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke" \
                               " Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algori" \
                               "thm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm) Jo" \
                               "ke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algo" \
                               "rithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm) " \
                               "Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Al" \
                               "gorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm" \
                               ")ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke " \
                               "Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorit" \
                               "hm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm) Jok" \
                               "e Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algor" \
                               "ithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm) J" \
                               "oke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Alg" \
                               "orithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm) " \
                               "Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Al" \
                               "gorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm" \
                               ")ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke " \
                               "Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorit" \
                               "hm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm) Jok" \
                               "e Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algor" \
                               "ithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm) J" \
                               "oke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Alg" \
                               "orithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm" \
                               ")ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke" \
                               " Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algor" \
                               "ithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm) " \
                               "Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke A" \
                               "lgorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorith" \
                               "m)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm) Jok" \
                               "e Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algo" \
                               "rithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)" \
                               " Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke " \
                               "Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algori" \
                               "thm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm) J" \
                               "oke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Al" \
                               "gorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorith" \
                               "m)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm) Jok" \
                               "e Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algo" \
                               "rithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)" \
                               " Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke " \
                               "Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algori" \
                               "thm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm) J" \
                               "oke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Al" \
                               "gorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorith" \
                               "m)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm) Jok" \
                               "e Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algo" \
                               "rithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)" \
                               " Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke " \
                               "Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algori" \
                               "thm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm) J" \
                               "oke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Al" \
                               "gorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorith" \
                               "m)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm) Jok" \
                               "e Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algo" \
                               "rithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)" \
                               " Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke " \
                               "Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algori" \
                               "thm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm) J" \
                               "oke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Al" \
                               "gorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorith" \
                               "m)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke" \
                               " Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algor" \
                               "ithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm) " \
                               "Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke A" \
                               "lgorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorit" \
                               "hm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm) Jo" \
                               "ke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Alg" \
                               "orithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm" \
                               ")ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke" \
                               " Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algor" \
                               "ithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm) " \
                               "Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke A" \
                               "lgorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorit" \
                               "hm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm) Jo" \
                               "ke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Alg" \
                               "orithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm" \
                               ")ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke" \
                               " Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algor" \
                               "ithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm) " \
                               "Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke A" \
                               "lgorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorit" \
                               "hm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm) Jo" \
                               "ke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Alg" \
                               "orithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm" \
                               ")ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke" \
                               " Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algor" \
                               "ithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm) " \
                               "Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke A" \
                               "lgorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorit" \
                               "hm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm) Jo" \
                               "ke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Alg" \
                               "orithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm" \
                               ")ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke" \
                               " Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algor" \
                               "ithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm) J" \
                               "oke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Al" \
                               "gorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorith" \
                               "m)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm) Jok" \
                               "e Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algo" \
                               "rithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)" \
                               " Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke " \
                               "Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algori" \
                               "thm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm) J" \
                               "oke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Al" \
                               "gorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorith" \
                               "m)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm) Jok" \
                               "e Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algo" \
                               "rithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)" \
                               " Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke " \
                               "Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algori" \
                               "thm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm) J" \
                               "oke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Al" \
                               "gorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorith" \
                               "m)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm) Jok" \
                               "e Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algo" \
                               "rithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)" \
                               " Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke " \
                               "Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algori" \
                               "thm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm) J" \
                               "oke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Al" \
                               "gorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorith" \
                               "m)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm) Jok" \
                               "e Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algo" \
                               "rithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)" \
                               " Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke " \
                               "Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algori" \
                               "thm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm)ja's Joke Algorithm) Jo" \
                               "ke Algorithm)ja's Joke Algorithm)" \
                               "\n........................Sorry, I got a bit lost in the recursion there."
                    state = 6
                elif command == "JOKE PLEASE":
                    data_out = "Knock knock"
                    state = 2
                elif command == "KNOCK KNOCK":
                    data_out = "Who's there?"
                    state = 4
                else:
                    data_out = "Sorry, that is not a valid command. Try: JOKE PLEASE, KNOCK KNOCK, or WHAT DOES " \
                               "AJA MEAN? to proceed, or type QUIT to quit"

            elif state == 2:
                if command == "WHO'S THERE?":
                    setup = "Tank"
                    data_out = setup
                    state = 3
                else:
                    data_out = "Sorry, that is not a valid command. Try: WHO'S THERE?, or type QUIT to quit"
            elif state == 3:
                if command == str(setup).upper() + " WHO?":
                    punchline = "You're welcome!"
                    data_out = punchline
                    state = 6
                else:
                    data_out = "Sorry, that is not a valid command. Try:" + setup + " WHO?, or type QUIT to quit"

            if state == 6:
                data_out = data_out + "\nWould you like to continue using AJA? YES/NO"
                print(data_out)
                state = 7
            elif state == 7:
                if command == "YES":
                    state = 0
                    break

            conn.send(data_out.encode())

        data = str(data).upper()
        #print("Received from User: " + str(data))

        data_out = data
        conn.send(data_out.encode())

    conn.close()


if __name__ == '__main__':
    Main()