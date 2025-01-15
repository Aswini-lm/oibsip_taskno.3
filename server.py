import socket

def start_server(host='127.0.0.1', port=5000):
    """Starts a TCP server that communicates with a single client."""
    try:
        # Create a socket and use a context manager to ensure proper cleanup
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((host, port))  # Bind the socket to the address
            server_socket.listen(1)          # Listen for incoming connections
            print(f"Server is running on {host}:{port} and waiting for a connection...")

            # Accept connection from a client
            conn, addr = server_socket.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    # Receive message from client
                    client_message = conn.recv(1024).decode()
                    if not client_message:  # Check for empty message
                        print("Client has disconnected.")
                        break
                    print(f"Client: {client_message}")
                    
                    # Handle exit command
                    if client_message.lower() == "exit":
                        print("Client requested to close the connection.")
                        break

                    # Send a response to the client
                    server_message = input("You: ")
                    conn.sendall(server_message.encode())
                    if server_message.lower() == "exit":
                        print("Server is closing the connection.")
                        break

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Server has shut down.")

if __name__ == "__main__":
    start_server()
