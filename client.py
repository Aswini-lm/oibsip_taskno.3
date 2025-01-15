import socket

def start_client(host='127.0.0.1', port=5000):
    """
    Starts a TCP client to communicate with a server.

    Args:
        host (str): The server's IP address. Default is localhost ('127.0.0.1').
        port (int): The server's port number. Default is 5000.
    """
    try:
        # Create a socket object
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            print(f"Attempting to connect to the server at {host}:{port}...")
            client_socket.connect((host, port))  # Connect to the server
            print("Connected to the server. Type 'exit' to quit.\n")

            while True:
                # Get user input for the message to send
                client_message = input("You: ").strip()
                if not client_message:
                    print("Empty messages are not allowed. Please try again.")
                    continue
                
                client_socket.sendall(client_message.encode())  # Send message to the server
                if client_message.lower() == "exit":
                    print("Connection closed by the client.")
                    break

                # Receive message from the server
                server_message = client_socket.recv(1024).decode()
                if not server_message:
                    print("Server has disconnected.")
                    break
                elif server_message.lower() == "exit":
                    print("Server has closed the connection.")
                    break

                print(f"Server: {server_message}")

    except ConnectionRefusedError:
        print("Error: Could not connect to the server. Ensure the server is running and accessible.")
    except KeyboardInterrupt:
        print("\nConnection interrupted by the user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Client has shut down.")

if __name__ == "__main__":
    # Optionally allow the user to specify host and port
    host_input = input("Enter server IP (press Enter for default '127.0.0.1'): ").strip()
    port_input = input("Enter server port (press Enter for default 5000): ").strip()
    
    host = host_input if host_input else '127.0.0.1'
    port = int(port_input) if port_input.isdigit() else 5000

    start_client(host, port)
