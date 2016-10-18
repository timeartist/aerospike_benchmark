from threading import Thread
from redis import StrictRedis, ConnectionPool

NUMBER_OF_CONNECTIONS = 10

R = lambda: StrictRedis(ConnectionPool({'host':'redis-13034.lace.demo-rlec.redislabs.com',
                                        'port':13034, max_connections=NUMBER_OF_CONNECTIONS}))

def hello_dummy():
    r = R()
    print r.set('foo', 'bar')
    print r.get('foo')


if __name__ == '__main__':
    t = Thread(target=hello_dummy)
    t.start()
    t.join()
