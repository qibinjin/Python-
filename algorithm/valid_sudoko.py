my_list = []
with open('my_suduku.txt', 'r') as f:
    data = f.readlines()
    for i,j in enumerate(data):
        my_list.append([])
        my_list[i].extend([x for x in j.split(' ') if x != '\n' and x != ''])

def suduko():
    for num in my_list:
        for i in range(9):
            for j in range(i + 1, 9):
                if num[i] == num[j] and num[i] != '.':
                    print('数独不合法...')
                    return
    else:
        for k in range(9):
            for i in range(8):
                for j in range(i + 1, 9):
                    if my_list[i][k] == my_list[j][k] and my_list[i][k] != '.':
                        print('数独不合法....')
                        return
        else:
            for i in range(0,9,3):
                for j in range(0,9,3):
                    for k in range(i,i+3):
                        for v in range(j, j+3):
                            if k ==v :
                                if k != i+2:
                                    if my_list[k][v] == my_list[k+1][v+1]:
                                        print('数独不合法...')
                                        return
                                else:
                                    if my_list[k][k-2] == my_list[k-2][k]:
                                        print('数独不合法....')
                                        return

                            else:
                                if my_list[k][v] == my_list[v][k]:
                                    print('数独不合法...')
                                    return




