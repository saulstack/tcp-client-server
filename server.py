import socket
from pathlib import Path

SERVER_HOST = ''
SERVER_PORT = 20000
BUFFER_SIZE = 4096
FILE_PATH = Path('file.mp4')
ENCODING = 'utf-8'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen(1)

    print('Server ready to start communication.')

    connection_socket, address = server_socket.accept()

    with connection_socket:
        print(f'Connection established with {address}')

        name_bytes = FILE_PATH.name.encode(ENCODING)
        length_name = len(name_bytes)
        connection_socket.sendall(length_name.to_bytes(4, 'big'))
        connection_socket.sendall(name_bytes)

        FILE_SIZE = FILE_PATH.stat().st_size
        connection_socket.sendall(FILE_SIZE.to_bytes(8, 'big'))


        with open(FILE_PATH, 'rb') as file:
            while True:
                chunk = file.read(BUFFER_SIZE)

                if not chunk:
                    break

                connection_socket.sendall(chunk)

print('File sent successfully.')