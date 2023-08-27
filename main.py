from multiprocessing import Process, Queue
from utills import run_app, run_listener
from config import API_KEYS


queue = Queue()

if __name__ == '__main__':
    print("available models: GooglePaLM")
    model_string = input("Enter the model you want to use: ")
    api_key = API_KEYS[model_string]
    p1 = Process(target=run_app, args=(queue,))
    p2 = Process(target=run_listener, args=(model_string, api_key, queue,))

    p1.start()  # Start the Tkinter app
    p2.start()  # Start the keyboard listener

    p1.join()  # Wait for the Tkinter app to finish
    p2.terminate()  # Terminate the keyboard listener (optional based on your design)
