def fibonacci(n):
    '''Generates a fibonacci number'''
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

num = int(input())
sum = 0
i = 0
fib_number = 0
while fib_number <= num:
    fib_number = fibonacci(i)
    if fib_number % 2 == 0:
        sum += fib_number
    i += 1
print(sum)
