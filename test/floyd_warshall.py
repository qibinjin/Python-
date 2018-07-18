e = [[0, 0, 0, 0, 0],
     [0, 0, 2, 6, 4],
     [0, 9999, 0, 3, 9999],
     [0, 7, 9999, 0, 1],
     [0, 5, 9999, 12, 0]]

for k in range(1, 5):
    for i in range(1, 5):
        for j in range(1, 5):
            if e[i][j] > e[i][k] + e[k][j]:
                e[i][j] = e[i][k] + e[k][j]
e = [i[1:] for i in e[1:]]
print(e)
