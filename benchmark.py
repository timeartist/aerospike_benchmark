from threading import Thread, Timer, Event

from aerospike.exception import RecordNotFound

from counter import AtomicCounter

from fixture import Fixture
from fixture.redis_fixture import RedisFixture
from fixture.aerospike_fixture import AerospikeFixture

OBJECT_SIZE = 20480
TEST_TIME = 10
NUMBER_OF_THREADS = 1
TIMEOUT = Event()

def benchmark_test(TestFixture, counter, **kwargs):
    fixture = TestFixture(OBJECT_SIZE, kwargs, counter)
    while True:
        fixture.write('foo')
        fixture.read('foo')
        if TIMEOUT.isSet():
            break
        
def times_up():
    print 'Times up!'
    TIMEOUT.set()


if __name__ == '__main__':
    threads = []
    counter = AtomicCounter()
    timer = Timer(TEST_TIME, times_up)
    timer.start()
    
    
    for i in range(NUMBER_OF_THREADS):
#        T = Thread(target=benchmark_test, args=(RedisFixture, counter), kwargs={'host':'redis-13034.lace.demo-rlec.redislabs.com', 'port':13034})
        T = Thread(target=benchmark_test, args=(AerospikeFixture, counter), kwargs={'hosts':[('172.31.12.144', 3000)]})
        T.start()
        threads.append(T)
    
    for t in threads:
        t.join()
        
    print counter.value()
    #
    #aerospike_server = 
    #A = AerospikeFixture(20480, {'hosts':[aerospike_server]}, counter)
    #A.write('baz')
    #try:
    #    A.read('lfdagdaga')
    #except RecordNotFound:
    #    print 'Record not Found'
