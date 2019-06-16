#! /usr/bin/env python3
import network
import socket
import time
from machine import Pin
from machine import ADC

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.ifconfig()
print()

HOST = ''
PORT = 5020
CLIENTS = 1
DEVICE = "Wemos D1 Mini"

led = Pin(2, Pin.OUT)
adc = ADC(0)

def get_voltage(adc_obj, sample, dly):
    l = []
    for i in range(sample):
        l.append(adc_obj.read())
        time.sleep(dly)
    l.remove(max(l))
    l.remove(min(l))
    voltage = (sum(l)/len(l)) * .022
    return voltage


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
            elif from_client == "voltage":
                reply = str(get_voltage(adc, 12, 5))
            else:
                reply = "NoOp"

            conn.send(reply.encode()) 
    finally:
        conn.close() 

SOCK = create_socket(HOST, PORT, CLIENTS)
while True:
    socket_server(SOCK)
    print("Conn closed - retrying")

