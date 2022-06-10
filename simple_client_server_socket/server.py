from base64 import encode
import socket


HOST = '127.0.0.1'
PORT = 9999
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen(5)
print(f"server is lisetning at [{HOST}:{PORT}]")

while True:
    communication_socket, address = server.accept()
    print(f"connected to {address}")
    message = communication_socket.recv(1024).decode('utf-8')
    print(f"message from client is : {message}")
    message = int(message)
    message = message*2 
    message = str(message)
    communication_socket.send(message.encode("utf-8"))

    
    

    communication_socket.close()
    print(f"connection with {address} ended!")