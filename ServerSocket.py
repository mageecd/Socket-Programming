import socket
import time
import random


def write_dictionary(dictionary):
    file = open("jokefile.txt", "w")
    for key in dictionary:
        line = key + " | " + "; ".join(dictionary[key]) + "\n"
        file.write(line)
    file.close()

def main():
    host = '127.0.0.1' #localhost
    #host = "165.22.150.177" #server's host IP
    port = 4001 #server listens on this port

    jokeDictionary = {} #a dictionary to store all the jokes
    inputFile = open("jokefile.txt", "r") #file to save the jokes

    for aline in inputFile:  # go through each line of the input
        setupList = [x.strip() for x in aline.split("|")]  # split the name from the classes
        punchlineList = [x.strip() for x in setupList[1].split(";")]  # split the classes into their own items
        if setupList[0] not in jokeDictionary:
            jokeDictionary[setupList[0]] = punchlineList
        else:
            jokeDictionary[setupList[0]] = jokeDictionary[setupList[0]] + punchlineList

    print(jokeDictionary)
    inputFile.close()

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
        instructions = "To hear a knock-knock joke, type JOKE PLEASE. \n To tell a knock-knock joke, type KNOCK KNOCK." \
                       "\n To learn about what AJA means, type WHAT DOES AJA MEAN? \n To quit at any time, type QUIT" \
                       "\nNote: Commands are NOT case-sensitive."
        conn.send(instructions.encode())
        state = 1

        while state != 0:
            data = conn.recv(1024).decode()
            command = str(data).upper()
            if not data or command == "QUIT":
                write_dictionary(jokeDictionary)
                return #get out of connection loop
            if state == 1: #waiting on initial command
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

            elif state == 2:#user has joke please path
                if command == "WHO'S THERE?":
                    setup = random.choice(list(jokeDictionary))
                    data_out = setup
                    state = 3
                else:
                    data_out = "Sorry, that is not a valid command. Try: WHO'S THERE?, or type QUIT to quit"
            elif state == 3:
                if command == str(setup).upper() + " WHO?":
                    randomNum = random.randint(0, len(jokeDictionary[setup]) - 1)
                    punchline = jokeDictionary[setup][randomNum]
                    data_out = punchline
                    state = 6
                else:
                    data_out = "Sorry, that is not a valid command. Try:" + str(setup).upper() + " WHO?, or type QUIT " \
                                                                                                 "to quit"

            elif state == 4:#user has chosen knock knock path
                setup = data
                data_out = setup + " who?"
                state = 5
            elif state == 5:
                punchline = data
                if setup not in jokeDictionary:
                    jokeDictionary[setup] = []
                newList = jokeDictionary[setup]
                newList.append(punchline)
                jokeDictionary[setup] = newList
                state = 6
            if state == 6:
                data_out = data_out + "\nWould you like to continue using AJA? YES/NO"
                state = 7
            elif state == 7:
                if command == "YES":
                    state = 0
                    break
                elif command == "NO":
                    write_dictionary(jokeDictionary)
                    return

            conn.send(data_out.encode())


    conn.close()


if __name__ == '__main__':
    main()