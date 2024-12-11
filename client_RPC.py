import xmlrpc.client

def client_program():
    # Server info
    host = 'http://localhost'  # The server is running on the local machine
    port = 12344  # The same port as the server
    
    # Create an RPC client proxy to interact with the server
    server = xmlrpc.client.ServerProxy(f'{host}:{port}')
    
    # File to be received
    filename = 'received_transfer_file.txt'
    
    # Request the file from the server
    print(f"Requesting file '{filename}' from the server...")
    file_data = server.sendfile(filename)  # RPC call
    
    if isinstance(file_data, str) and file_data.startswith("File"):
        # If the server returns an error message (file not found, etc.)
        print(file_data)
    else:
        # Otherwise, save the received file
        with open(filename, 'wb') as f:
            print("Receiving file data...")
            f.write(file_data)
        print(f"File received successfully! Saved as {filename}")
    
if __name__ == '__main__':
    client_program()
