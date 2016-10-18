import aerospike

from fixture import Fixture


class AerospikeFixture(Fixture):
    def __init__(self,  object_size, connection_args, counter, **kwargs):
        Fixture.__init__(self, object_size, connection_args, counter)
        self.A = aerospike.client(connection_args).connect()
        self.namespace = 'bar'
        self.set = 'benchmark'
        
    def write(self, key):
        self.A.put((self.namespace, self.set, key), {'foo':self._value()})
        self.counter.increment()
        
    def read(self, key):
        self.A.get((self.namespace, self.set, key))
        self.counter.increment()
    