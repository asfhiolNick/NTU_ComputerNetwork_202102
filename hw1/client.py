import socket
from simplecrypt import encrypt, decrypt

HOST = '127.0.0.1'
PORT = 8000

def remoteEncrypt(msg):

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    client.sendall(msg.encode())

    #serverMessage = str(client.recv(1024), encoding='utf-8')
    serverMessage = client.recv(1024)

    client.close()
    return serverMessage

clientMessage = 'Hello!'
encoded = remoteEncrypt(clientMessage)

passkey = 'ntu'
print('Encoded message: ', encoded)

decoded = decrypt(passkey, encoded)
print('Decoded message: ', decoded.decode("utf-8"))
