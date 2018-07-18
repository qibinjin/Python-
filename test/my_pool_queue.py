import multiprocessing


def write(queue):
    for i in range(10):
        if queue.full():
            print('queue is full')
            return
        queue.put(i)


def read(queue):
    for i in range(10):
        if queue.empty():
            print('queue is empty')
            return
        print(queue.get())


if __name__ == '__main__':
    queue = multiprocessing.Manager().Queue(5)
    pool = multiprocessing.Pool(2)
    pool.apply_async(write, args=(queue,))
    pool.apply_async(read, args=(queue,))
    pool.close()
    pool.join()
