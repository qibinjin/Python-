import multiprocessing, time


def sing():
    for _ in range(10):
        print('singing....')
        time.sleep(0.5)


def dance():
    sing_process = multiprocessing.Process(target=sing)
    sing_process.start()
    for _ in range(10):
        if _ == 5:
            # sing_process = q.get()
            sing_process.terminate()
            sing_process.join()
        print('dancing....')
        time.sleep(0.5)



if __name__ == '__main__':
    # q = multiprocessing.Queue()


    dance_process = multiprocessing.Process(target=dance)

    dance_process.start()
    # sing_process.start()
    # q.put(sing_process)


    print('test....')
