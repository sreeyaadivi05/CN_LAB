import socket
import threading

clients = []


def handle_client(client_socket, client_address):
    print(f"New connection from {client_address}")
    while True:
        try:
            # Receive the message from the client
            message = client_socket.recv(1024).decode()
            if not message:
                break  # Client has disconnected
            print(f"Received from {client_address}: {message}")
            # Broadcast the message to all connected clients
            for client in clients:
                if client != client_socket:
                    client.sendall(message.encode())
        except:
            break
            # Remove the client from the list when they disconnect
    clients.remove(client_socket)
    client_socket.close()


def chat_server():
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to an address and port
    server_socket.bind(('localhost', 55556))
    # Listen for incoming connections
    server_socket.listen(5)
    print("Server listening on port 55555...")
    while True:
        # Accept a new client connection
        client_socket, client_address = server_socket.accept()
        # Add the client to the list
        clients.append(client_socket)
        # Start a new thread for each client
        threading.Thread(target=handle_client, args=(client_socket, client_address)).start()


if __name__ == '__main__':
    chat_server()