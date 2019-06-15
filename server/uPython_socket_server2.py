#! /usr/bin/env python3
import network
import socket
from machine import Pin

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.ifconfig()
print()

led = Pin(2, Pin.OUT)
HOST = ''
PORT = 5020
CLIENTS = 1

def create_socket( addr, port_num, clients):
    sock = socket.socket()
    sock.bind((addr, port_num))
    sock.listen(clients)

    return sock

def socket_server(sock):
    try:
        print("Waiting for a connection...")
        conn, address = sock.accept()  # accept new connection
        print("Connection from: " + str(address))
        while True:
            data = conn.recv(1024).decode()
            if not data:
                # if data is not received break
                break
            print("from connected user: " + str(data))
            from_client = str(data)
            if from_client == '6on':
                led(0)
            elif from_client == '6off':
                led(1)

            conn.send(data.encode())  # send data back
    finally:
        conn.close()  # close the connection

SOCK = create_socket(HOST, PORT, CLIENTS)
while True:
    socket_server(SOCK)
    print("Conn closed - retrying")

