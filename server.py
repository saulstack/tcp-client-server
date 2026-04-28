import socket

SERVER_HOST = ''
SERVER_PORT = 20000
BUFFER_SIZE = 1024
ENCODING = 'utf-8'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen(1)

    print('Server is listening...')

    connection_socket, client_address = server_socket.accept()

    with connection_socket:
        print(f'Connection established with {client_address}')

        while True:
            data = connection_socket.recv(BUFFER_SIZE)

            if not data:
                print('Connection closed by client.')
                break

            client_message = data.decode(ENCODING)
            print(f'Client: {client_message}')

            response = input('Server: ')
            connection_socket.sendall(response.encode(ENCODING))