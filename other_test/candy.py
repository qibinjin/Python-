from atexit import register
from random import randrange
from threading import BoundedSemaphore, Lock, Thread
from time import sleep, ctime

lock = Lock()
MAX = 5
candytray = BoundedSemaphore(MAX) #设置信号量 即糖果槽最大值 默认初始是满的
print(candytray._value)
def refill():
    lock.acquire() #锁 开始线程
    print('Refilling candy...')
    print(candytray._value)
    try:
        candytray.release()  #尝试填充糖果槽
    except ValueError:  #如果是满的会报错
        print('full skipping...') #跳过填充
    else:
        print('Ok')
    lock.release() #解锁

def buy():
    lock.acquire()
    print('buying candy...')
    print(candytray._value)
    if candytray.acquire(False):  #非阻塞式的查看 信号量acquire 的值
        print('OK')
    else:
        print('empty,Skipping...')
    lock.release()

def producer(loops):
    for i in range(loops):
        refill()
        sleep(randrange(3))

def consumer(loops):
    for i in range(loops):
        buy()
        sleep(randrange(3))

def _main():
    print('starting at:',ctime())
    nloops = randrange(2, 6)
    print('The Candy Machine (full with %d bars)' % MAX)
    Thread(target=consumer,args=(randrange(nloops,nloops+MAX+2),)).start()
    Thread(target=producer,args=(nloops,)).start()

@register
def _atexit():
    print('all Done at:', ctime())

if __name__ == '__main__':
    _main()