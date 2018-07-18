import time


def work1():
    while True:
        print('work1...')
        yield
        time.sleep(0.1)


def work2():
    while True:
        print('work2...')
        yield
        time.sleep(0.1)


if __name__ == '__main__':
    while True:
        next(work1())
        next(work2())
