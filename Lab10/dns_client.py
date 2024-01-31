from socket import *

host = "127.0.0.1" # Standard loopback interface address (localhost)
# host = "192.168.4.13" # Standard loopback interface address (localhost)
port = 30000       # Port to listen on (non-privileged ports are > 1023)
dataPayload = 1024 # The maximum amount of data to be received at once

# Cria o socket UDP
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Conecta o socket ao servidor
clientAddress = (host, port)
print("Connecting to %s port %s" % clientAddress)
print("-----------------------------------------------------")

# Definindo o tempo limite de 1 segundo
clientSocket.settimeout(1)

while True:
    print("WARNING: If you want to stop the server type 'stop'")
    name = input("Which domain do you want to know the address? ")

    if name == "stop":
        break

    # Tenta realizar essa tarefa
    try:
        # Enviar a mensagem criptografada para o servidor
        clientSocket.sendto(name.encode(), clientAddress)

        # Recebendo dados do socket UDP, com tamanho máximo 1024
        ipAddress, dnsAddress = clientSocket.recvfrom(dataPayload)

        # Descriptografa o endereço IP
        ipAddress = ipAddress.decode()

        # Imprimi as informações do servidor
        print("The IP address of the domain '" + name + "' is " + ipAddress)

        # Define mensagem para enviar para o servidor
        message = "Hello, " + name

        # Envia mensagem para o servidor informado
        clientSocket.sendto(message.encode(), (ipAddress, 60500))

        # Recebendo dados de volta do servidor informado
        data, serverAddress = clientSocket.recvfrom(dataPayload)

        print("Received: %s" % data.decode())
        print("-----------------------------------------------------")

    # Quando há um erro
    except:
        print("Request Timed Out")
        print("-----------------------------------------------------")
        continue