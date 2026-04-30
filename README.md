# TCP File Transfer

A simple TCP-based file transfer system implemented in Python using sockets.

## Overview

This project implements a client-server architecture over TCP that allows transferring files from a server to a client.

Version 3 introduces a custom protocol with metadata transmission, allowing the client to know the filename and total file size before receiving the file data.

This enables:

- Dynamic file naming
- Exact byte tracking
- Reliable file reconstruction
- Real-time progress monitoring

## Features

- TCP client-server communication
- File transfer over TCP
- Metadata transmission: filename and file size
- Chunked data transfer using 4096-byte chunks
- Binary-safe file handling using `rb` and `wb`
- Progress tracking during transfer
- Robust handling of partial TCP reads using `recv_exact`

## Protocol Design

The system uses a simple custom binary protocol:

    [4 bytes]  -> filename length as a big-endian integer
    [n bytes]  -> filename encoded in UTF-8
    [8 bytes]  -> file size in bytes as a big-endian integer
    [...]      -> file data streamed in chunks

This allows the client to know exactly:

- how many bytes to read for the filename
- how many bytes to expect for the file content
- when the file transfer is complete

## How to Run

### 1. Prepare the file on the server side

Place the file you want to send in the project directory and set the file path in `server.py`:

    FILE_PATH = Path('file.mp4')

### 2. Start the server

    python server.py

### 3. Run the client

    python client.py

The received file will be saved in the current directory.

## Technical Details

- Uses `socket.AF_INET` and `socket.SOCK_STREAM` for TCP communication
- Metadata is transmitted before the file content
- Integer values are encoded using big-endian byte order
- `recv_exact()` is used to receive an exact number of bytes from the TCP stream
- File data is received until the expected file size is reached
- The transfer does not rely on closing the connection to detect the end of the file
- Progress is calculated using:

    received_bytes / total_file_size * 100

## Limitations

- Supports only one client connection at a time
- No encryption; data is sent over plain TCP
- No checksum or hash verification yet
- No resume support for interrupted transfers
- File path is currently configured directly in the source code

## Versions

- v1: basic TCP client-server communication
- v2: file transfer over TCP
- v3: metadata protocol and progress tracking

## Future Improvements

- Add SHA-256 checksum verification
- Support multiple simultaneous clients
- Add resume support for interrupted transfers
- Add command-line arguments for host, port, and file path
- Add encrypted communication using TLS
- Improve error handling and logging

## Learning Goals

This project demonstrates:

- TCP socket programming
- Client-server architecture
- Binary file transmission
- Stream-based data handling
- Designing a simple application-layer protocol
- Handling partial reads in TCP
- Real-time transfer progress tracking