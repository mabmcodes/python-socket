import threading
import socket

HOST = "127.0.0.1"
PORT = 9999
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()
print(f"server is listening at [{HOST}:{PORT}]!")

clients = []
nickNames = []


def brodcast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            brodcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickName = nickNames[index]
            brodcast(f"{nickName} left the chat!\n".encode("utf-8"))
            nickNames.remove(nickName)


def receive():
    while True:
        client, address = server.accept()
        print(f"connected with {str(address)}")
        client.send("nick".encode("utf-8"))
        nickName = client.recv(1024).decode("utf-8")
        nickNames.append(nickName)
        clients.append(client)
        print(f"nickname of the client is {nickName}!")
        brodcast(f"{nickName} join th chat !".encode("utf-8"))
        client.send("connected to the server !".encode("utf-8"))
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


receive()
