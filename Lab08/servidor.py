import socket

host = "127.0.0.1"	# Standard loopback interface address (localhost)
port = 65432 	   	# Port to listen on (non-privileged ports are > 1023)
data_payload = 1024 # The maximum amount of data to be received at once

# Create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = (host, port)
print("Starting up echo server on %s port %s" % server_address)
sock.bind(server_address)

# Listen to clients, argument specifies the max no. of queued connections
sock.listen(5)
client, address = sock.accept()

while True:
	print("Wainting to receive message from client")
	data = client.recv(data_payload)
	message = data.decode()

	if message:
		print("Data: %s" % message)
		client.sendall(message.encode())
	else:
		break

print("Closing client connection", client)
client.close()