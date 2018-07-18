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
        print('message:', queue.get())


if __name__ == '__main__':
    q = multiprocessing.Queue(5)
    write_process = multiprocessing.Process(target=write, args=(q,))
    read_process = multiprocessing.Process(target=read, args=(q,))
    write_process.start()
    write_process.join()
    read_process.start()
