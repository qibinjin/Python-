import name
from time import ctime, sleep
def loop0():
    print('loop0 start at:', ctime())
    sleep(4)
    print('loop0 end at:', ctime())

def loop1():
    print('loop1 start at:', ctime())
    sleep(2)
    print('loop1 start at:', ctime())
threads = []

def main():

    for i in range(2):
        t = name.Thread(target=eval('loop%d' % i), args=())
        threads.append(t)

    for i in range(2):
        threads[i].start()
    for i in range(2):
        threads[i].join()
    print('all done', ctime())

if __name__ == '__main__':
    main()