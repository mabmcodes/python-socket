import socket



HOST = "127.0.0.1"
PORT = 9999
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))


nomber = int(input("entrer un nomber" ))
nomber = str(nomber)
client.send(nomber.encode("utf-8"))

message =  client.recv(1024).decode("utf-8")

print(f"la multiplication de {nomber} est: {message}")
