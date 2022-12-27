import socket
from simplecrypt import encrypt, decrypt

HOST = '127.0.0.1'
PORT = 8000

passkey = 'ntu'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(10)
while True:
    conn, addr = server.accept()
    clientMessage = conn.recv(1024)

    print('Client message is:', clientMessage.decode("utf-8"))

    serverMessage = encrypt(passkey, clientMessage)
    conn.sendall(serverMessage)
    conn.close()
    
