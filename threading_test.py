from threading import Thread

def hello_dummy():
    print 'hi!'


if __name__ == '__main__':
    t = Thread(target=hello_dummy)
    t.start()
    t.join()

    
