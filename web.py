import socket

def get_webpage(host, path="/"):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, 80))

    request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"
    s.sendall(request.encode())

    response = b""
    while True:
        chunk = s.recv(1024)
        if not chunk:
            break
        response += chunk

    s.close()
    return response.decode(errors='ignore')  # Handle decoding issues

# Example use
html_data = get_webpage("www.example.com")
print(html_data)

