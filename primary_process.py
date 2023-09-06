from KeyListener import KeyListener
from mpi4py import MPI

def run_listener(comm: MPI.Comm, master_process: int) -> None:
    key_listener = KeyListener(comm, master_process)
    key_listener.start()