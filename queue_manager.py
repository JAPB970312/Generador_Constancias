# queue_manager.py
from queue import PriorityQueue
from enum import IntEnum

class Priority(IntEnum):
    HIGH = 1
    NORMAL = 2
    LOW = 3

class GenerationQueue:
    def __init__(self):
        self.queue = PriorityQueue()
        self.paused = False
    
    def add_job(self, job_data, priority=Priority.NORMAL):
        """Añade trabajo a la cola con prioridad"""
        self.queue.put((priority, job_data))
    
    def process_queue(self):
        """Procesa trabajos en orden de prioridad"""
        while not self.queue.empty() and not self.paused:
            priority, job_data = self.queue.get()
            yield job_data