# To work with network
import socket

# AF_INET == ipv4 connection
# Sock_stream == Tcp/ip
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(0.05)

ip = input("Type the ip : ")

ports = []
count = 0
while count < 10:
    ports.append = int(input("Type the port : "))
    count += 1

for port in ports:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.05)
    code = client.connect_ex((ip, port))

    if code == 0:
        print(str(port), ">> Open")
    else:
        print(str(port), ">> Close")
print("Finished")
