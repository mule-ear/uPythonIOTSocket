# uPythonIOTSocket
Develop a strong MicroPython Client/Server using sockets

This initial commit has a working server and a client. 

It was tested on a Wemos D1 Mini, with a 3V3 relay connected to pin 2 (labelled D4 on the board)

## How to use this:
1. Install micropython on the D1 Mini [See micropython documentation](https://docs.micropython.org/en/latest/esp8266/tutorial/intro.html#intro) 
2. Copy the main.py file from the server directory over to the D1 mini using *ampy* [Ton of ampy tutorials - picked this at random:](https://www.dfrobot.com/blog-687.html) 
3. Connect your D1 Mini to your network - `help()` from the D1 Mini micropython prompt or [here](http://docs.micropython.org/en/latest/esp8266/quickref.html#networking)
4. Get the IP address from the D1 Mini
5. Restart the D1 Mini
6. Adjust the HOST address in the client script to match your D1 Mini address
7. Using python3 run the client script
8. Enter `6on` to activate the LED (or relay)
9. Enter `6off` to de-activate the relay
10. Enter `QUIT` to quit the client
