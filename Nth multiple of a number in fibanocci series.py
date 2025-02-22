def nth_multiple_fibonacci(n, multiple):
    fib_series = [0, 1]
    while len(fib_series) < n:
        next_fib = fib_series[-1] + fib_series[-2]
        fib_series.append(next_fib)

    multiples = [fib for fib in fib_series if fib % multiple == 0]
    return multiples[n - 1] if n <= len(multiples) else None
a=int(input())
b=int(input())
print("Nth multiple of the given number in Fibonacci series:", nth_multiple_fibonacci(a,b))
