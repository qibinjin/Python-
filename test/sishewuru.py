def name(num):
    str_list = str(num).split('.')
    if len(str_list[1]) > 1:
        if str_list[1][1] >= '5':
            return '%.1f' % (float(str_list[0] + '.' + str_list[1][0]) + 0.1)
        else:
            return '%.1f' % float(str_list[0] + '.' + str_list[1][0])
    else:
        return '%.1f' % float(str_list[0] + '.' + str_list[1][0])

if __name__ == '__main__':
    print(name(4.6783465245))
