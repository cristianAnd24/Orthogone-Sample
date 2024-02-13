# Basic Web Server

## Description
This project consists of a basic web server and client implementation using Python. The server serves files from its filesystem based on client requests.

## Requirements
- Python 3.x

## Usage
1. Run the server:
python server.py

The server will start on port 12345 and listen for incoming connections.

2. Run the client:
python client.py [host] [port] [filename] [timeout]
- `host`: IP address of the server (use '127.0.0.1' for localhost).
- `port`: Port number (use '12345' to connect to the running server).
- `filename`: Name of the file you want to request.
- `timeout`: (Optional) Timeout in seconds for the client to wait for a response (default is 5 seconds).

Example:
python client.py 127.0.0.1 12345 test123.txt

This will request the file 'test.txt' from the server.
