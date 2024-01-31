from socket import *

host = "127.0.0.7" # Standard loopback interface address (localhost)
port = 60500       # Default DNS port
dataPayload = 1024 # The maximum amount of data to be received at once

# Cria o socket UDP
aliceSocket = socket(AF_INET, SOCK_DGRAM)

# Faz o bind do socket Alice
aliceSocket.bind((host, port))

print('Server "alice" started. Listening on port 60500...')

while True:
    # Recebe informações através do servidor
    message, clientAddress = aliceSocket.recvfrom(dataPayload)

    print(clientAddress)

    # Imprimi de onde veio a informação
    print('Received DNS query from: ', clientAddress)
    print('Message: ', message.decode())

    # Envia mensagem para o servidor
    aliceSocket.sendto(message, clientAddress)
