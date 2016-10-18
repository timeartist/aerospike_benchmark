from threading import Thread
from redis import StrictRedis, ConnectionPool

NUMBER_OF_CONNECTIONS = 10

R = lambda: StrictRedis(connection_pool=ConnectionPool(**{'host':'redis-13034.lace.demo-rlec.redislabs.com',

                                        'port':13034, 'max_connections':NUMBER_OF_CONNECTIONS}))

def hello_dummy():
    while True:
        r = R()
        r.set('foo', 'bar')
        r.get('foo')


if __name__ == '__main__':
    threads = []
    for i in range(50):
        t = Thread(target=hello_dummy)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
