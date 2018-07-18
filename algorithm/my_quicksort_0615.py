

def quicksort(list):
    if len(list) < 2:
        return list
    tmp = list[0]
    less = [x for x in list[1:] if x <= tmp]
    more = [x for x in list[1:] if x > tmp]
    return quicksort(less) + [tmp] + quicksort(more)

quicksort([6,5,4,2,1])