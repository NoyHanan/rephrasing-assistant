from KeyListener import KeyListener
from mpi4py import MPI


def run_listener_mac(comm: MPI.Comm, writer: int) -> None:
    key_listener = KeyListener(comm, writer)
    key_listener.start()
