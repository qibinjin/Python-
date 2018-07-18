from atexit import register
from random import randrange
from threading import Thread, Lock, currentThread
from time import sleep, ctime

class CleanOutputSet(set):
    def __str__(self):
        return ', '.join(x for x in self)

lock = Lock()
loops = (randrange(2, 5) for x in range(randrange(3, 7)))#写出一个随机数生成器 范围2,4 个数3,6
remaining = CleanOutputSet() #特殊的集合类,重写了print

def loop(nsec):
    myname = currentThread().name
    # lock.acquire() #上锁保证 add 和 print 有序的一个一个进行 !2.5版本以后支持with操作
    with lock:
        remaining.add(myname)
        print('[%s] Started %s' % (ctime(), myname))
    # lock.release()    # 在这个释放后大家一起并行执行耗时代码 !2.5版本以后支持with操作
    sleep(nsec)     #模拟耗时操作
    with lock: #lock.acquire() #耗时操作完成后重新上锁 根据完成时间快慢上锁并执行最终代码 !2.5版本以后支持with操作
        remaining.remove(myname)
        print('[%s] Completed %s(%d secs)' % (ctime(), myname, nsec))
        print('(remaining: %s)' % (remaining or None))
    # lock.release() # 代码执行完成后释放锁 交给下一个线程 !2.5版本以后支持with操作

def _main():
    for pause in loops:
        Thread(target=loop, args=(pause,)).start() #创建新的进程并开始,每次调用都相当于创建新的实例对象 但没有赋值
@register
def _atexit():
    print('all Done at:', ctime())
if __name__ == '__main__':
    _main()
