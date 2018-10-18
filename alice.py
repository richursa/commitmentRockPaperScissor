import hashlib
import socket
print("waiting for bob to connect")
serverSocket = socket.socket()
serverSocket.bind(("localhost",9999))
serverSocket.listen(5)

connection , address = serverSocket.accept()
print("bob connected from " ,address)
secretKey = raw_input("enter a secret key ")
aliceChoice = raw_input("enter either rock , paper or scissor ")
string = secretKey + aliceChoice
hash = hashlib.sha256(string)
connection.send(hash.hexdigest())
print("bob is choosing ")
bobChoice = connection.recv(1024)
print("bob has chosen ")
print(bobChoice)
connection.send(secretKey)
connection.send(aliceChoice)
if bobChoice == "rock":
    if aliceChoice == bobChoice :
        print("draw")
    elif aliceChoice == "scissor" :
        print("you lost")
    else:
        print("you won")
elif bobChoice == "scissor":
    if aliceChoice == bobChoice:
        print("draw")
    elif aliceChoice == "paper":
        print("you lost")
    else:
        print("you won")
else:
    if aliceChoice == bobChoice:
        print("draw")
    elif aliceChoice == "rock":
        print("you lost")
    else:
        print("you won")