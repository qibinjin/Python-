def bfs(start):
    searched.append(start)
    search_queue.extend(my_dict[start])
    while search_queue:
        if search_queue[0] not in searched:
            search_queue.extend(my_dict[search_queue[0]])
            searched.append(search_queue.pop(0))
        else:
            search_queue.pop(0)
    print(searched)

if __name__ == '__main__':
    searched = []
    search_queue = []
    my_dict = {1: [2, 3, 5, 6], 2: [1, 4], 3: [1, 5], 4: [2], 5: [1, 3], 6: [4, 1]}
    bfs(1)

