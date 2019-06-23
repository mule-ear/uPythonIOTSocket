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
TIMEOUT = 10.0
V_OFFSET = .022

led = Pin(2, Pin.OUT)
adc = ADC(0)

def get_voltage(adc_obj, sample, dly):
    # A sample function to be caled by the client
    l = []
    for i in range(sample):
        l.append(adc_obj.read())
        time.sleep(dly)
    l.remove(max(l))
    l.remove(min(l))
    voltage = (sum(l)/len(l)) / .022
    return voltage


def create_socket( addr, port_num, clients):
    sock = socket.socket()
    sock.bind((addr, port_num))
    sock.listen(clients)
    # Added to make the socket non-blocking
    sock.setblocking(0)
    # Added to make it a hybrid application
    # Part socket server and part stand-alone
    # Where code can be executed even if there is no client
    sock.settimeout(TIMEOUT)

    return sock

def socket_server(sock):
    try:
        print("Waiting for a connection...")
        conn, addr = sock.accept()  
        print("Connection from: " + str(addr[0]))
        # sock.settimeout(60.0)
        # can't set the timeout once the connection has been establised
        while True:
            incoming_data = conn.recv(1024).decode()
            if not incoming_data:
                break
            print("Recieved from " + str(addr[0])+ ": " + str(incoming_data))
            # 6on was just an arbitrary message
            from_client = str(incoming_data)
            if from_client == '6on':
                led(0) # Activate the relay connected on D4
                reply = "Relay On"
            elif from_client == '6off':
                led(1) # Deactivate the relay
                reply = "Relay Off"
            elif from_client == "info":
                reply = DEVICE # Example
            elif from_client == "voltage":
                reply = str(get_voltage(adc, 5, 1)) # Example of performing a function
                                                    # Should take less than the timeout
            else:
                reply = "NoOp"

            conn.send(reply.encode()) 
    except OSError as e:
        # Handle expected event when no client is available
        print("No client available", e)
    finally:
        print("No connection")

# Create the socket outside of the server function
# Threads are not yet available in uPython
SOCK = create_socket(HOST, PORT, CLIENTS)
while True:
    socket_server(SOCK)
    # Sample of a funtion to be performed outside of a client request
    print(get_voltage(adc,5,1))
    print("No connection - retrying")

