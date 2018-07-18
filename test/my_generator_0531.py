def fibonacci(num):
    a = 0
    b = 1
    current = 0
    while current < num:
        current += 1
        a, b = b, a + b
        yield b - a
    return 'Done'

if __name__ == '__main__':
    fib = fibonacci(5)
    for i in fib:
        print(i)

    my_generator = (i for i in range(10))
    for i in my_generator:
        print(i)