import socket

def connect_to_server(parameter):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 9005))

    # Send parameter to the server
    client.send(parameter.encode())

    # Receive data from the server
    response = client.recv(1000)
    print(response.decode())

    # Close the client socket
    client.close()


connect_to_server("""""")


