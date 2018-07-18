from multiprocessing import Process
import time
import os

def run_proc():
    while True:
        print('----2----%d%d' % (os.getpid(), os.getppid()))
        time.sleep(1)

if __name__ == '__main__':
    p = Process(target=run_proc)
    p.start()

    while True:
        print('----1----%d' % os.getpid())
        time.sleep(1)