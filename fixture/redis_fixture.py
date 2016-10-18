from fixture import Fixture

from redis import StrictRedis, ConnectionPool

class RedisFixture(Fixture):
    def __init__(self,  object_size, connection_args, counter, **kwargs):
        Fixture.__init__(self, object_size, connection_args, counter, **kwargs)
        self.R = StrictRedis(connection_pool=ConnectionPool(**connection_args))
        
    def write(self, key):
        self.R.set(key, self._value())
        self.counter.increment()
        
    def read(self, key):
        self.R.get(key)
        self.counter.increment()
    
    