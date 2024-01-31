from socket import *
import time

host = "127.0.0.1" # Standard loopback interface address (localhost)
# host = "192.168.0.6" # Standard loopback interface address (localhost)
port = 50000       # Port to listen on (non-privileged ports are > 1023)
dataPayload = 1024 # The maximum amount of data to be received at once

# Cria o socket UDP
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Conecta o socket ao servidor
clientAddress = (host, port)
print("Connecting to %s port %s" % clientAddress)
print("-----------------------------------------------------")

# Definindo o tempo limite de 1 segundo
clientSocket.settimeout(1)

# Definindo as variáveis iniciais
minimum, maximum = 1, 0
average, lost = 0, 0

# Laço para percorrer os
for i in range(10):
    # Definindo a mensagem para enviar
    message = "Hello, " + str(i + 1) + "! " + time.asctime()

    # Tenta realizar essa tarefa
    try:
        # Retorna o tempo atual em segundos do servidor
        rttBegin = time.time()

        # Enviar a mensagem criptografada para o servidor
        clientSocket.sendto(message.encode(), clientAddress)

        # Recebendo dados do socket UDP, com tamanho máximo 1024
        data, address = clientSocket.recvfrom(dataPayload)

        # Retorna o tempo atual em segundos do cliente
        rttEnd = time.time()

        # Imprimi os dados recebidos do servidor
        print("Answer from " + address[0])
        print("Message: " + data.decode())

        # Soma para saber o tempo total
        rtt = rttEnd - rttBegin
        print("The Round Trip Time was " + str(rtt) + " seconds")

        # Encontrar o tempo mínimo de resposta
        if rtt < minimum:
            minimum = rtt

        # Encontrar o tempo máximo de resposta
        if rtt > maximum:
            maximum = rtt

        # Soma o tempo para o cálculo da média
        average += rtt

        print("-----------------------------------------------------")

    # Quando há um erro (rand < 4)
    except:
        # Soma o que deu erro para saber a porcentagem do pacote perdido
        lost += 1
        print("Request timed out " + str(i + 1) + "!")
        print("-----------------------------------------------------")
        continue

# Se teve algum dado perdido, fazer o cálculo da média
if lost != 0:
    average /= lost
# Se nada se perdeu, a média é zero
else:
    average = 0

print("Minimum Round Trip Time: " + str(minimum) + " seconds")
print("Maximum Round Trip Time: " + str(maximum) + " seconds")
print("Average Round Trip Time: " + str(average) + " seconds")
print("Percentage lost of the package: " + str(lost * 10) + "%")

# Fechando o servidor
print("Closing connection to the server")
clientSocket.close()