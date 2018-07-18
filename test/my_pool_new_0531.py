import os
import multiprocessing


def copy(name, source):
    dest_folder = source + '[copy]'

    try:
        os.mkdir(dest_folder)
    except FileExistsError:
        pass

    with open(source + '/' + name, 'r') as r:
        with open(dest_folder + '/' + name, 'w') as w:
            while True:
                data = r.read(1024)
                if data:
                    w.write(data)
                else:
                    print('file copy complete', name)
                    break


if __name__ == '__main__':
    pool = multiprocessing.Pool(3)
    source_folder = input('please input source_folder')
    file_names = os.listdir(source_folder)
    for file in file_names:
        pool.apply_async(copy, args=(file, source_folder))
    pool.close()
    pool.join()
