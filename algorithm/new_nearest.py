class NewDict(dict):
    def get_father(self, value):
        for k, v in self.items():
            if value == v or value in v:
                if k.__class__.__name__ == 'str':
                    return eval(k)
                else:
                    return k
        else:
            return False
walked = 0


def get_step(start, stop):
    global walked
    if stop == start:
        return
    walked += 1
    return get_step(start, my_map.get_father(stop))
if __name__ == '__main__':
    my_map = NewDict()
    # ((1, [2, 3]), (2, [1, 3, 4]), (3, [1, 2, 4, 5]), (4, [2, 5, 3]), (5, [4, 3]))
    m = int(input('please input num of points'))
    for i in range(m):
        my_map[int(input('please input key'))] = eval(input('please input value'))
    get_step(1, 5)
    print(walked)
