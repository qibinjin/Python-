import threading


class MyThread(threading.Thread):
    def __init__(self, name, my_func, args):
        threading.Thread.__init__(self)
        self.name = name
        self.myfunc = my_func
        self.args = args

    def run(self):
        self.myfunc(self.args)


def work1(name):
    print(name)
    print('work1')


def work2():
    print('work2')


if __name__ == '__main__':
    my_thread = MyThread('name', work1, 'xiaoming')
    my_thread.start()
