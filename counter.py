from threading import Lock


class AtomicCounter(object):
    def __init__(self):
        self.lock = Lock()
        self.count = 0
    
    def increment(self):
        self.lock.acquire()
        self.count += 1
        self.lock.release()
   
    def value(self):
        return self.count