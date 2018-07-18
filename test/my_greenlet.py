from greenlet import greenlet
import time


def work1():
    for i in range(10):
        print('work1.....')
        gr2.switch(10,'ab')
        time.sleep(0.1)


def work2(num,ab):
    for i in range(num):
        print('work2.....%s' % ab)
        gr1.switch()
        time.sleep(0.1)


if __name__ == '__main__':
    gr1 = greenlet(work1)
    gr2 = greenlet(work2)
    gr1.switch()
