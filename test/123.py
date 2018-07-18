from atexit import register
from random import randrange
from threading import Thread, Lock, current_thread
from time import sleep, ctime


class CleanOutputSet(set):
    def __str__(self):
        return ', '.join(x for x in self)
lock = Lock()
loops = (randrange(2,5) for x in range(randrange(3,7)))
remaining = CleanOutputSet()
print(loops)
def loop(nsec):
    myname = current_thread().name
    lock.acquire()
    remaining.add(myname)
    print('[%s] Started %s' % (ctime(), myname))
    lock.release()
    sleep(nsec)
    lock.acquire()
    remaining.remove(myname)
    print('[%s] Completed %s (%d secs)' % (ctime(), myname, nsec))
    print('   (remaining:%s)' % (remaining or None))
    lock.release()

def _main():
    for pause in loops:
        Thread(target = loop, args=(pause,)).start()
@register
def _atexit():
    print('all Done at:', ctime())
if __name__ == '__main__':
    _main()