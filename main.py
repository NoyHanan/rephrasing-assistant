from mpi4py import MPI
from config import API_KEYS, MASTER_RANK, SUB_RANK
from sub_process import run_listener
from primary_process import run_app
from utills import get_api_key

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == MASTER_RANK:
    print("available models: GooglePaLM")
    model_str = input("Enter the model you want to use: ")
    api_key = get_api_key(model_str, comm)
    # api_key = API_KEYS["GooglePaLM"]
    # model_str = "GooglePaLM"
    run_app(model_str, api_key, comm, SUB_RANK)
elif rank == SUB_RANK:
    run_listener(comm, MASTER_RANK)
else:
    raise ValueError(f"rank {rank} is not supported")
