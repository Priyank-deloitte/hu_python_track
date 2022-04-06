def fibonacciGenerator(n):
    a = 0
    b = 1
    yield a

    for i in range(n+1):
        yield b
        a, b = b, a + b


n = int(input("Enter Limit : "))
values = fibonacciGenerator(n)
for i in values:
    print(i)

