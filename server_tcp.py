import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    server.bind(("0.0.0.0", 4444))  # Listen that server port && CHANGE VALUES
    server.listen(5)
    print("Listening... ")
    client_socket, address = server.accept()
    print("Received from: " + address[0])

    while True:
        data = client_socket.recv(1024).decode()
        print(data)
        client_socket.send(input("Message: " + "\n").encode())
    server.close()

except Exception as error:
    print("Error ", error)
