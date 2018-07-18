from collections import Iterable


def func(obj):
    if isinstance(obj, Iterable):
        print('%s is iterable:' % obj.__class__.__name__)
    else:
        print("%s isn't iterable:" % obj.__class__.__name__)


if __name__ == '__main__':
    func('abcbdbd')
    func([1, 3, 5])
    func((2, 4, 6))
    func({1, 5, 7})
    func({'name': 'xm'})
    func(range(10))
    func(10)
    print(isinstance(111, int))
