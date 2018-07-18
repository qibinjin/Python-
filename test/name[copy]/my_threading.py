import threading
import time


def sing(num):
    for _ in range(num):
        print('singing ...')
        time.sleep(0.5)


def dance(num):
    for _ in range(num):
        print('dancing...')
        time.sleep(0.5)


if __name__ == '__main__':
    # sing_thread = threading.Thread(target=sing, args=(10,))
    # dance_thread = threading.Thread(target=dance, args=(10,))

    threads = []
    funcs = [sing, dance]
    for i in range(2):
        t = threading.Thread(target=funcs[i], args=(10,))
        threads.append(t)

    for i in range(2):
        threads[i].start()

        # sing_thread.start()
        # dance_thread.start()
