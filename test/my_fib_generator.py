
def fibonacci(num):
    a = 0
    b = 1
    current = 0

    while current < num:
        current += 1
        ret = a
        a, b = b, a + b
        yield ret
    return 'Stop iteration'

if __name__ == '__main__':
    fib = fibonacci(5)
    for i in fib:
        print(i)
