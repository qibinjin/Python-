import multiprocessing


class KaoYa(object):
    __count = 0  # 记录创建了多少次

    def __init__(self):
        KaoYa.__count += 1
        self.__count = KaoYa.__count

    def __str__(self):
        return "我是第%s只被烤熟的鸭子" % (self.__count)


def consumer(input_q, count=5):
    for kaoya in range(1, count):
        item = input_q.get()  # 消费几只烤鸭次
        print("消费者：", item)


def prodution(output_q, count=11):
    for i in range(1, count):
        item = KaoYa()
        output_q.put(item)  # 默认是循环10次生产10只鸭子
        print("生产者：", item)


# 创建进程
if __name__ == '__main__':
    joinable = multiprocessing.Queue(10)

    prodution_process = multiprocessing.Process(target=prodution, args=(joinable,))
    consumer_process = multiprocessing.Process(target=consumer, args=(joinable,))

    prodution_process.start()
    consumer_process.start()
