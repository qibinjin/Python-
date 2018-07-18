class MyList(object):
    def __init__(self):
        self.items = []

    def add(self, num):
        self.items.append(num)

    def __iter__(self):
        return MyIterator(self.items)


class MyIterator(object):
    def __init__(self, items):
        self.items = items
        self.current = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        if self.current < len(self.items):
            return self.items[self.current]
        else:
            raise StopIteration


if __name__ == '__main__':
    my_list = MyList()
    my_list.add(1)
    my_list.add(3)
    my_list.add(4)
    # a = my_list.__iter__()
    # print(a.__next__())
    for i in my_list:
        print(i)
