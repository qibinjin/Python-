n = 3
X = {1, 2}


def staircase(n, X):
    cache = [0 for _ in range(n + 1)]
    cache[0] = 1
    for i in range(n + 1):
        cache[i] += sum(cache[i - x] for x in X if i - x > 0)  # cache[i] = cache[i - 步数1] + cache[i - 步数2]..等等
        cache[i] += 1 if i in X else 0  #若 i 属于集合X 则cache[i] + 1
    return cache[-1]
print(staircase(n, X))