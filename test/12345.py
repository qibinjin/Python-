import multiprocessing


def work1():
    for i in range(10):
        if q.full():
            print('queue is full')
            return
        q.put(i)


def work2():
    for i in range(10):
        if q.empty():
            if q.empty():
                print(' queue is empty')
                return
        print(q.get())


if __name__ == '__main__':
    q = multiprocessing.Manager().Queue(5)
    pool = multiprocessing.Pool(2)

    pool.apply_async(work1)
    pool.apply_async(work2)

    pool.close()
    pool.join()
