from multiprocessing import Pool
import os, time, random


def worker(msg):
    t_start = time.time()
    print('%s start runing ,pid is %d' % (msg, os.getpid()))
    time.sleep(random.random()*2)
    t_stop = time.time()
    print(msg, 'all done using time %0.2f' % (t_stop-t_start))

po = Pool(3)

for i in range(10):
    po.apply_async(worker, (i, ))

print('------start------')
po.close()
po.join()
print('------end------')