from socket import *
import sys

# Function to send a request to the server
def send_request(host, port, filename, timeout):
    with socket(AF_INET, SOCK_STREAM) as client_socket:
        client_socket.settimeout(timeout)  # Set timeout for the client socket
        try:
            client_socket.connect((host, port))  # Connect to the server
            print("Connection: OK")
            request = f"GET /{filename} HTTP/1.1\r\n\r\n"  # Formulate the GET request
            client_socket.send(request.encode())  # Send the request

            response = client_socket.recv(4096).decode()  # Receive the response
            header, content = response.split("\r\n\r\n", 1)  # Split header and content
            http_status = header.split(" ")[1]  # Extract the HTTP status code

            print("Request message sent.")
            print("Server HTTP Response:", header.split("\r\n")[0])  # Print HTTP response
            # Print content based on HTTP status
            if http_status == "200":
                print("Content-Type:", header.split("\r\n")[1].split(":")[1].strip())
                print(content)
            else:
                print(content)

        except ConnectionError:
            print("Connection error occurred.")
        except timeout:
            print("Client timed out waiting for the server's response.")

# Command line arguments processing
if len(sys.argv) < 4:
    print("Usage: python client.py [host] [port] [filename] (optional: timeout)")
    sys.exit(1)

host = sys.argv[1]
port = int(sys.argv[2])
filename = sys.argv[3]
timeout = 5 if len(sys.argv) < 5 else int(sys.argv[4])

# Send the request with provided parameters
send_request(host, port, filename, timeout)
