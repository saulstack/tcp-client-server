import socket

SERVER_HOST = ''
SERVER_PORT = 20000
BUFFER_SIZE = 4096
FILE_PATH = 'FILE.PDF'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen(1)

    print('Server ready to start communication.')

    connection_socket, address = server_socket.accept()

    with connection_socket:
        print(f'Connection established with {address}')

        with open(FILE_PATH, 'rb') as file:
            while True:
                chunk = file.read(BUFFER_SIZE)

                if not chunk:
                    break

                connection_socket.sendall(chunk)

print('File sent successfully.')