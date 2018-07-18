from multiprocessing import Process
import os
from time import sleep


def run_proc(name, age, **kwargs):
    for i in range(10):
        print('fork process running...,name=%s,age=%d,pid=%d...' % (name, age, os.getpid()))
        print(kwargs)
        sleep(0.2)

if __name__ == '__main__':
    p = Process(target=run_proc, args=('test', 18),kwargs={'m':20})
    p.start()
    sleep(1)
    p.terminate()
    p.join()
