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
DEVICE = "Wemos D1 Mini"

def create_socket( addr, port_num, clients):
    sock = socket.socket()
    sock.bind((addr, port_num))
    sock.listen(clients)

    return sock

def socket_server(sock):
    try:
        print("Waiting for a connection...")
        conn, addr = sock.accept()  
        print("Connection from: " + str(addr[0]))
        while True:
            incoming_data = conn.recv(1024).decode()
            if not incoming_data:
                break
            print("Recieved from " + str(addr[0])+ ": " + str(incoming_data))
            # print(type(incoming_data))
            # 6on was just an arbitrary message
            from_client = str(incoming_data)
            if from_client == '6on':
                led(0)
                reply = "Relay On"
            elif from_client == '6off':
                led(1)
                reply = "Relay Off"
            elif from_client == "info":
                reply = DEVICE
            else:
                reply = "NoOp"

            conn.send(reply.encode()) 
    finally:
        conn.close() 

SOCK = create_socket(HOST, PORT, CLIENTS)
while True:
    socket_server(SOCK)
    print("Conn closed - retrying")

