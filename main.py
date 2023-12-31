from mpi4py import MPI
from config import MASTER_RANK, SUB_RANK
from sub_process import run_listener_mac
from primary_process import run_app_mac
from utills import get_api_key, get_model_str

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == MASTER_RANK:
    model_str = get_model_str()
    api_key = get_api_key(model_str, comm)
    run_app_mac(model_str, api_key, comm, SUB_RANK)
elif rank == SUB_RANK:
    run_listener_mac(comm, MASTER_RANK)
else:
    raise ValueError(f"rank {rank} is not supported")
