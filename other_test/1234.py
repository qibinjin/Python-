import multiprocessing

def write():
    for i in range(10):
        if queue.full():
            print('消息队列满了')
            return
        queue.put(i)
        print('write',multiprocessing.current_process())

def read():
    for i in range(10):
        if queue.empty():
            print('消息队列空了')
            return
        print(queue.get(),multiprocessing.current_process())

if __name__ == '__main__':
    # 进程池使用Manager()创建消息队列

    queue = multiprocessing.Manager().Queue(5)

    pool = multiprocessing.Pool(2)

    sub_process = pool.apply_async(write)
    sub_process.wait()
    pool.apply_async(read)

    pool.close()
    pool.join()
