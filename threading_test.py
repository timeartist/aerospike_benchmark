from threading import Thread
from uuid import uuid4
from random import choice, getrandbits

from redis import StrictRedis, ConnectionPool


NUMBER_OF_CONNECTIONS = 1
NUMBER_OF_THREADS = 100
NUMBER_OF_KEYS = 1000
SIZE_OF_VALUE = 8*10*1024

GUIDS = []

R = lambda: StrictRedis(connection_pool=ConnectionPool(**{'host':'redis-13034.lace.demo-rlec.redislabs.com',
                                                          'port':13034,
                                                          'max_connections':NUMBER_OF_CONNECTIONS}))

def hello_dummy():
    r = R()
    while True:
        r.set(choice(GUIDS), getrandbits(SIZE_OF_VALUE))
        #r.get('foo'):q


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
