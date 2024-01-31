from socket import *

host = "127.0.0.1" # Standard loopback interface address (localhost)
# host = "192.168.0.6" # Standard loopback interface address (localhost)
port = 30000       # Default DNS port
dataPayload = 1024 # The maximum amount of data to be received at once

# Matriz com nomes e endereços para o DNS saber
addressesMatrix = [
    ['google', '127.0.0.2'],
    ['facebook', '127.0.0.3'],
    ['instagram', '127.0.0.4'],
    ['alice', '127.0.0.7']
]

# Cria o socket UDP
socketDNS = socket(AF_INET, SOCK_DGRAM)

# Define o endereço e a porta do socket
serverAddress = (host, port)
print("Starting up DNS on %s port %s" % serverAddress)
socketDNS.bind(serverAddress)

count = 0

while True:
    # Recebe um nome através do servidor
    name, clientAddress = socketDNS.recvfrom(dataPayload)
    name = name.decode()

    # Imprimi de onde veio a informação
    print('Received DNS query from: ', clientAddress)

    # Laço que percorre toda a matriz de endereços
    for domainName in addressesMatrix:
        # Procura na lista de endereços DNS o nome passado na mensagem
        if domainName[0] == name:
            # Envia o IP criptografado para o cliente
            socketDNS.sendto(domainName[1].encode(), clientAddress)