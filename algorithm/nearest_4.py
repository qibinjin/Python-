numbers = [1, 0 ,-1, 0, -2, 2]
target = 0
numbers = sorted(numbers)
ret = []
k = 0
i = len(numbers) - 1
v = 1
j = len(numbers) - 2
while k < i:
    while v < j:
        if numbers[k] + numbers[v] + numbers[i] + numbers[j] < target:
            v += 1
        elif numbers[k] + numbers[v] + numbers[i] + numbers[j] > target:
            j -= 1
        else:
            break
    if numbers[k] + numbers[v] + numbers[i] + numbers[j] == target:
        if sorted([numbers[k], numbers[v], numbers[i], numbers[j]]) not in ret:
            ret.append(sorted([numbers[k], numbers[v], numbers[i], numbers[j]]))

    k += 1
    v -= 1
    v = 1
    j = len(numbers) - 2



print(ret)
