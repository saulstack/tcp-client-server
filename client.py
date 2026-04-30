import socket
from pathlib import Path


def recv_exact(sock, num_bytes):
    data = b''

    while len(data) < num_bytes:
        chunk = sock.recv(num_bytes - len(data))

        if not chunk:
            raise ConnectionError('Connection closed before receiving expected data.')

        data += chunk

    return data

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 20000
BUFFER_SIZE = 4096
ENCODING = 'utf-8'
PATH_TO_RECEIVED_FILE = Path('.')

with (socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket):
    client_socket.connect((SERVER_HOST, SERVER_PORT))

    raw_len_name = recv_exact(client_socket,4)
    file_name_len = int.from_bytes(raw_len_name, 'big')
    name_bytes = recv_exact(client_socket, file_name_len)


    FILE_NAME = name_bytes.decode(ENCODING)
    RECEIVED_FILE = PATH_TO_RECEIVED_FILE / Path(FILE_NAME).name

    DATA_SIZE = recv_exact(client_socket, 8)
    FILE_SIZE = int.from_bytes(DATA_SIZE, byteorder='big')

    current_received_bytes = 0
    with open(RECEIVED_FILE, 'wb') as file:
        while current_received_bytes < FILE_SIZE:
            remaining_bytes = FILE_SIZE - current_received_bytes
            chunk = client_socket.recv(min(BUFFER_SIZE, remaining_bytes))

            if not chunk:
                raise ConnectionError('Connection closed before full file was received.')

            file.write(chunk)
            current_received_bytes += len(chunk)
            percentage = (current_received_bytes / FILE_SIZE) * 100
            print(f'\rProgress: {percentage:.2f}%',  end = '')

    print('\nFile received successfully.')