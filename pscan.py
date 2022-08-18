# To work with network
import socket

# AF_INET == ipv4 connection
# Sock_stream == Tcp/ip
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(0.05)

ip = input("Type the ip : ")
port = input("Type the port : ")

code = client.connect_ex((ip, port))

if code == 0:
    print("Open")
else:
    print("Close")