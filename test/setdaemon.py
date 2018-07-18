import threading
import time


def work(name, age):
    for _ in range(10):

        print(name, age)
        print('working ...%d' % _)
        time.sleep(0.1)

def study():

    for _ in range(10):

        print('study....')
        time.sleep(0.1)



if __name__ == '__main__':
    single_thread = threading.Thread(target=work, args=('xiaoming', 22))
    study_thread = threading.Thread(target=study)

    single_thread.setDaemon(True)
    single_thread.start()
    study_thread.start()
    print('123123')
