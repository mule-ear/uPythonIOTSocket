#! /usr/bin/env python3
import socket

# Temporary hard coded host and port
HOST = '192.168.22.106'
PORT = 5020
SOCK = socket.socket()

def client(sock, host, port):
    sock.connect((host, port)) 
    msg2send = ''

    while msg2send.strip() != 'QUIT':
        msg2send = input("Message: ")
        sock.send(msg2send.encode())  
        receivedMsg = sock.recv(1024).decode() 
        print('Message from socket server: ' + receivedMsg)

    sock.close()

if __name__ == '__main__':
    client(SOCK, HOST, PORT)

