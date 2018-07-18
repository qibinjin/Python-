import multiprocessing, time


def work():
    print(multiprocessing.current_process())
    print('work1')
    time.sleep(0.1)


if __name__ == '__main__':
    pool = multiprocessing.Pool(3)
    for i in range(10):
        pool.apply_async(work)

    pool.close()
    pool.join()
