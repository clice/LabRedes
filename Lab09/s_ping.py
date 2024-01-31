# s_ping.py
import random
from socket import *

host = "127.0.0.1" # Standard loopback interface address (localhost)
# host = "192.168.0.6" # Standard loopback interface address (localhost)
port = 50000       # Port to listen on (non-privileged ports are > 1023)
dataPayload = 1024 # The maximum amount of data to be received at once

# Cria o socket UDP
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Define o endereço e a porta do socket
serverAddress = (host, port)
print("Starting up echo server on %s port %s" % serverAddress)
serverSocket.bind((host, port))

while True:
    # Gera números randômicos entre 0 to 10
    rand = random.randint(0, 10)

    # Recebe o pacote e o endereço do cliente
    message, address = serverSocket.recvfrom(dataPayload)

    # Coloca a mensagem em maíusculo
    message = message.upper()

    # Se o número rand é menor que 4, consideramos o pacote perdido.
    if rand < 4:
        continue

    # Caso contrário, o servidor responde
    serverSocket.sendto(message, address)