from multiprocessing import Process
from multiprocessing import Queue
import os, random, time


def write_data(q):
    for value in ['a', 'b', 'c']:
        print('put %s in queue' % value)
        q.put(value)
        time.sleep(random.random())


def read(q:Queue):
    while True:
        if not q.empty():
            value = q.get(True)
            print('get %s from queue' % value)
            time.sleep(random.random())
        else:
            break


if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write_data, args=(q,))
    pr = Process(target=read, args=(q,))

    pw.start()

    pw.join()

    pr.start()

    pr.join()

    print('')
    print('all process is done')

