# practising TCP executed from LABView on Python
# CompA- TCP server


import socket
import threading


bind_ip = "192.168.166.201"  # assigning IP address
bind_port = 27700  # assigning port number
# New socket creation
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)
print("Server is listening on %s:%d" % (bind_ip, bind_port))

#Client handler function for recieving client data
def clientHandler(client_socket):
    # sending acknowledgemnet to the client
    client_socket.send("CompA is ready".encode())
    # Recieving binary data from the client
    request = client_socket.recv(1024)
    print("Received \"" + request.decode() + "\" from client")
    # close the connection again
    client_socket.close()
    print("Connection closed")


while True:
    # wait for client to connect
    client, addr = server.accept()
    print("Client connected " + str(addr))
    # create and start a thread to handle the client
    client_handler = threading.Thread(target=clientHandler, args=(client,))
    client_handler.start()
