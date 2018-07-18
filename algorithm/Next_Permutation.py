S = [1, 2, 3, 4]
my_list = []
used = []
ret = []


def dfs(step):
    global ret
    if step == 4:
        ret += my_list
        return
    for i in range(0, 4):
        if i not in used:
            my_list.insert(step, S[i])
            used.append(i)
            dfs(step + 1)
            my_list.remove(S[i])
            used.remove(i)
    return


dfs(0)
x = [ret[i:i + 4] for i in range(0, len(ret), 4)]
try:
    print(x[x.index([1, 2, 3, 4]) + 1], x.index([1, 2, 3, 4]) + 2)

except IndexError:
    print(x[0], 1)
