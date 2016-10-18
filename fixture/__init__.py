from random import getrandbits
from threading import Lock

lock = Lock()

class Fixture(object):
    def __init__(self, object_size, connection_args, counter):
        self.object_size = object_size
        self.connection_args = connection_args
        self.counter = counter
        
    def write(self, keyname):
        raise NotImplementedError
    
    def read(self):
        raise NotImplementedError
    
    def _value(self):
        return 'x'*self.object_size

        
    
    
    
    