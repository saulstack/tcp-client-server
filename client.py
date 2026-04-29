import socket

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 20000
BUFFER_SIZE = 4096
OUTPUT_FILE = 'received_file.pdf'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((SERVER_HOST, SERVER_PORT))

    with open(OUTPUT_FILE, 'wb') as file:
        while True:
            chunk = client_socket.recv(BUFFER_SIZE)

            if not chunk:
                break

            file.write(chunk)

print('File received successfully.')