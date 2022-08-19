import socket

client = socket.socket(socket.AF_inet, socket.SOCK_DGRAM)
try:
    while True:
        message = input("Message: ") + "\n"
        client.sendto(message.encode(), ("127.0.1.1", 4444))  # Change this values
        data, sender = client.recvfrom(1024)
        print(sender[0], + ": " + data.decode())
        if data.decode() == "exit\n" or message == "exit\n":
            client.close()
            break
    client.close()
except Exception as error:
    print("Connection failed for the reason: ", error)
    client.close()
