import time
def wrapper(func):
    def inner(*args, **kwargs):
        start = time.time()
        ret = func()
        print(time.time()-start)
        return ret
    return inner
@wrapper
def func():
    for i in range(10000):
        time.sleep(0.01)

func()