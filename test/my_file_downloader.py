from multiprocessing import Manager, Pool
import os,time


def copy(q, file, dest_name):
    with open(file, 'rb') as f:
        with open(dest_name + file, 'wb') as w:
            while True:
                data = f.read(1024)
                w.write(data)
                # time.sleep(1)
                if not data:
                    break
    q.put(file)


if __name__ == '__main__':
    source_name = input('please input folder name')
    file_names = os.listdir(source_name)
    dest_name = source_name + '[copy]' + '/'
    po = Pool(5)
    q = Manager().Queue()

    try:
        os.mkdir(dest_name)
    except FileExistsError:
        pass

    file_names = os.listdir(source_name)
    for file in file_names:
        po.apply_async(copy, args=(q, file, dest_name))

    po.close()


    all_file_num = len(file_names)
    while True:
        name = q.get()
        if name in file_names:
            file_names.remove(name)
        copy_rate = (all_file_num - len(file_names)) * 100 / all_file_num
        print('%.2f-------%s' % (copy_rate, name))
        if copy_rate >= 100:
            break
