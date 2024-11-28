import time
import random
from queue import Queue
from threading import Thread

class WorkerNode:
    def __init__(self, id):
        self.id = id
        
    def process_task(self, task):
        print(f"Worker {self.id} processing: {task}")
        time.sleep(random.uniform(1, 3))  # Set a range for random sleep time
        print(f"\nWorker {self.id} finished: {task}")   
        
def worker(task_queue, worker_id):
    while True:
        task = task_queue.get()
        if task is None:
            break
        WorkerNode(worker_id).process_task(task)
        task_queue.task_done()
      
def main():
    task_queue = Queue()
    num_workers = 2
    threads = []
    
    for i in range(num_workers):
        t = Thread(target=worker, args=(task_queue, i))
        t.start()
        threads.append(t)
        
    tasks = [f"Task {i}" for i in range(5)]
    
    for task in tasks:
        task_queue.put(task)
        
    task_queue.join()
    
    for _ in range(num_workers):
        task_queue.put(None)
    for t in threads:
        t.join()
        
    print("All tasks processed.")
    
if __name__ == "__main__":
    main()
