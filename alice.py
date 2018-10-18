import socket
serverSocket = socket.socket()
serverSocket.bind(("localhost",9999))
serverSocket.listen(5)
connection , address = serverSocket.accept()
print("bob connected from" + address)
secretKey = raw_input("enter a secret key")