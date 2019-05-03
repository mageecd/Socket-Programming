Aja's Joke Algorithm README


How to use: Start the server first, then client, using a Python3 interpreter. Enter commands as prompted. 
Submitted version uses localhost, so two different command prompts will suffice. My DigitalOcean droplet's IP is in the code commented out in case you were curious.

Github Repository for Files: https://github.com/mageecd/Socket-Programming.git
This will show times that I updated the repo with changes, more programming, etc.
All in all, took me about 8 hours total of programming.

Guide used: https://www.techbeamers.com/python-tutorial-essentials-of-python-socket-programming/


Application-Layer Service:

Three paths are available to the user upon connection:
1. Joke please: Server picks a random knock knock joke from the jokes source file and tells it to the user.
2. Knock knock: Client/User can tell a knock knock joke to the server, which will log that joke and add it to the source file, allowing it to be used by the server later.
3. What does AJA mean?: A random number of Aja's Joke Algorithm "recursions" are sent to the client.

Client side:

Main function is to connect to the server and send string commands.
A small amount of other code allows for the client to know it needs to receive more data in the event that the "recursion" joke is requested.
Upon entering 'QUIT', the client will close the connection and inform the user.

Server side:

Main function is to listen and connect to a client, allowing the client to send commands. This contains most of the code for the application layer service.
Responds to the user/client commands with a small amount of error handling.

