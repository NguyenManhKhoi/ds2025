import xmlrpc.server
import os

class FileTransferRPC:
    def sendfile(self, filename):
        """Send a file to the client."""
        if not os.path.exists(filename):
            return f"File '{filename}' not found on the server."
        
        with open(filename, 'rb') as f:
            file_data = f.read()
        
        return file_data

def run_rpc_server():
    # Create RPC server
    server = xmlrpc.server.SimpleXMLRPCServer(('0.0.0.0', 12344))
    server.register_instance(FileTransferRPC())
    print("RPC Server is running on port 12344...")
    server.serve_forever()

if __name__ == '__main__':
    run_rpc_server()
