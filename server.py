from socket import *
import os

# Function to determine the content type based on file extension
def get_content_type(filename):
    if filename.endswith(".html"):
        return "text/html"
    elif filename.endswith(".txt"):
        return "text/plain"
    elif filename.endswith(".jpg") or filename.endswith(".jpeg"):
        return "image/jpeg"
    elif filename.endswith(".png"):
        return "image/png"
    elif filename.endswith(".mp3"):
        return "audio/mp3"
    elif filename.endswith(".mp4"):
        return "video/mp4"
    return "application/octet-stream"

server_port = 12345
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('', server_port))
server_socket.listen(1)
print('The server is ready to receive')

# Server main loop
while True:
    connection_socket, addr = server_socket.accept()  # Accept incoming connections
    try:
        message = connection_socket.recv(1024).decode()  # Receive the request
        if message.startswith("GET"):
            filename = message.split(' ')[1][1:]  # Parse the filename from the request
            # Check if the file exists and send it
            if os.path.exists(filename):
                with open(filename, 'rb') as file:
                    content = file.read()
                header = f"HTTP/1.1 200 OK\r\nContent-Type: {get_content_type(filename)}\r\n\r\n"
                connection_socket.send(header.encode() + content)
            else:
                # Send 404 response if file not found
                header = "HTTP/1.1 404 Not Found\r\n\r\n"
                connection_socket.send(header.encode() + b"404 Not Found")
    except Exception as e:
        print("Error:", e)
    finally:
        connection_socket.close()  # Close the connection
