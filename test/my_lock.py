import threading

lock = threading.Lock()
num = 0


def work1():
    global num
    # lock.acquire()
    # for _ in range(1000000):
    #     num += 1
    # print(num)
    # lock.release()
    with lock:
        for _ in range(1000000):
            num += 1
        print('work1', num)


def work2():
    global num
    # lock.acquire()
    # for _ in range(1000000):
    #     num += 1
    # print(num)
    # lock.release()
    with lock:
        for _ in range(1000000):
            num += 1
        print('work2', num)


if __name__ == '__main__':
    work1_thread = threading.Thread(target=work1)
    work2_thread = threading.Thread(target=work2)
    work1_thread.start()
    work2_thread.start()
