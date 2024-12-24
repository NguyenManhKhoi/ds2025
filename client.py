import socket

def client_program():
    # server and client must have the same IP and port
    host = '172.19.219.4'  
    port = 12344  # Port
    
    # TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect to server
    client_socket.connect((host, port))
    
    # File
    filename = 'received_transfer_file.txt'  # Name the the file 
    
    # Try to receive the file from the server
    with open(filename, 'wb') as f:
        print(f"Receiving file from the server...")
        
        while True:
            data = client_socket.recv(1024)
            if not data:
                print("No more data received, closing connection.")
                break  # No more data received, end of file transfer
            f.write(data)  # Write data to the file

    print(f"File received successfully! Saved as {filename}")
    
    # Close ocket connection
    client_socket.close()

if __name__ == '__main__':
    client_program()
