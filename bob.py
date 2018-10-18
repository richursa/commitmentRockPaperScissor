import hashlib
import socket
clientSocket = socket.socket()
serverIP = raw_input("enter alices's ip address  to connect  ")
port = input("enter port no  ")
clientSocket.connect((serverIP,port))
print("connected successfully ")
aliceCommitment = clientSocket.recv(102400)
print("alice has commited ")
print(aliceCommitment)
bobChoice = raw_input("enter either rock,  paper or scissor ")
clientSocket.send(bobChoice)
aliceSecret  = clientSocket.recv(102400)
aliceChoice  = clientSocket.recv(102400)
if(hashlib.sha256(aliceSecret+aliceChoice).hexdigest() == aliceCommitment):
    if bobChoice == "rock":
        if aliceChoice == bobChoice :
            print("draw")
        elif aliceChoice == "scissor" :
            print("you won")
        else:
            print("you lost")
    elif bobChoice == "scissor":
        if aliceChoice == bobChoice:
            print("draw")
        elif aliceChoice == "paper":
            print("you won")
        else:
            print("you lost")
    else:
        if aliceChoice == bobChoice:
            print("draw")
        elif aliceChoice == "rock":
            print("you won")
        else:
            print("you lost")
else:
    print("alice has cheated ")