from threading import Thread
from redis import StrictRedis, ConnectionPool

R = StrictRedis(ConnectionPool({'host':'redis-13034.lace.demo-rlec.redislabs.com',
                 'port':13034}))

def hello_dummy():
    print 'hi!'


if __name__ == '__main__':
    t = Thread(target=hello_dummy)
    t.start()
    t.join()
