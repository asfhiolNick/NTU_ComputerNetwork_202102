import socket
import time

HOST = '127.0.0.1'
PORT = 8000
server_addr = (HOST, PORT)

send_base = 0
next_seq_num = 0

cwnd_size = 3
num_pkt = 10

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# TODO: write your codes here
while next_seq_num < num_pkt:
    for i in range(next_seq_num, send_base+cwnd_size):
        clientMessage = str(i)
        client.sendto(clientMessage.encode(), server_addr)

    next_seq_num = send_base+cwnd_size
    client.settimeout(1)
    serverMessage = ''

    try:
        serverMessage, addr = client.recvfrom(1024)
    except Exception as e:
        print('timeout')
        next_seq_num = send_base

    if len(serverMessage)>0:
        send_base = int(serverMessage) + 1

while send_base < next_seq_num:
    try:
        serverMessage, addr = client.recvfrom(1024)
    except Exception as e:
        print('timeout')
        for i in range(send_base, next_seq_num):
            print('retranmit')
            clientMessage = str(i)
            client.sendto(clientMessage.encode(), server_addr)
    if len(serverMessage) > 0:
        send_base = int(serverMessage) + 1


