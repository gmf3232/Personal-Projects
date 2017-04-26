def fibonacci(n):
    if n == 1 or n == 2:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

total = 0
i = 2

while i < 4000000:
    total += fibonacci(i)
    i += 2
