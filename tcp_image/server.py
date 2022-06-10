import socket

PORT = 9999
HOST = "127.0.0.1"
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

client, address = server.accept()

file = open("server_image.jpg", "wb")
image_chunk = client.recv(2048)

while image_chunk:
    file.write(image_chunk)
    image_chunk = client.recv(2048)

file.close()
client.close()
