"""
worker manager
"""
import multiprocessing


def start_worker(task, worker_function):
    """start worker"""
    p = multiprocessing.Process(target=worker_function, args=(task,))
    p.start()
    return p


def stop_worker(process):
    """stop worker"""
    process.terminate()
