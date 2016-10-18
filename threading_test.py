from threading import Thread
from uuid import uuid4
from random import selection, getrandbits

from redis import StrictRedis, ConnectionPool


NUMBER_OF_CONNECTIONS = 10
NUMBER_OF_THREADS = 50
NUMBER_OF_KEYS = 100
SIZE_OF_VALUE = 8*10*1024

GUIDS = []

R = lambda: StrictRedis(connection_pool=ConnectionPool(**{'host':'redis-13034.lace.demo-rlec.redislabs.com',
                                                          'port':13034,
                                                          'max_connections':NUMBER_OF_CONNECTIONS}))

def hello_dummy():
    r = R()
    while True:
        r.set(choice(GUIDS), getrandbits(SIZE_OF_VALUE))
        #r.get('foo')


if __name__ == '__main__':
    for i in range(NUMBER_OF_KEYS):
        GUIDS.append(uuid4)

    threads = []
    for i in range(NUMBER_OF_THREADS):
        t = Thread(target=hello_dummy)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
