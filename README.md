# TCP File Transfer

Simple TCP-based file transfer between a client and a server using Python sockets.

## Overview

This project implements a basic client-server architecture over TCP that allows transferring files from a server to a client.

The server reads a file in binary mode and sends it in chunks.  
The client receives the data and reconstructs the file locally.

## Features

- TCP client-server communication
- File transfer over TCP
- Chunked transmission (4096 bytes)
- Binary-safe file handling (rb / wb)
- Simple and minimal implementation

## How to Run

### 1. Start the server

    python server.py

### 2. Configure the client

Open `client.py` and set the server IP address:

    SERVER_HOST = "127.0.0.1"  # or your server's IP

### 3. Configure the file (server side)

Open `server.py` and set the file to send:

    FILE_PATH = "FILE.PDF"

### 4. Run the client

    python client.py

The file will be received and saved locally.

## Technical Details

- Uses socket.AF_INET and socket.SOCK_STREAM (TCP)
- File is read and sent in fixed-size chunks (4096 bytes)
- Data is received using recv() and written directly to a file
- End of transmission is detected when recv() returns empty data (b'')

## Limitations

- Only supports a single client connection
- No file metadata is sent (filename is hardcoded)
- No progress tracking
- No data integrity verification
- No encryption (plain data transfer)

## Versions

- v1: basic TCP client-server communication  
- v2: file transfer over TCP  

## Future Improvements

- Send file metadata (filename and size)
- Add progress tracking during transfer
- Implement data integrity verification (SHA-256)
- Support multiple clients
- Add encrypted communication (TLS)

## Learning Goals

This project helped me understand:

- TCP socket communication
- Client-server architecture
- Binary file handling in Python
- Chunk-based data transmission
- How data flows over a TCP stream