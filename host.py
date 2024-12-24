from mpi4py import MPI
import os

def server_program():
    # mpi init
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    # Only process 0 will act as the server
    if rank == 0:
        host = '172.19.219.4'  # Server ip
        port = 12344            # Port 

        print(f"Server listening on {host}:{port}...")
        
        # Receive  from client (rank 1)
        file_name = comm.recv(source=1, tag=1)  # Client (rank 1) sends 
        print(f"Server is receiving the file: {file_name}")

        # Open the file to save data
        with open(file_name, 'wb') as f:
            data = comm.recv(source=1, tag=2)  # Receive from client
            while data:
                f.write(data)
                data = comm.recv(source=1, tag=2)

        print(f"File {file_name} received successfully.")
    else:
        print(f"Process {rank} is idle...")

if __name__ == "__main__":
    server_program()
