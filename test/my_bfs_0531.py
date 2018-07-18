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


#
# def bfs(start):
#     sum = 0
#     search_queue.append(start)
#     while search_queue:
#         if 5 in my_map[search_queue[0]]:
#             # print(sum)
#             return
#         if search_queue[0] not in searched:
#             searched.append(search_queue[0])
#             search_queue.extend(my_map[search_queue[0]])
#             # my_dict.get_walked(search_queue[0],)
#             print(search_queue)
#         search_queue.pop(0)
#         sum += 1
def get_step(start, stop):
    global walked
    if stop == start:
        return
    walked += 1
    return get_step(start, my_map.get_father(stop))


if __name__ == '__main__':
    # my_dict = NewDict()
    my_map = NewDict(((1, [2, 3]), (2, [3, 4]), (3, [4, 5]), (4, [5, 3]), (5, [4, 3])))
    # #
    # # print(my_map)
    # # {}
    # searched = []
    # search_queue = []
    # start = int(input('please input start point'))
    # bfs(start)
    get_step(1, 5)
    print(walked)
    # eval(1)
