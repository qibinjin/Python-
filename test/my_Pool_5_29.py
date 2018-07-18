from multiprocessing import Manager, Pool
import time


def main():
    for _ in range(10):
        print('asdfasdasd')
        time.sleep(1)
        print(q.get())


if __name__ == '__main__':
    po = Pool(3)
    q = Manager().Queue()


    for _ in range(10):
        q.put('adsasd')
        po.apply_async(main)

    po.close()
    po.join()


