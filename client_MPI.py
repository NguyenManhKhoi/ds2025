from mpi4py import MPI
import os

def client_program():
    # MPI init
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    if rank == 1:  # Client process with rank 1
        host = '172.19.219.4'  # Server IP (same as before)
        port = 12344            # Port

        # File 
        filename = 'send_file.txt'

        # Send the filename to the server (rank 0)
        comm.send(filename, dest=0, tag=1)
        print(f"Sending file: {filename}")

        # Open the file to send
        with open(filename, 'rb') as f:
            data = f.read(1024)  
            while data:
                comm.send(data, dest=0, tag=2)  
                data = f.read(1024)

        
        comm.send(None, dest=0, tag=2)
        print(f"File {filename} sent successfully.")
    else:
        print(f"Process {rank} is idle...")

if __name__ == "__main__":
    client_program()
