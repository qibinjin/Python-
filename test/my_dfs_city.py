def dfs(start, dis):
    global min
    if dis > min: return
    if start == dest:
        if dis < min: min = dis
        print(searched)
        print(min)
        return

    for i in my_map:
        if i[0] == start:
            if i not in searched:
                searched.append(i)
                dfs(i[1], dis + int(my_map[i]))
                searched.remove(i)
    return


if __name__ == '__main__':
    min = 9999999
    searched = []
    my_map = {}

    while True:
        a = input('please input source')
        b = input('please input desttination')
        c = input('please input distance')
        if a:
            my_map[(a, b)] = c
        else:
            break
    dest = input('please input dest')
    dfs('1', 0)
    print(my_map)
