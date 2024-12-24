import socket

HOST = '172.19.219.4'  # Localhost
PORT = 12344        # Port to listen on

# Create a socket 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))

# Start listening 
server_socket.listen(1)
print(f"Server listening on {HOST}:{PORT}...")

# Connection from client
conn, addr = server_socket.accept()
print(f"Connected by {addr}")

# Receive the file
file_name = conn.recv(1024).decode('utf-8')  # Receive file name
print(f"Receiving file: {file_name}")

# Open the file in write-binary mode to save it
with open(file_name, 'wb') as f:
    while True:
        
        data = conn.recv(1024)
        if not data:
            break  
        f.write(data)

print(f"File {file_name} received successfully.")
conn.close()  # Close 
server_socket.close()  
