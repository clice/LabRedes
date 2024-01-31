import socket

host = "127.0.0.1"
port = 65432

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the server
client_address = (host, port)
print("Connecting to %s port %s" % client_address)
sock.connect(client_address)

# Send data
message = "Hello, world!"
sock.sendall(message.encode())
data = sock.recv(1024)
print("Received: %s" % data.decode())

print("Closing connection to the server")
sock.close()