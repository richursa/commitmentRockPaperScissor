import hashlib
import socket
clientSocket = socket.socket()
serverIP = raw_input("enter alices's ip address  to connect")
port = input("enter port no")
clientSocket.connect((serverIP,port))
print("connected successfully")
msg = clientSocket.recv(102400)
print("alice has commited ")
print(msg)
choice = raw_input("enter either rock paper or scissor")
clientSocket.send(choice)

