# coidng: utf-8 -*-


import sys

import threading

import time


def loop():
    print('thread {} is running...'.format(threading.current_thread().name))
    n = 0
    while n < 5:
        n = n + 1
        print('thread {} >>> {}'.format(threading.current_thread().name, n))
        time.sleep(20)
    print('thread {} ended.'.format(threading.current_thread().name))


if __name__ == '__main__':
    '''
    i = 0
    for arg in sys.argv:
        print('arg[{}]: {}\n'.format(i, arg))
        i += 1
    '''
    print('thread {} is running...'.format(threading.current_thread().name))
    t = threading.Thread(target=loop, name='LoopThread')
    t.start()
    try:
        while True:
            print('thread {} is running...'.format(threading.current_thread().name))
            time.sleep(5)
    except KeyboardInterrupt:
        print("Process is ended by KeyboardInterrupt!")
    #t.join()
    print('thread {} ended.'.format(threading.current_thread().name))
