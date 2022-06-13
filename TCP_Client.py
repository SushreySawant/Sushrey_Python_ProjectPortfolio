#CompB- TCP client


import time
import random
import socket

while True:
 target_host = "192.168.166.201" # CompA IP address (address of local machine DHCP/static if both Client and server on same PC same as labview)
 target_port = 27700 # CompA port number

# creating a TCPIP-socket
 client: socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# connection request to CompA- TCP_server
 client.connect((target_host, target_port))

# Receiving Acknowledgement from CompB
 response = client.recv(2000)
 if response.decode() == "CompA is ready":
    print("Successful connection with CompB")
 else:
    print("FAILED")


# sending 32 bit binary data
 data = random.randint(0, 2147483647)
 print("OG:", bin(data))
 time.sleep(0.50) # toggling bit every 50ms
 data=data^1
 client.send(bin(data).encode())
 print("Toggle:", bin(data))
 time.sleep(2)  # Sending data every 2000ms










