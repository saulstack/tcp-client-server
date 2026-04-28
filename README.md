# TCP Client-Server Communication

Basic TCP communication between a client and a server using Python sockets.

## Overview

This project implements a simple client-server architecture over TCP.  
The client connects to the server and both sides can send and receive messages in real time.

## Features

- Establishes a TCP connection between client and server
- Sends and receives text messages
- Uses blocking sockets
- Handles connection termination when one side closes the connection

## How to Run

### 1. Start the server

    python server.py

### 2. Configure the client

Open `client.py` and set `SERVER_HOST` to the server machine's IP address.

### 3. Run the client

    python client.py

### 4. Communicate

Type messages in either the client or the server terminal.

## Technical Details

- Uses socket.AF_INET and socket.SOCK_STREAM (TCP)
- Messages are encoded using UTF-8
- Data is received in fixed-size buffers (1024 bytes)
- Connection is terminated when recv() returns empty data (b'')

## Limitations

- Only supports a single client connection
- No support for file transfer
- No encryption (plain text communication)
- No error handling for invalid inputs

## Future Improvements

- Implement file transfer over TCP
- Add metadata (filename and file size)
- Add progress tracking for file transfer
- Implement data integrity verification (SHA-256)
- Support multiple clients
- Add encrypted communication (TLS)

## Learning Goals

This project helped me understand:

- How TCP connections work
- Client-server communication
- Encoding and decoding data
- Blocking I/O behavior in sockets