import socket


HOST = '127.0.0.1'
PORT = 9999
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))

print(f"server is lisetning at [{HOST}:{PORT}]")

while True:
    Data, address = server.recvfrom(1024)
    print(f"connected to {address}")
    
    print(f"message from client is : '{Data.decode('utf-8')}'")
    server.sendto(" got your message ! Thank you !".encode('utf-8'),(address))
    # communication_socket.close()
    # print(f"connection with {address} ended!")