import socket

SERVER_HOST = 'SERVER IP: '
SERVER_PORT = 20000
BUFFER_SIZE = 1024
ENCODING = 'utf-8'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((SERVER_HOST, SERVER_PORT))

    while True:
        message = input('Client: ')
        client_socket.sendall(message.encode(ENCODING))

        data = client_socket.recv(BUFFER_SIZE)

        if not data:
            print('Connection closed by server.')
            break

        response = data.decode(ENCODING)
        print(f'Server: {response}')