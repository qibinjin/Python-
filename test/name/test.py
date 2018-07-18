import threading
import time
my_list = []


def write():
    for i in range(10):
        my_list.append(i)
        print('write %s' % my_list)
        time.sleep(0.1)
    print('write %s' % my_list)


def read():
    write_thread.join()
    print('read %s' % my_list)


if __name__ == '__main__':
    write_thread = threading.Thread(target=write)
    read_thread = threading.Thread(target=read)

    write_thread.start()
    read_thread.start()
