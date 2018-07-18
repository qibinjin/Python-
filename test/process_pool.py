from multiprocessing import Pool,Manager
import os, time


def reader(q):
    print('reader run(%s), parent is (%s)' % (os.getpid(), os.getppid()))
    for i in range(q.qsize()):
        print('reader get msg...%s' % q.get(True))


def writer(q):
    print('writer is run,(%s), parent is %s' % (os.getpid(), os.getppid()))
    for i in 'itcast':
        q.put(i)

if __name__ == '__main__':
    print('(%s) start' % os.getpid())
    q = Manager().Queue()
    po = Pool()
    po.apply_async(writer, (q, ))
    time.sleep(1)

    po.apply_async(reader, (q, ))

    po.close()
    po.join()
    print('(%s) End'  % os.getpid())