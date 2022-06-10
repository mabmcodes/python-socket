from email import message
import socket

HOST = '127.0.0.1'
PORT = 9999
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
address = (HOST, PORT)

client.sendto(("Hello server!".encode('utf-8')), address)
data , address = client.recvfrom(1024)
print(data.decode('utf-8'))