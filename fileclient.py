import socket


def file_transfer_client():
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect to the server
    client_socket.connect(('localhost', 12345))
    # Send the filename to the server
    filename = input("Enter the filename to send: ")
    client_socket.sendall(filename.encode())
    try:
        with open(filename, 'rb') as file:
            # Read the file and send it to the server in chunks
            while (chunk := file.read(1024)):
                client_socket.sendall(chunk)
    except FileNotFoundError:
        print(f"File {filename} not found.")
    print(f"File {filename} sent successfully.")
    client_socket.close()


if __name__ == '__main__':
    file_transfer_client()



